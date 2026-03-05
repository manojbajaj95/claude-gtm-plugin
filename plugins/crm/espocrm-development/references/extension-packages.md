# Extension Package Development Reference

## Overview

Extension packages are the recommended way to distribute custom functionality in EspoCRM. They provide a clean, version-controlled method for installing, upgrading, and uninstalling custom modules.

### Package Structure

```
MyExtension.zip
├── manifest.json                 # Package metadata and configuration
├── scripts/                      # Lifecycle scripts
│   ├── BeforeInstall.php
│   ├── AfterInstall.php
│   ├── BeforeUninstall.php
│   └── AfterUninstall.php
├── files/                        # Files to be copied to application
│   └── custom/
│       └── Espo/
│           └── Modules/
│               └── MyModule/
│                   ├── Resources/
│                   │   ├── metadata/
│                   │   │   ├── entityDefs/
│                   │   │   ├── clientDefs/
│                   │   │   └── scopes/
│                   │   ├── layouts/
│                   │   └── i18n/
│                   │       ├── en_US/
│                   │       └── de_DE/
│                   ├── Services/
│                   ├── Controllers/
│                   ├── Hooks/
│                   └── Entities/
└── data/                         # Optional: SQL scripts, data files
    └── schema.sql
```

## Manifest Configuration

### Basic manifest.json

```json
{
  "name": "My Extension",
  "version": "1.0.0",
  "acceptableVersions": [
    ">=8.0.0 <9.0.0"
  ],
  "description": "Description of what the extension does",
  "author": "Your Name",
  "license": "MIT",
  "skipBackup": false,
  "delete": []
}
```

### Manifest Fields

**Required Fields:**
- `name` (string) - Display name of the extension
- `version` (string) - Semantic version (e.g., "1.0.0", "2.1.3")
- `acceptableVersions` (array) - EspoCRM version compatibility

**Optional Fields:**
- `description` (string) - Detailed description
- `author` (string) - Author/company name
- `license` (string) - License type (MIT, GPL-3.0, Proprietary, etc.)
- `skipBackup` (boolean) - Skip backup creation during install (default: false)
- `delete` (array) - Files/directories to remove during installation
- `releaseDate` (string) - Release date (ISO format)
- `checkVersionUrl` (string) - URL to check for updates

### Version Constraints

Use composer-style version constraints:

```json
{
  "acceptableVersions": [
    ">=8.0.0 <9.0.0"  // Works with 8.x but not 9.x
  ]
}
```

Common patterns:
- `">=8.0.0"` - Version 8.0.0 or higher
- `">=8.0.0 <9.0.0"` - Version 8.x only
- `">=7.5.0 <8.2.0"` - Specific range
- `"*"` - Any version (not recommended)

### Delete Array - Cleanup Old Files

Use the `delete` array to remove files from previous versions or conflicting extensions:

```json
{
  "delete": [
    "custom/Espo/Modules/OldModule",
    "custom/Espo/Custom/Resources/metadata/entityDefs/ObsoleteEntity.json",
    "client/custom/modules/old-module"
  ]
}
```

**Important:**
- Paths are relative to EspoCRM root
- Use forward slashes (/) on all platforms
- Be careful not to delete core files

## Lifecycle Scripts

Lifecycle scripts execute at specific points during installation/uninstallation. They provide access to EspoCRM's services via dependency injection.

### Available Lifecycle Hooks

| Script | When Executed |
|--------|---------------|
| BeforeInstall.php | Before files are copied |
| AfterInstall.php | After files are copied, before cache rebuild |
| BeforeUninstall.php | Before files are removed |
| AfterUninstall.php | After files are removed |

### Script Template

All scripts follow this structure:

```php
<?php
namespace Espo\Modules\MyModule;

use Espo\Core\Container;

class BeforeInstall
{
    private Container $container;

    public function run(Container $container): void
    {
        $this->container = $container;

        // Script logic here
    }
}
```

### BeforeInstall.php - Pre-Installation Validation

Use to validate system requirements and prerequisites:

```php
<?php
namespace Espo\Modules\MyModule;

use Espo\Core\Container;
use Espo\Core\Exceptions\Error;
use Espo\ORM\EntityManager;

class BeforeInstall
{
    private Container $container;

    public function run(Container $container): void
    {
        $this->container = $container;

        $this->checkRequirements();
        $this->validateConfiguration();
    }

    private function checkRequirements(): void
    {
        // Check PHP extensions
        if (!extension_loaded('curl')) {
            throw new Error('MyModule requires PHP cURL extension');
        }

        // Check PHP version
        if (version_compare(PHP_VERSION, '8.1.0', '<')) {
            throw new Error('MyModule requires PHP 8.1 or higher');
        }

        // Check for conflicting extensions
        $entityManager = $this->container->get('entityManager');
        $existingExtension = $entityManager
            ->getRDBRepository('Extension')
            ->where(['name' => 'ConflictingExtension'])
            ->findOne();

        if ($existingExtension) {
            throw new Error('Please uninstall ConflictingExtension before installing MyModule');
        }
    }

    private function validateConfiguration(): void
    {
        $config = $this->container->get('config');

        // Check required config values
        if (!$config->get('siteUrl')) {
            throw new Error('Site URL must be configured before installing MyModule');
        }
    }
}
```

### AfterInstall.php - Post-Installation Setup

Use for database initialization, default data creation, and configuration:

```php
<?php
namespace Espo\Modules\MyModule;

use Espo\Core\Container;
use Espo\ORM\EntityManager;
use Espo\Core\Utils\Config;
use Espo\Core\Utils\Metadata;
use Espo\Core\Utils\File\Manager as FileManager;

class AfterInstall
{
    private Container $container;

    public function run(Container $container): void
    {
        $this->container = $container;

        $this->createDatabaseSchema();
        $this->insertDefaultData();
        $this->updateConfiguration();
        $this->createDirectories();
    }

    private function createDatabaseSchema(): void
    {
        $entityManager = $this->container->get('entityManager');
        $pdo = $entityManager->getPDO();

        // Execute SQL from package data directory
        $sqlFile = 'data/schema.sql';
        if (file_exists($sqlFile)) {
            $sql = file_get_contents($sqlFile);
            $pdo->exec($sql);
        }

        // Or create tables programmatically
        $sql = "
            CREATE TABLE IF NOT EXISTS `my_custom_table` (
                `id` VARCHAR(24) NOT NULL PRIMARY KEY,
                `name` VARCHAR(255),
                `status` VARCHAR(50),
                `created_at` DATETIME,
                `modified_at` DATETIME,
                `deleted` TINYINT(1) DEFAULT 0
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        ";
        $pdo->exec($sql);
    }

    private function insertDefaultData(): void
    {
        $entityManager = $this->container->get('entityManager');

        // Create default entities
        $defaultCategories = ['Sales', 'Marketing', 'Support'];

        foreach ($defaultCategories as $categoryName) {
            // Check if already exists
            $existing = $entityManager
                ->getRDBRepository('MyCategory')
                ->where(['name' => $categoryName])
                ->findOne();

            if (!$existing) {
                $category = $entityManager->getNewEntity('MyCategory');
                $category->set([
                    'name' => $categoryName,
                    'status' => 'Active'
                ]);
                $entityManager->saveEntity($category);
            }
        }
    }

    private function updateConfiguration(): void
    {
        $config = $this->container->get('config');
        $configWriter = $this->container->get('configWriter');

        // Add custom configuration values
        $configWriter->set('myModuleApiKey', $this->generateApiKey());
        $configWriter->set('myModuleEnabled', true);
        $configWriter->save();
    }

    private function createDirectories(): void
    {
        $fileManager = $this->container->get('fileManager');

        $directories = [
            'data/upload/mymodule',
            'data/cache/mymodule',
            'data/logs/mymodule'
        ];

        foreach ($directories as $dir) {
            if (!file_exists($dir)) {
                $fileManager->mkdir($dir, 0755, true);
            }
        }
    }

    private function generateApiKey(): string
    {
        return bin2hex(random_bytes(32));
    }
}
```

### BeforeUninstall.php - Pre-Uninstallation Cleanup

Use for data validation and backup before removal:

```php
<?php
namespace Espo\Modules\MyModule;

use Espo\Core\Container;
use Espo\Core\Exceptions\Error;
use Espo\ORM\EntityManager;

class BeforeUninstall
{
    private Container $container;

    public function run(Container $container): void
    {
        $this->container = $container;

        $this->checkDependencies();
        $this->backupData();
        $this->notifyUsers();
    }

    private function checkDependencies(): void
    {
        $entityManager = $this->container->get('entityManager');

        // Check if other extensions depend on this one
        $dependentExtensions = $entityManager
            ->getRDBRepository('Extension')
            ->where(['dependencies' => '%MyModule%'])
            ->find();

        if (count($dependentExtensions) > 0) {
            $names = array_map(fn($e) => $e->get('name'), iterator_to_array($dependentExtensions));
            throw new Error(
                'Cannot uninstall MyModule. These extensions depend on it: ' .
                implode(', ', $names)
            );
        }

        // Check for data that will be lost
        $recordCount = $entityManager
            ->getRDBRepository('MyEntity')
            ->where(['deleted' => false])
            ->count();

        if ($recordCount > 0) {
            throw new Error(
                "Warning: Uninstalling will delete {$recordCount} MyEntity records. " .
                "Please export your data before uninstalling."
            );
        }
    }

    private function backupData(): void
    {
        $entityManager = $this->container->get('entityManager');
        $fileManager = $this->container->get('fileManager');

        // Export data to JSON
        $records = $entityManager
            ->getRDBRepository('MyEntity')
            ->find();

        $backup = [
            'timestamp' => date('Y-m-d H:i:s'),
            'version' => '1.0.0',
            'records' => []
        ];

        foreach ($records as $record) {
            $backup['records'][] = $record->toArray();
        }

        $backupFile = 'data/mymodule_backup_' . date('Ymd_His') . '.json';
        $fileManager->putContents($backupFile, json_encode($backup, JSON_PRETTY_PRINT));
    }

    private function notifyUsers(): void
    {
        $entityManager = $this->container->get('entityManager');

        // Send notification to admins
        $admins = $entityManager
            ->getRDBRepository('User')
            ->where(['isAdmin' => true, 'isActive' => true])
            ->find();

        foreach ($admins as $admin) {
            $notification = $entityManager->getNewEntity('Notification');
            $notification->set([
                'type' => 'System',
                'userId' => $admin->getId(),
                'message' => 'MyModule extension has been uninstalled',
                'data' => [
                    'timestamp' => date('Y-m-d H:i:s')
                ]
            ]);
            $entityManager->saveEntity($notification);
        }
    }
}
```

### AfterUninstall.php - Post-Uninstallation Cleanup

Use to remove custom tables, clean configuration, and remove residual files:

```php
<?php
namespace Espo\Modules\MyModule;

use Espo\Core\Container;
use Espo\ORM\EntityManager;

class AfterUninstall
{
    private Container $container;

    public function run(Container $container): void
    {
        $this->container = $container;

        $this->dropDatabaseTables();
        $this->cleanConfiguration();
        $this->removeCustomDirectories();
    }

    private function dropDatabaseTables(): void
    {
        $entityManager = $this->container->get('entityManager');
        $pdo = $entityManager->getPDO();

        // Drop custom tables
        $tables = [
            'my_custom_table',
            'my_module_settings'
        ];

        foreach ($tables as $table) {
            $pdo->exec("DROP TABLE IF EXISTS `{$table}`");
        }
    }

    private function cleanConfiguration(): void
    {
        $configWriter = $this->container->get('configWriter');

        // Remove module-specific config values
        $configWriter->remove('myModuleApiKey');
        $configWriter->remove('myModuleEnabled');
        $configWriter->save();
    }

    private function removeCustomDirectories(): void
    {
        $fileManager = $this->container->get('fileManager');

        $directories = [
            'data/upload/mymodule',
            'data/cache/mymodule',
            'data/logs/mymodule'
        ];

        foreach ($directories as $dir) {
            if (file_exists($dir)) {
                $fileManager->removeInDir($dir, true);
                $fileManager->rmdir($dir);
            }
        }
    }
}
```

### Available Container Services

Common services available in lifecycle scripts:

```php
// Core services
$entityManager = $container->get('entityManager');
$metadata = $container->get('metadata');
$config = $container->get('config');
$configWriter = $container->get('configWriter');
$fileManager = $container->get('fileManager');
$dataManager = $container->get('dataManager');

// Utility services
$dateTime = $container->get('dateTime');
$language = $container->get('language');
$log = $container->get('log');

// Service factory
$serviceFactory = $container->get('serviceFactory');
$myService = $serviceFactory->create('MyEntity');
```

## File Organization

### Module Directory Structure

Files in the `files/` directory are copied directly to the EspoCRM installation:

```
files/
└── custom/
    └── Espo/
        └── Modules/
            └── MyModule/
                ├── Resources/
                │   ├── metadata/          # Entity and app definitions
                │   │   ├── entityDefs/
                │   │   │   └── MyEntity.json
                │   │   ├── clientDefs/
                │   │   │   └── MyEntity.json
                │   │   ├── scopes/
                │   │   │   └── MyEntity.json
                │   │   └── app/
                │   │       └── scheduledJobs.json
                │   ├── layouts/           # UI layouts
                │   │   └── MyEntity/
                │   │       ├── detail.json
                │   │       └── list.json
                │   └── i18n/             # Translations
                │       ├── en_US/
                │       │   └── MyEntity.json
                │       └── de_DE/
                │           └── MyEntity.json
                ├── Services/             # Business logic
                │   └── MyEntity.php
                ├── Controllers/          # API endpoints
                │   └── MyEntity.php
                ├── Hooks/               # Lifecycle hooks
                │   └── MyEntity/
                │       └── Validation.php
                ├── Entities/            # Entity classes
                │   └── MyEntity.php
                ├── Repositories/        # Data access
                │   └── MyEntity.php
                └── Jobs/               # Scheduled jobs
                    └── MyCustomJob.php
```

### Namespace Convention

All module code MUST follow this namespace pattern:

```php
<?php
namespace Espo\Modules\MyModule\{SubDirectory};

// Examples:
namespace Espo\Modules\MyModule\Services;
namespace Espo\Modules\MyModule\Controllers;
namespace Espo\Modules\MyModule\Hooks\MyEntity;
```

### Metadata Example - Entity Definition

`files/custom/Espo/Modules/MyModule/Resources/metadata/entityDefs/MyEntity.json`:

```json
{
  "fields": {
    "name": {
      "type": "varchar",
      "required": true,
      "maxLength": 255
    },
    "status": {
      "type": "enum",
      "options": ["New", "In Progress", "Complete"],
      "default": "New"
    },
    "description": {
      "type": "text"
    }
  },
  "links": {
    "account": {
      "type": "belongsTo",
      "entity": "Account",
      "foreign": "myEntities"
    }
  }
}
```

### Metadata Example - Scope Definition

`files/custom/Espo/Modules/MyModule/Resources/metadata/scopes/MyEntity.json`:

```json
{
  "entity": true,
  "object": true,
  "layouts": true,
  "tab": true,
  "acl": true,
  "module": "MyModule",
  "stream": true,
  "disabled": false
}
```

## Building and Packaging

### Manual Packaging

```bash
# 1. Create package directory
mkdir MyExtension-1.0.0
cd MyExtension-1.0.0

# 2. Create manifest
cat > manifest.json << 'EOF'
{
  "name": "My Extension",
  "version": "1.0.0",
  "acceptableVersions": [">=8.0.0 <9.0.0"],
  "author": "Your Name"
}
EOF

# 3. Create directory structure
mkdir -p files/custom/Espo/Modules/MyModule/Resources/metadata
mkdir -p scripts

# 4. Add your files
cp -r /path/to/your/code/* files/

# 5. Create lifecycle scripts (optional)
touch scripts/AfterInstall.php

# 6. Create ZIP package
zip -r MyExtension-1.0.0.zip manifest.json files/ scripts/

# 7. Package is ready: MyExtension-1.0.0.zip
```

### Automated Build Script

Create `build.sh`:

```bash
#!/bin/bash

NAME="MyExtension"
VERSION="1.0.0"
BUILD_DIR="build"
PACKAGE_NAME="${NAME}-${VERSION}"

# Clean previous builds
rm -rf ${BUILD_DIR}
mkdir -p ${BUILD_DIR}/${PACKAGE_NAME}

# Copy files
cp manifest.json ${BUILD_DIR}/${PACKAGE_NAME}/
cp -r files ${BUILD_DIR}/${PACKAGE_NAME}/
cp -r scripts ${BUILD_DIR}/${PACKAGE_NAME}/

# Create package
cd ${BUILD_DIR}
zip -r ${PACKAGE_NAME}.zip ${PACKAGE_NAME}
cd ..

echo "Package created: ${BUILD_DIR}/${PACKAGE_NAME}.zip"
```

## Installation Methods

### Via Admin UI

1. Navigate to **Administration > Extensions**
2. Click **Upload** button
3. Select your `.zip` package file
4. Click **Install**
5. Review changes and confirm
6. Wait for installation to complete
7. Click **Rebuild** when prompted

### Via CLI

```bash
# Install extension
php command.php extension --file="path/to/MyExtension-1.0.0.zip"

# Uninstall extension
php command.php extension --uninstall="My Extension"

# List installed extensions
php command.php extension --list

# Rebuild after installation
php command.php rebuild
```

### Programmatic Installation

```php
<?php
use Espo\Core\Container;
use Espo\Core\Utils\File\Manager as FileManager;

$container = $GLOBALS['container'];
$fileManager = $container->get('fileManager');

// Copy extension package to upload directory
$packagePath = 'data/upload/extensions/MyExtension-1.0.0.zip';
$fileManager->copy('/path/to/package.zip', $packagePath);

// Install via API
$extensionManager = $container->get('extensionManager');
$extensionManager->install($packagePath);
```

## Upgrade Packages

Create upgrade packages to update existing installations:

### Upgrade Package Structure

```
MyExtension-Upgrade-1.0.0-to-1.1.0.zip
├── manifest.json
├── scripts/
│   └── AfterUpgrade.php
└── files/
    └── custom/
        └── Espo/
            └── Modules/
                └── MyModule/
                    └── (only changed files)
```

### Upgrade Manifest

```json
{
  "name": "My Extension",
  "version": "1.1.0",
  "acceptableVersions": [">=8.0.0 <9.0.0"],
  "isUpgrade": true,
  "upgradeFrom": ["1.0.0"],
  "description": "Upgrade from 1.0.0 to 1.1.0",
  "delete": [
    "custom/Espo/Modules/MyModule/Services/DeprecatedService.php"
  ]
}
```

### AfterUpgrade.php Script

```php
<?php
namespace Espo\Modules\MyModule;

use Espo\Core\Container;
use Espo\ORM\EntityManager;

class AfterUpgrade
{
    private Container $container;

    public function run(Container $container): void
    {
        $this->container = $container;

        $this->migrateData();
        $this->updateConfiguration();
    }

    private function migrateData(): void
    {
        $entityManager = $this->container->get('entityManager');

        // Update existing records for schema changes
        $entities = $entityManager
            ->getRDBRepository('MyEntity')
            ->find();

        foreach ($entities as $entity) {
            // Migrate old field to new field
            if (!$entity->get('newField') && $entity->get('oldField')) {
                $entity->set('newField', $entity->get('oldField'));
                $entityManager->saveEntity($entity);
            }
        }
    }

    private function updateConfiguration(): void
    {
        $configWriter = $this->container->get('configWriter');

        // Add new config option
        $configWriter->set('myModuleNewFeature', true);
        $configWriter->save();
    }
}
```

## Best Practices

### DO: Use Lifecycle Scripts for Data Migration

```php
// ✅ CORRECT - Migrate data in AfterInstall
class AfterInstall
{
    public function run(Container $container): void
    {
        $entityManager = $container->get('entityManager');

        // Create default data
        $defaultSettings = $entityManager->getNewEntity('MyModuleSettings');
        $defaultSettings->set(['enabled' => true]);
        $entityManager->saveEntity($defaultSettings);
    }
}
```

### DO: Provide Clear Uninstall Cleanup

```php
// ✅ CORRECT - Clean up properly in AfterUninstall
class AfterUninstall
{
    public function run(Container $container): void
    {
        // Remove all traces
        $this->dropTables($container);
        $this->removeConfiguration($container);
        $this->cleanFiles($container);
    }
}
```

### DO: Validate Version Compatibility

```json
{
  "acceptableVersions": [
    ">=8.0.0 <9.0.0"
  ]
}
```

```php
// ✅ CORRECT - Check EspoCRM version in BeforeInstall
class BeforeInstall
{
    public function run(Container $container): void
    {
        $config = $container->get('config');
        $version = $config->get('version');

        if (version_compare($version, '8.0.0', '<')) {
            throw new Error('Requires EspoCRM 8.0.0 or higher');
        }
    }
}
```

### DO: Handle Errors Gracefully

```php
// ✅ CORRECT - Use try-catch and rollback
class AfterInstall
{
    public function run(Container $container): void
    {
        $entityManager = $container->get('entityManager');
        $transactionManager = $container->get('transactionManager');

        try {
            $transactionManager->run(function () use ($entityManager) {
                $this->createSchema($entityManager);
                $this->insertData($entityManager);
            });
        } catch (\Throwable $e) {
            $log = $container->get('log');
            $log->error('Installation failed: ' . $e->getMessage());
            throw $e; // Re-throw to fail installation
        }
    }
}
```

### DON'T: Modify Core Files

```php
// ❌ WRONG - Never modify core files
files/
└── application/          // Don't touch core!
    └── Espo/
        └── Core/
            └── (modified core file)

// ✅ CORRECT - Always use custom/ directory
files/
└── custom/
    └── Espo/
        └── Modules/
            └── MyModule/
```

### DON'T: Skip acceptableVersions

```json
// ❌ WRONG - No version check
{
  "name": "My Extension",
  "version": "1.0.0"
}

// ✅ CORRECT - Always specify compatible versions
{
  "name": "My Extension",
  "version": "1.0.0",
  "acceptableVersions": [">=8.0.0 <9.0.0"]
}
```

### DON'T: Leave Orphaned Data

```php
// ❌ WRONG - No cleanup in AfterUninstall
class AfterUninstall
{
    public function run(Container $container): void
    {
        // Does nothing - leaves data behind
    }
}

// ✅ CORRECT - Clean up everything
class AfterUninstall
{
    public function run(Container $container): void
    {
        $this->dropCustomTables($container);
        $this->removeConfiguration($container);
        $this->deleteCustomFiles($container);
    }
}
```

### DON'T: Hard-Code Database Credentials

```php
// ❌ WRONG - Hard-coded credentials
class AfterInstall
{
    public function run(Container $container): void
    {
        $pdo = new PDO('mysql:host=localhost;dbname=espocrm', 'root', 'password');
    }
}

// ✅ CORRECT - Use EntityManager (uses config automatically)
class AfterInstall
{
    public function run(Container $container): void
    {
        $entityManager = $container->get('entityManager');
        $pdo = $entityManager->getPDO();
    }
}
```

## Testing Your Extension

### Test Installation

1. **Fresh Install**: Test on clean EspoCRM instance
2. **Verify Files**: Check all files copied correctly to `custom/`
3. **Check Logs**: Review `data/logs/espo.log` for errors
4. **Test Functionality**: Verify all features work as expected
5. **Check Cache**: Ensure rebuild completes successfully

### Test Uninstallation

1. **Before Uninstall**: Note all files, tables, and config values
2. **Uninstall**: Use Admin UI or CLI
3. **Verify Cleanup**: Ensure all module data is removed
4. **Check Residual**: No leftover files in `custom/Espo/Modules/MyModule/`
5. **Database Check**: Verify custom tables are dropped

### Test Upgrade

1. **Install v1.0.0**: Install initial version
2. **Create Test Data**: Add some records
3. **Install v1.1.0**: Install upgrade package
4. **Verify Migration**: Check data migrated correctly
5. **Test Features**: Ensure old and new features work

## Common Issues

### Issue: Extension Won't Install

**Symptoms**: Installation fails with generic error

**Solution**:
```php
// Check logs
tail -f data/logs/espo.log

// Common causes:
// 1. Invalid manifest.json syntax
// 2. Script errors in lifecycle hooks
// 3. Version incompatibility
// 4. Insufficient permissions
```

### Issue: Files Not Copied

**Symptoms**: Files from package not appearing in `custom/`

**Solution**:
```bash
# Check file permissions
chmod -R 755 custom/
chown -R www-data:www-data custom/

# Verify ZIP structure
unzip -l MyExtension-1.0.0.zip

# Should show:
# manifest.json
# files/custom/Espo/Modules/...
```

### Issue: Cache Not Rebuilding

**Symptoms**: Changes not visible after install

**Solution**:
```bash
# Manual rebuild
php command.php rebuild

# Clear cache
rm -rf data/cache/*

# Check rebuild logs
tail -f data/logs/espo.log
```

### Issue: Database Changes Not Applied

**Symptoms**: Lifecycle script runs but no database changes

**Solution**:
```php
// Use transactions and check for errors
class AfterInstall
{
    public function run(Container $container): void
    {
        $log = $container->get('log');
        $entityManager = $container->get('entityManager');

        try {
            $pdo = $entityManager->getPDO();
            $sql = "CREATE TABLE IF NOT EXISTS my_table (...)";
            $result = $pdo->exec($sql);

            $log->info('Table created, rows affected: ' . $result);
        } catch (\Exception $e) {
            $log->error('Table creation failed: ' . $e->getMessage());
            throw $e;
        }
    }
}
```

## Example: Complete Extension Package

See the `files/` directory structure for a complete, working example including:
- Manifest with all required fields
- Full lifecycle script suite
- Proper metadata organization
- Service layer implementation
- Database schema setup
- Configuration management
- Cleanup procedures

This provides a production-ready template for building your own extensions.
