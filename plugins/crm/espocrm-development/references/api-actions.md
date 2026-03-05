# API Actions & Custom Endpoints Reference

## Overview

EspoCRM provides two approaches for creating custom API endpoints:
1. **Action Classes** (Recommended) - Modern, single-responsibility classes
2. **Controllers** (Legacy) - Multiple actions in one class

## API Structure

- **Root Path**: `api/v1/`
- **Format**: REST API returning JSON
- **Content-Type**: `application/json` for POST/PUT with JSON payloads
- **Authentication**: API Key, HMAC, or Basic Auth

## Route Definition

Routes are defined in `Resources/routes.json`:

```json
[
    {
        "route": "/MyEntity/:id/customAction",
        "method": "post",
        "params": {
            "controller": "MyEntity",
            "action": "customAction"
        }
    },
    {
        "route": "/MyEntity/bulkProcess",
        "method": "post",
        "actionClassName": "Espo\\Modules\\MyModule\\Api\\BulkProcess"
    },
    {
        "route": "/Reports/:reportId/generate",
        "method": "get",
        "actionClassName": "Espo\\Modules\\MyModule\\Api\\GenerateReport"
    },
    {
        "route": "/Integration/sync",
        "method": "post",
        "actionClassName": "Espo\\Modules\\MyModule\\Api\\SyncData",
        "noAuth": true
    }
]
```

### Route Parameters

| Parameter | Description |
|-----------|-------------|
| `route` | URL pattern with `:param` placeholders |
| `method` | HTTP method (get, post, put, patch, delete) |
| `actionClassName` | Full class name for Action approach |
| `controller` + `action` | Controller name and method for legacy approach |
| `noAuth` | Allow unauthenticated access (webhooks, public endpoints) |

## Action Classes (Recommended)

### Basic Action

```php
<?php
namespace Espo\Modules\MyModule\Api;

use Espo\Core\Api\Action;
use Espo\Core\Api\Request;
use Espo\Core\Api\Response;
use Espo\Core\Api\ResponseComposer;
use Espo\Core\Exceptions\BadRequest;
use Espo\Core\Exceptions\Forbidden;
use Espo\Core\Exceptions\NotFound;
use Espo\ORM\EntityManager;
use Espo\Core\Acl;

class CustomAction implements Action
{
    public function __construct(
        private EntityManager $entityManager,
        private Acl $acl
    ) {}

    public function process(Request $request): Response
    {
        // Get route parameter
        $id = $request->getRouteParam('id');

        if (!$id) {
            throw new BadRequest('ID is required');
        }

        // Get entity
        $entity = $this->entityManager->getEntityById('MyEntity', $id);

        if (!$entity) {
            throw new NotFound();
        }

        // Check access
        if (!$this->acl->checkEntityRead($entity)) {
            throw new Forbidden();
        }

        // Process and return
        return ResponseComposer::json([
            'id' => $entity->getId(),
            'name' => $entity->get('name'),
            'status' => $entity->get('status')
        ]);
    }
}
```

### Action with POST Body

```php
<?php
namespace Espo\Modules\MyModule\Api;

use Espo\Core\Api\Action;
use Espo\Core\Api\Request;
use Espo\Core\Api\Response;
use Espo\Core\Api\ResponseComposer;
use Espo\Core\Exceptions\BadRequest;
use Espo\ORM\EntityManager;
use stdClass;

class CreateWithValidation implements Action
{
    public function __construct(
        private EntityManager $entityManager
    ) {}

    public function process(Request $request): Response
    {
        // Get JSON body
        $body = $request->getParsedBody();

        // Validate required fields
        $this->validate($body);

        // Create entity
        $entity = $this->entityManager->createEntity('MyEntity', [
            'name' => $body->name,
            'description' => $body->description ?? null,
            'priority' => $body->priority ?? 'Normal'
        ]);

        // Return created entity
        return ResponseComposer::json([
            'id' => $entity->getId(),
            'name' => $entity->get('name')
        ]);
    }

    private function validate(stdClass $body): void
    {
        if (empty($body->name)) {
            throw new BadRequest('Name is required');
        }

        if (strlen($body->name) > 255) {
            throw new BadRequest('Name must be 255 characters or less');
        }

        $allowedPriorities = ['Low', 'Normal', 'High', 'Urgent'];
        if (!empty($body->priority) && !in_array($body->priority, $allowedPriorities)) {
            throw new BadRequest('Invalid priority value');
        }
    }
}
```

### Action with Query Parameters

```php
<?php
namespace Espo\Modules\MyModule\Api;

use Espo\Core\Api\Action;
use Espo\Core\Api\Request;
use Espo\Core\Api\Response;
use Espo\Core\Api\ResponseComposer;
use Espo\ORM\EntityManager;

class SearchWithFilters implements Action
{
    public function __construct(
        private EntityManager $entityManager
    ) {}

    public function process(Request $request): Response
    {
        // Get query parameters
        $status = $request->getQueryParam('status');
        $offset = (int) ($request->getQueryParam('offset') ?? 0);
        $limit = min((int) ($request->getQueryParam('limit') ?? 20), 100);
        $orderBy = $request->getQueryParam('orderBy') ?? 'createdAt';
        $order = $request->getQueryParam('order') ?? 'desc';

        // Build query
        $repository = $this->entityManager->getRDBRepository('MyEntity');

        if ($status) {
            $repository->where(['status' => $status]);
        }

        $collection = $repository
            ->order($orderBy, strtoupper($order))
            ->limit($offset, $limit)
            ->find();

        $total = $repository->count();

        // Format response
        $list = [];
        foreach ($collection as $entity) {
            $list[] = [
                'id' => $entity->getId(),
                'name' => $entity->get('name'),
                'status' => $entity->get('status'),
                'createdAt' => $entity->get('createdAt')
            ];
        }

        return ResponseComposer::json([
            'total' => $total,
            'list' => $list
        ]);
    }
}
```

### Action with File Upload

```php
<?php
namespace Espo\Modules\MyModule\Api;

use Espo\Core\Api\Action;
use Espo\Core\Api\Request;
use Espo\Core\Api\Response;
use Espo\Core\Api\ResponseComposer;
use Espo\Core\Exceptions\BadRequest;
use Espo\Core\FileStorage\Manager as FileStorageManager;
use Espo\ORM\EntityManager;
use Psr\Http\Message\UploadedFileInterface;

class UploadAttachment implements Action
{
    public function __construct(
        private EntityManager $entityManager,
        private FileStorageManager $fileStorageManager
    ) {}

    public function process(Request $request): Response
    {
        $uploadedFiles = $request->getUploadedFiles();

        if (empty($uploadedFiles['file'])) {
            throw new BadRequest('No file uploaded');
        }

        /** @var UploadedFileInterface $uploadedFile */
        $uploadedFile = $uploadedFiles['file'];

        // Validate file
        $allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
        $mimeType = $uploadedFile->getClientMediaType();

        if (!in_array($mimeType, $allowedTypes)) {
            throw new BadRequest('Invalid file type');
        }

        // Create attachment entity
        $attachment = $this->entityManager->createEntity('Attachment', [
            'name' => $uploadedFile->getClientFilename(),
            'type' => $mimeType,
            'size' => $uploadedFile->getSize()
        ]);

        // Store file
        $stream = $uploadedFile->getStream();
        $this->fileStorageManager->putStream($attachment, $stream);

        return ResponseComposer::json([
            'id' => $attachment->getId(),
            'name' => $attachment->get('name')
        ]);
    }
}
```

### Action with Custom Response

```php
<?php
namespace Espo\Modules\MyModule\Api;

use Espo\Core\Api\Action;
use Espo\Core\Api\Request;
use Espo\Core\Api\Response;

class DownloadFile implements Action
{
    public function process(Request $request): Response
    {
        $id = $request->getRouteParam('id');

        // Get file content
        $content = $this->getFileContent($id);
        $filename = $this->getFilename($id);

        $response = new Response();
        $response
            ->setStatus(200)
            ->setHeader('Content-Type', 'application/octet-stream')
            ->setHeader('Content-Disposition', 'attachment; filename="' . $filename . '"')
            ->setHeader('Content-Length', (string) strlen($content))
            ->writeBody($content);

        return $response;
    }

    private function getFileContent(string $id): string
    {
        // Implementation
        return '';
    }

    private function getFilename(string $id): string
    {
        return 'file.pdf';
    }
}
```

## Controller Approach (Legacy)

For multiple related actions, use a controller:

```php
<?php
namespace Espo\Modules\MyModule\Controllers;

use Espo\Core\Controllers\RecordBase;
use Espo\Core\Api\Request;
use Espo\Core\Exceptions\BadRequest;
use Espo\Core\Exceptions\Forbidden;

class MyEntity extends RecordBase
{
    // POST MyEntity/:id/markComplete
    public function postActionMarkComplete(Request $request): object
    {
        $id = $request->getRouteParam('id');
        $data = $request->getParsedBody();

        if (!$id) {
            throw new BadRequest('ID is required');
        }

        $service = $this->getRecordService();
        $entity = $service->markComplete($id, $data);

        return $entity->getValueMap();
    }

    // GET MyEntity/:id/summary
    public function getActionSummary(Request $request): object
    {
        $id = $request->getRouteParam('id');

        $service = $this->getRecordService();
        return $service->getSummary($id);
    }

    // PUT MyEntity/:id/reassign
    public function putActionReassign(Request $request): object
    {
        $id = $request->getRouteParam('id');
        $data = $request->getParsedBody();

        if (empty($data->assignedUserId)) {
            throw new BadRequest('assignedUserId is required');
        }

        $service = $this->getRecordService();
        $entity = $service->reassign($id, $data->assignedUserId);

        return $entity->getValueMap();
    }

    // DELETE MyEntity/:id/attachment/:attachmentId
    public function deleteActionRemoveAttachment(Request $request): bool
    {
        $id = $request->getRouteParam('id');
        $attachmentId = $request->getRouteParam('attachmentId');

        $service = $this->getRecordService();
        $service->removeAttachment($id, $attachmentId);

        return true;
    }
}
```

### Controller Route Configuration

```json
[
    {
        "route": "/MyEntity/:id/markComplete",
        "method": "post",
        "params": {
            "controller": "MyEntity",
            "action": "markComplete"
        }
    },
    {
        "route": "/MyEntity/:id/summary",
        "method": "get",
        "params": {
            "controller": "MyEntity",
            "action": "summary"
        }
    },
    {
        "route": "/MyEntity/:id/reassign",
        "method": "put",
        "params": {
            "controller": "MyEntity",
            "action": "reassign"
        }
    },
    {
        "route": "/MyEntity/:id/attachment/:attachmentId",
        "method": "delete",
        "params": {
            "controller": "MyEntity",
            "action": "removeAttachment"
        }
    }
]
```

## Authentication

### API Key Authentication

```bash
curl -X GET "https://your-espo/api/v1/Account" \
  -H "X-Api-Key: YOUR_API_KEY"
```

### HMAC Authentication (Most Secure)

```php
// Generate HMAC signature
$method = 'GET';
$uri = '/api/v1/Account';
$secretKey = 'your-secret-key';  // pragma: allowlist secret
$apiKey = 'your-api-key';  // pragma: allowlist secret

$string = $method . ' ' . $uri;
$signature = base64_encode(hash_hmac('sha256', $string, $secretKey, true));
$authHeader = base64_encode($apiKey . ':' . $signature);
```

```bash
curl -X GET "https://your-espo/api/v1/Account" \
  -H "X-Hmac-Authorization: $AUTH_HEADER"
```

### Webhook (No Auth)

For webhooks from external services:

```json
{
    "route": "/Webhook/stripe",
    "method": "post",
    "actionClassName": "Espo\\Modules\\Payment\\Api\\StripeWebhook",
    "noAuth": true
}
```

```php
<?php
namespace Espo\Modules\Payment\Api;

use Espo\Core\Api\Action;
use Espo\Core\Api\Request;
use Espo\Core\Api\Response;
use Espo\Core\Api\ResponseComposer;
use Espo\Core\Exceptions\BadRequest;

class StripeWebhook implements Action
{
    public function process(Request $request): Response
    {
        // Verify webhook signature
        $signature = $request->getHeader('Stripe-Signature');
        $payload = $request->getBodyContents();

        if (!$this->verifySignature($payload, $signature)) {
            throw new BadRequest('Invalid signature');
        }

        // Process webhook
        $event = json_decode($payload);
        $this->handleEvent($event);

        return ResponseComposer::json(['received' => true]);
    }

    private function verifySignature(string $payload, ?string $signature): bool
    {
        // Stripe signature verification
        return true;
    }

    private function handleEvent(object $event): void
    {
        // Handle different event types
    }
}
```

## Error Handling

### Standard Exceptions

```php
use Espo\Core\Exceptions\BadRequest;      // 400
use Espo\Core\Exceptions\Forbidden;       // 403
use Espo\Core\Exceptions\NotFound;        // 404
use Espo\Core\Exceptions\Conflict;        // 409
use Espo\Core\Exceptions\Error;           // 500

// Usage
throw new BadRequest('Invalid input data');
throw new Forbidden('Access denied');
throw new NotFound('Record not found');
throw new Conflict('Record has been modified');
throw new Error('Internal server error');
```

### Custom Error Response

```php
public function process(Request $request): Response
{
    try {
        // Processing logic
    } catch (\Exception $e) {
        $response = new Response();
        $response->setStatus(422);
        $response->writeBody(json_encode([
            'error' => 'Validation failed',
            'details' => $e->getMessage()
        ]));

        return $response;
    }
}
```

## Middleware and Access Control

### Check Entity Access

```php
public function process(Request $request): Response
{
    $id = $request->getRouteParam('id');
    $entity = $this->entityManager->getEntityById('MyEntity', $id);

    // Read access
    if (!$this->acl->checkEntityRead($entity)) {
        throw new Forbidden();
    }

    // Edit access
    if (!$this->acl->checkEntityEdit($entity)) {
        throw new Forbidden();
    }

    // Delete access
    if (!$this->acl->checkEntityDelete($entity)) {
        throw new Forbidden();
    }

    // Create access (scope level)
    if (!$this->acl->checkScope('MyEntity', 'create')) {
        throw new Forbidden();
    }
}
```

## OpenAPI Documentation

EspoCRM auto-generates OpenAPI spec at `/api/v1/OpenAPI`:

```bash
curl -X GET "https://your-espo/api/v1/OpenAPI" \
  -H "X-Api-Key: YOUR_API_KEY"
```

## Best Practices

### DO:
- Use Action classes for new endpoints (modern approach)
- Always validate input data
- Check ACL permissions before operations
- Use appropriate HTTP methods (GET for read, POST for create, etc.)
- Return meaningful error messages
- Log errors for debugging
- Clear cache after adding routes: `bin/command rebuild`

### DON'T:
- Skip authentication on sensitive endpoints
- Return stack traces in production
- Use GET for operations that modify data
- Bypass ACL checks
- Hardcode user IDs or entity types
- Forget to handle edge cases (null, empty, etc.)

## Resources

- [EspoCRM API Documentation](https://docs.espocrm.com/development/api/)
- [API Action Classes](https://docs.espocrm.com/development/api-action/)
- [Controllers](https://docs.espocrm.com/development/controllers/)
