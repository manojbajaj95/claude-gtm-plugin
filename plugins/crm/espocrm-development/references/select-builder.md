# Select Builder & Advanced Querying Reference

## Overview

The Select Builder constructs ORM queries while handling elements the ORM itself cannot manage: search parameters from frontend, access control restrictions, text filters, boolean filters, and primary filters.

## Basic Usage

### SelectBuilder Factory

```php
<?php
namespace Espo\Modules\MyModule\Services;

use Espo\Core\Select\SelectBuilderFactory;
use Espo\ORM\EntityManager;

class ReportService
{
    public function __construct(
        private SelectBuilderFactory $selectBuilderFactory,
        private EntityManager $entityManager
    ) {}

    public function getFilteredAccounts(): iterable
    {
        $query = $this->selectBuilderFactory
            ->create()
            ->from('Account')
            ->withStrictAccessControl()  // Apply ACL
            ->build();

        return $this->entityManager
            ->getRDBRepository('Account')
            ->clone($query)
            ->find();
    }
}
```

### With Search Parameters

```php
use Espo\Core\Select\SearchParams;

public function searchWithParams(array $params): iterable
{
    $searchParams = SearchParams::fromRaw($params);

    $query = $this->selectBuilderFactory
        ->create()
        ->from('Opportunity')
        ->withSearchParams($searchParams)
        ->withStrictAccessControl()
        ->build();

    return $this->entityManager
        ->getRDBRepository('Opportunity')
        ->clone($query)
        ->find();
}

// Example params from frontend:
// [
//     'primaryFilter' => 'open',
//     'boolFilterList' => ['onlyMy'],
//     'where' => [
//         ['type' => 'greaterThan', 'attribute' => 'amount', 'value' => 10000]
//     ],
//     'orderBy' => 'createdAt',
//     'order' => 'desc',
//     'offset' => 0,
//     'maxSize' => 20
// ]
```

## SearchParams Object

### Creating SearchParams

```php
use Espo\Core\Select\SearchParams;
use Espo\Core\Select\Where\Item as WhereItem;

// From raw array (API request)
$searchParams = SearchParams::fromRaw([
    'primaryFilter' => 'open',
    'where' => [
        ['type' => 'equals', 'attribute' => 'status', 'value' => 'Active']
    ]
]);

// Programmatic creation
$searchParams = SearchParams::create()
    ->withPrimaryFilter('open')
    ->withBoolFilter('onlyMy')
    ->withWhere(
        WhereItem::fromRaw([
            'type' => 'greaterThan',
            'attribute' => 'amount',
            'value' => 10000
        ])
    )
    ->withOrderBy('createdAt')
    ->withOrder('DESC')
    ->withOffset(0)
    ->withMaxSize(50);
```

### Where Clause Types

```php
// Comparison operators
['type' => 'equals', 'attribute' => 'status', 'value' => 'Active']
['type' => 'notEquals', 'attribute' => 'status', 'value' => 'Closed']
['type' => 'greaterThan', 'attribute' => 'amount', 'value' => 1000]
['type' => 'lessThan', 'attribute' => 'amount', 'value' => 50000]
['type' => 'greaterThanOrEquals', 'attribute' => 'probability', 'value' => 50]
['type' => 'lessThanOrEquals', 'attribute' => 'daysOpen', 'value' => 30]

// Null checks
['type' => 'isNull', 'attribute' => 'assignedUserId']
['type' => 'isNotNull', 'attribute' => 'closeDate']

// String matching
['type' => 'like', 'attribute' => 'name', 'value' => '%Corp%']
['type' => 'notLike', 'attribute' => 'name', 'value' => '%Test%']
['type' => 'startsWith', 'attribute' => 'name', 'value' => 'Acme']
['type' => 'endsWith', 'attribute' => 'website', 'value' => '.com']
['type' => 'contains', 'attribute' => 'description', 'value' => 'urgent']

// Array operations
['type' => 'in', 'attribute' => 'stage', 'value' => ['Proposal', 'Negotiation']]
['type' => 'notIn', 'attribute' => 'status', 'value' => ['Cancelled', 'Lost']]

// Date operations
['type' => 'today', 'attribute' => 'dueDate']
['type' => 'past', 'attribute' => 'closeDate']
['type' => 'future', 'attribute' => 'followUpDate']
['type' => 'lastXDays', 'attribute' => 'createdAt', 'value' => 7]
['type' => 'nextXDays', 'attribute' => 'dueDate', 'value' => 14]
['type' => 'currentMonth', 'attribute' => 'createdAt']
['type' => 'lastMonth', 'attribute' => 'createdAt']
['type' => 'currentQuarter', 'attribute' => 'closeDate']
['type' => 'currentYear', 'attribute' => 'createdAt']
['type' => 'between', 'attribute' => 'createdAt', 'value' => ['2024-01-01', '2024-12-31']]

// Logical operators
[
    'type' => 'or',
    'value' => [
        ['type' => 'equals', 'attribute' => 'status', 'value' => 'Active'],
        ['type' => 'equals', 'attribute' => 'priority', 'value' => 'High']
    ]
]

[
    'type' => 'and',
    'value' => [
        ['type' => 'greaterThan', 'attribute' => 'amount', 'value' => 10000],
        ['type' => 'notEquals', 'attribute' => 'stage', 'value' => 'Lost']
    ]
]
```

## Primary Filters

Primary filters are predefined named filters configured in metadata.

### Defining Primary Filters

In `metadata/selectDefs/{EntityType}.json`:

```json
{
    "primaryFilterClassNameMap": {
        "open": "Espo\\Modules\\MyModule\\Classes\\Select\\Opportunity\\PrimaryFilters\\Open",
        "myActive": "Espo\\Modules\\MyModule\\Classes\\Select\\Opportunity\\PrimaryFilters\\MyActive",
        "closingThisMonth": "Espo\\Modules\\MyModule\\Classes\\Select\\Opportunity\\PrimaryFilters\\ClosingThisMonth"
    }
}
```

### Implementing Primary Filter

```php
<?php
namespace Espo\Modules\MyModule\Classes\Select\Opportunity\PrimaryFilters;

use Espo\Core\Select\Primary\Filter;
use Espo\ORM\Query\SelectBuilder;
use Espo\Entities\User;

class Open implements Filter
{
    public function __construct(private User $user) {}

    public function apply(SelectBuilder $queryBuilder): void
    {
        $queryBuilder->where([
            'stage!=' => ['Closed Won', 'Closed Lost']
        ]);
    }
}

class MyActive implements Filter
{
    public function __construct(private User $user) {}

    public function apply(SelectBuilder $queryBuilder): void
    {
        $queryBuilder->where([
            'assignedUserId' => $this->user->getId(),
            'stage!=' => ['Closed Won', 'Closed Lost'],
            'deleted' => false
        ]);
    }
}

class ClosingThisMonth implements Filter
{
    public function apply(SelectBuilder $queryBuilder): void
    {
        $startOfMonth = date('Y-m-01');
        $endOfMonth = date('Y-m-t');

        $queryBuilder->where([
            'closeDate>=' => $startOfMonth,
            'closeDate<=' => $endOfMonth,
            'stage!=' => ['Closed Won', 'Closed Lost']
        ]);
    }
}
```

## Boolean Filters

Boolean filters are toggle-style filters.

### Defining Boolean Filters

In `metadata/selectDefs/{EntityType}.json`:

```json
{
    "boolFilterClassNameMap": {
        "onlyMy": "Espo\\Modules\\MyModule\\Classes\\Select\\Opportunity\\BoolFilters\\OnlyMy",
        "followed": "Espo\\Modules\\MyModule\\Classes\\Select\\Opportunity\\BoolFilters\\Followed",
        "highValue": "Espo\\Modules\\MyModule\\Classes\\Select\\Opportunity\\BoolFilters\\HighValue"
    }
}
```

### Implementing Boolean Filter

```php
<?php
namespace Espo\Modules\MyModule\Classes\Select\Opportunity\BoolFilters;

use Espo\Core\Select\Bool\Filter;
use Espo\ORM\Query\SelectBuilder;
use Espo\Entities\User;
use Espo\Core\Utils\Config;

class OnlyMy implements Filter
{
    public function __construct(private User $user) {}

    public function apply(SelectBuilder $queryBuilder, OrGroupBuilder $orGroupBuilder): void
    {
        $queryBuilder->where([
            'assignedUserId' => $this->user->getId()
        ]);
    }
}

class HighValue implements Filter
{
    public function __construct(private Config $config) {}

    public function apply(SelectBuilder $queryBuilder, OrGroupBuilder $orGroupBuilder): void
    {
        $threshold = $this->config->get('highValueThreshold', 100000);

        $queryBuilder->where([
            'amount>=' => $threshold
        ]);
    }
}
```

## Text Filters (Full-Text Search)

### Defining Text Filter

In `metadata/selectDefs/{EntityType}.json`:

```json
{
    "textFilterClassName": "Espo\\Modules\\MyModule\\Classes\\Select\\Opportunity\\TextFilter"
}
```

### Implementing Text Filter

```php
<?php
namespace Espo\Modules\MyModule\Classes\Select\Opportunity;

use Espo\Core\Select\Text\Filter;
use Espo\ORM\Query\SelectBuilder;
use Espo\Core\Select\Text\FilterParams;

class TextFilter implements Filter
{
    public function apply(SelectBuilder $queryBuilder, FilterParams $params): void
    {
        $filter = $params->getFilter();

        if (!$filter) {
            return;
        }

        // Search in multiple fields
        $queryBuilder->where([
            'OR' => [
                ['name*' => "%{$filter}%"],
                ['description*' => "%{$filter}%"],
                ['accountName*' => "%{$filter}%"]
            ]
        ]);
    }
}
```

## Query Builder Extension

For more complex queries, get the QueryBuilder to continue building:

```php
public function getComplexQuery(): iterable
{
    $queryBuilder = $this->selectBuilderFactory
        ->create()
        ->from('Opportunity')
        ->withStrictAccessControl()
        ->buildQueryBuilder();  // Returns QueryBuilder, not Query

    // Add custom joins
    $queryBuilder
        ->join('account')
        ->leftJoin('assignedUser')
        ->where([
            'account.type' => 'Customer',
            'stage' => ['Proposal', 'Negotiation']
        ])
        ->order('amount', 'DESC')
        ->limit(0, 100);

    $query = $queryBuilder->build();

    return $this->entityManager
        ->getRDBRepository('Opportunity')
        ->clone($query)
        ->find();
}
```

## Fetching SearchParams from Request

In API actions, use SearchParamsFetcher:

```php
<?php
namespace Espo\Modules\MyModule\Api;

use Espo\Core\Api\Action;
use Espo\Core\Api\Request;
use Espo\Core\Api\Response;
use Espo\Core\Api\ResponseComposer;
use Espo\Core\Select\SearchParams;
use Espo\Core\Record\SearchParamsFetcher;
use Espo\Core\Select\SelectBuilderFactory;
use Espo\ORM\EntityManager;

class SearchOpportunities implements Action
{
    public function __construct(
        private SearchParamsFetcher $searchParamsFetcher,
        private SelectBuilderFactory $selectBuilderFactory,
        private EntityManager $entityManager
    ) {}

    public function process(Request $request): Response
    {
        // Fetch search params from request query string
        $searchParams = $this->searchParamsFetcher->fetch($request);

        $query = $this->selectBuilderFactory
            ->create()
            ->from('Opportunity')
            ->withSearchParams($searchParams)
            ->withStrictAccessControl()
            ->build();

        $collection = $this->entityManager
            ->getRDBRepository('Opportunity')
            ->clone($query)
            ->find();

        $total = $this->entityManager
            ->getRDBRepository('Opportunity')
            ->clone($query)
            ->count();

        $list = [];
        foreach ($collection as $entity) {
            $list[] = $entity->getValueMap();
        }

        return ResponseComposer::json([
            'total' => $total,
            'list' => $list
        ]);
    }
}
```

## User-Specific Queries

Apply access control for a specific user (not current user):

```php
public function getAccountsForUser(string $userId): iterable
{
    $user = $this->entityManager->getEntityById('User', $userId);

    $query = $this->selectBuilderFactory
        ->create()
        ->from('Account')
        ->forUser($user)  // Apply this user's ACL
        ->withStrictAccessControl()
        ->build();

    return $this->entityManager
        ->getRDBRepository('Account')
        ->clone($query)
        ->find();
}
```

## Aggregation Queries

```php
public function getOpportunityStats(string $accountId): array
{
    $queryBuilder = $this->entityManager->getQueryBuilder();

    // Total amount by stage
    $query = $queryBuilder
        ->select()
        ->from('Opportunity')
        ->select([
            'stage',
            ['SUM:amount', 'totalAmount'],
            ['COUNT:id', 'count']
        ])
        ->where([
            'accountId' => $accountId,
            'deleted' => false
        ])
        ->group('stage')
        ->build();

    $sth = $this->entityManager->getQueryExecutor()->execute($query);

    $results = [];
    while ($row = $sth->fetch()) {
        $results[$row['stage']] = [
            'total' => (float) $row['totalAmount'],
            'count' => (int) $row['count']
        ];
    }

    return $results;
}
```

## Subqueries

```php
public function getAccountsWithOpenOpportunities(): iterable
{
    $subQuery = $this->entityManager->getQueryBuilder()
        ->select()
        ->from('Opportunity')
        ->select('accountId')
        ->where([
            'stage!=' => ['Closed Won', 'Closed Lost'],
            'deleted' => false
        ])
        ->build();

    return $this->entityManager
        ->getRDBRepository('Account')
        ->where([
            'id=s' => $subQuery  // 's' suffix for subquery
        ])
        ->find();
}
```

## Best Practices

### DO:
- Always use `withStrictAccessControl()` for user-facing queries
- Use SearchParams for API requests from frontend
- Create reusable Primary/Boolean filters for common queries
- Use `forUser()` when querying on behalf of another user
- Use aggregation queries for reports instead of loading all entities

### DON'T:
- Skip access control (`withStrictAccessControl()`) unless intentional
- Build raw SQL - use QueryBuilder
- Load all entities into memory for large datasets (use STH collections)
- Hardcode filter logic - use metadata-configured filters

## Resources

- [EspoCRM Select Builder Documentation](https://docs.espocrm.com/development/select-builder/)
- [ORM QueryBuilder Documentation](https://docs.espocrm.com/development/orm/)
