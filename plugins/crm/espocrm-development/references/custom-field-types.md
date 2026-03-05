# Custom Field Types Reference

## Overview

EspoCRM allows creating custom field types that extend the built-in types (varchar, text, enum, etc.). A custom field type requires:

1. **Field Metadata** - Backend configuration
2. **Frontend View** - JavaScript view for rendering/editing
3. **Templates** - Handlebars templates for different modes
4. **Translations** - Labels for Entity Manager

## Field Type Metadata

Create `Resources/metadata/fields/{fieldType}.json`:

```json
{
    "view": "custom:views/fields/my-field",
    "params": [
        {
            "name": "maxLength",
            "type": "int"
        },
        {
            "name": "options",
            "type": "array"
        },
        {
            "name": "required",
            "type": "bool"
        }
    ],
    "filter": true,
    "textFilter": true,
    "textFilterForeign": false,
    "personalData": true,
    "actualFields": ["value"],
    "notActualFields": [],
    "fieldDefs": {
        "type": "varchar",
        "maxLength": 255
    },
    "converterClassName": "Espo\\Modules\\MyModule\\Classes\\FieldConverters\\MyField"
}
```

### Metadata Properties

| Property | Description |
|----------|-------------|
| `view` | Frontend view class path |
| `params` | Configurable parameters in Entity Manager |
| `filter` | Enable filtering in list views |
| `textFilter` | Include in text search |
| `personalData` | Mark as personal data (GDPR) |
| `actualFields` | Database column suffixes |
| `fieldDefs` | Default database column definition |
| `validatorClassName` | Backend validation class |
| `converterClassName` | Field value converter |

## Frontend View

Create `client/custom/src/views/fields/my-field.js`:

```javascript
define('custom:views/fields/my-field', ['views/fields/base'], function (BaseFieldView) {

    return BaseFieldView.extend({

        // Template for detail/list view
        detailTemplateContent: `
            <span class="my-field-value">{{value}}</span>
            {{#if formattedValue}}
                <span class="formatted">({{formattedValue}})</span>
            {{/if}}
        `,

        // Template for edit view
        editTemplateContent: `
            <input
                type="text"
                class="main-element form-control"
                name="{{name}}"
                value="{{value}}"
                autocomplete="off"
                maxlength="{{maxLength}}"
                {{#if required}}required{{/if}}
            >
            <div class="help-block hidden"></div>
        `,

        // Template for list view (optional, uses detailTemplateContent if not defined)
        listTemplateContent: `
            <span class="my-field-list-value">{{value}}</span>
        `,

        // Template for search filter
        searchTemplateContent: `
            <input
                type="text"
                class="form-control"
                name="{{name}}"
                value="{{searchValue}}"
                placeholder="{{translate 'Search'}}"
            >
        `,

        // Setup method - called before rendering
        setup: function () {
            BaseFieldView.prototype.setup.call(this);

            // Get field params from metadata
            this.maxLength = this.params.maxLength || 255;

            // Listen for model changes
            this.listenTo(this.model, 'change:' + this.name, function () {
                if (this.isRendered()) {
                    this.reRender();
                }
            }, this);
        },

        // Data passed to templates
        data: function () {
            var data = BaseFieldView.prototype.data.call(this);

            data.value = this.model.get(this.name);
            data.formattedValue = this.formatValue(data.value);
            data.maxLength = this.maxLength;
            data.required = this.params.required || false;

            return data;
        },

        // Called after DOM is ready
        afterRender: function () {
            BaseFieldView.prototype.afterRender.call(this);

            if (this.isEditMode()) {
                // Initialize any plugins
                this.$element = this.$el.find('.main-element');

                // Add input handlers
                this.$element.on('input', function () {
                    this.trigger('change');
                }.bind(this));
            }
        },

        // Get value from DOM (edit mode)
        fetch: function () {
            var data = {};
            data[this.name] = this.$element.val().trim();
            return data;
        },

        // Validate field value
        validateRequired: function () {
            if (this.isRequired()) {
                var value = this.model.get(this.name);
                if (!value || value === '') {
                    var msg = this.translate('fieldIsRequired', 'messages')
                        .replace('{field}', this.getLabelText());
                    this.showValidationMessage(msg);
                    return true;
                }
            }
            return false;
        },

        // Custom validation
        validateMaxLength: function () {
            var value = this.model.get(this.name);
            if (value && value.length > this.maxLength) {
                var msg = this.translate('fieldMaxLength', 'messages')
                    .replace('{field}', this.getLabelText())
                    .replace('{max}', this.maxLength);
                this.showValidationMessage(msg);
                return true;
            }
            return false;
        },

        // Format value for display
        formatValue: function (value) {
            if (!value) return '';
            // Custom formatting logic
            return value.toUpperCase();
        },

        // Parse value from input
        parseValue: function (value) {
            if (!value) return null;
            return value.trim().toLowerCase();
        },

        // Get value for export
        getValueForExport: function () {
            return this.model.get(this.name) || '';
        },

        // Search data for filter
        fetchSearch: function () {
            var value = this.$el.find('input[name="' + this.name + '"]').val();

            if (!value) {
                return false;
            }

            return {
                type: 'contains',
                value: value
            };
        }
    });
});
```

## Complete Example: Rating Field

### 1. Field Metadata

`Resources/metadata/fields/rating.json`:

```json
{
    "view": "custom:views/fields/rating",
    "params": [
        {
            "name": "maxValue",
            "type": "int",
            "default": 5
        },
        {
            "name": "allowHalf",
            "type": "bool",
            "default": false
        }
    ],
    "filter": true,
    "fieldDefs": {
        "type": "float",
        "default": null
    },
    "validatorClassName": "Espo\\Modules\\MyModule\\Classes\\FieldValidators\\Rating"
}
```

### 2. Frontend View

`client/custom/src/views/fields/rating.js`:

```javascript
define('custom:views/fields/rating', ['views/fields/base'], function (BaseFieldView) {

    return BaseFieldView.extend({

        detailTemplateContent: `
            <div class="rating-display">
                {{#each stars}}
                    <span class="star {{#if filled}}filled{{/if}}{{#if half}}half{{/if}}">
                        {{#if filled}}★{{else}}☆{{/if}}
                    </span>
                {{/each}}
                <span class="rating-value">({{value}}/{{maxValue}})</span>
            </div>
        `,

        editTemplateContent: `
            <div class="rating-input" data-max="{{maxValue}}">
                {{#each stars}}
                    <span
                        class="star clickable {{#if filled}}filled{{/if}}"
                        data-value="{{value}}"
                    >☆</span>
                {{/each}}
                <input type="hidden" name="{{name}}" value="{{value}}">
                <button type="button" class="btn btn-link btn-sm clear-rating">
                    {{translate 'Clear'}}
                </button>
            </div>
        `,

        events: {
            'click .star.clickable': function (e) {
                var value = $(e.currentTarget).data('value');
                this.setRating(value);
            },
            'click .clear-rating': function () {
                this.setRating(null);
            }
        },

        setup: function () {
            BaseFieldView.prototype.setup.call(this);

            this.maxValue = this.params.maxValue || 5;
            this.allowHalf = this.params.allowHalf || false;
        },

        data: function () {
            var data = BaseFieldView.prototype.data.call(this);
            var value = this.model.get(this.name);

            data.value = value;
            data.maxValue = this.maxValue;
            data.stars = this.buildStars(value);

            return data;
        },

        buildStars: function (value) {
            var stars = [];
            value = value || 0;

            for (var i = 1; i <= this.maxValue; i++) {
                stars.push({
                    value: i,
                    filled: i <= value,
                    half: this.allowHalf && i - 0.5 === value
                });
            }

            return stars;
        },

        setRating: function (value) {
            this.model.set(this.name, value);
            this.reRender();
        },

        fetch: function () {
            var data = {};
            data[this.name] = this.$el.find('input[name="' + this.name + '"]').val() || null;

            if (data[this.name]) {
                data[this.name] = parseFloat(data[this.name]);
            }

            return data;
        },

        validateRange: function () {
            var value = this.model.get(this.name);

            if (value !== null && (value < 0 || value > this.maxValue)) {
                this.showValidationMessage(
                    'Rating must be between 0 and ' + this.maxValue
                );
                return true;
            }

            return false;
        }
    });
});
```

### 3. Backend Validator

`Classes/FieldValidators/Rating.php`:

```php
<?php
namespace Espo\Modules\MyModule\Classes\FieldValidators;

use Espo\Core\FieldValidation\Validator;
use Espo\Core\FieldValidation\Validator\Data;
use Espo\ORM\Entity;

class Rating implements Validator
{
    public function validate(Entity $entity, string $field, Data $data): bool
    {
        $value = $entity->get($field);

        if ($value === null) {
            return true; // Allow null
        }

        $maxValue = $data->getParam('maxValue') ?? 5;

        if (!is_numeric($value)) {
            return false;
        }

        if ($value < 0 || $value > $maxValue) {
            return false;
        }

        return true;
    }
}
```

### 4. Translations

`Resources/i18n/en_US/Admin.json`:

```json
{
    "fieldTypes": {
        "rating": "Rating"
    },
    "fieldParams": {
        "rating": {
            "maxValue": "Maximum Value",
            "allowHalf": "Allow Half Stars"
        }
    }
}
```

### 5. CSS Styling

`client/custom/css/rating-field.css`:

```css
.rating-display .star {
    font-size: 1.2em;
    color: #ccc;
}

.rating-display .star.filled {
    color: #ffc107;
}

.rating-input .star {
    font-size: 1.5em;
    cursor: pointer;
    transition: color 0.2s;
}

.rating-input .star:hover {
    color: #ffc107;
}

.rating-input .star.filled {
    color: #ffc107;
}
```

## Complex Field: Address with Autocomplete

### Field Metadata

`Resources/metadata/fields/addressAutocomplete.json`:

```json
{
    "view": "custom:views/fields/address-autocomplete",
    "params": [
        {
            "name": "provider",
            "type": "enum",
            "options": ["google", "mapbox"]
        },
        {
            "name": "countries",
            "type": "array"
        }
    ],
    "actualFields": ["street", "city", "state", "country", "postalCode"],
    "fieldDefs": {
        "notStorable": true
    },
    "fields": {
        "street": {
            "type": "varchar",
            "maxLength": 255
        },
        "city": {
            "type": "varchar",
            "maxLength": 100
        },
        "state": {
            "type": "varchar",
            "maxLength": 100
        },
        "country": {
            "type": "varchar",
            "maxLength": 100
        },
        "postalCode": {
            "type": "varchar",
            "maxLength": 20
        }
    },
    "naming": "suffix"
}
```

### Frontend View

`client/custom/src/views/fields/address-autocomplete.js`:

```javascript
define('custom:views/fields/address-autocomplete', ['views/fields/address'], function (AddressFieldView) {

    return AddressFieldView.extend({

        editTemplateContent: `
            <div class="address-autocomplete">
                <input
                    type="text"
                    class="form-control autocomplete-input"
                    placeholder="{{translate 'Start typing address...'}}"
                    autocomplete="off"
                >
                <div class="autocomplete-results"></div>
            </div>
            <div class="address-fields" style="margin-top: 10px;">
                <input type="text" class="form-control" name="{{streetName}}" value="{{street}}" placeholder="{{translate 'Street'}}">
                <div class="row" style="margin-top: 5px;">
                    <div class="col-sm-6">
                        <input type="text" class="form-control" name="{{cityName}}" value="{{city}}" placeholder="{{translate 'City'}}">
                    </div>
                    <div class="col-sm-6">
                        <input type="text" class="form-control" name="{{stateName}}" value="{{state}}" placeholder="{{translate 'State'}}">
                    </div>
                </div>
                <div class="row" style="margin-top: 5px;">
                    <div class="col-sm-6">
                        <input type="text" class="form-control" name="{{countryName}}" value="{{country}}" placeholder="{{translate 'Country'}}">
                    </div>
                    <div class="col-sm-6">
                        <input type="text" class="form-control" name="{{postalCodeName}}" value="{{postalCode}}" placeholder="{{translate 'Postal Code'}}">
                    </div>
                </div>
            </div>
        `,

        afterRender: function () {
            AddressFieldView.prototype.afterRender.call(this);

            if (this.isEditMode()) {
                this.initAutocomplete();
            }
        },

        initAutocomplete: function () {
            var $input = this.$el.find('.autocomplete-input');
            var $results = this.$el.find('.autocomplete-results');

            $input.on('input', _.debounce(function () {
                var query = $input.val();

                if (query.length < 3) {
                    $results.hide();
                    return;
                }

                this.fetchAddressSuggestions(query).then(function (suggestions) {
                    this.renderSuggestions(suggestions);
                }.bind(this));
            }.bind(this), 300));
        },

        fetchAddressSuggestions: function (query) {
            return this.ajaxGetRequest('AddressAutocomplete', {
                query: query,
                provider: this.params.provider || 'google'
            });
        },

        renderSuggestions: function (suggestions) {
            var $results = this.$el.find('.autocomplete-results');
            $results.empty();

            suggestions.forEach(function (suggestion) {
                var $item = $('<div class="suggestion-item">')
                    .text(suggestion.formatted)
                    .data('address', suggestion);

                $item.on('click', function () {
                    this.selectAddress(suggestion);
                    $results.hide();
                }.bind(this));

                $results.append($item);
            }.bind(this));

            $results.show();
        },

        selectAddress: function (address) {
            this.$el.find('[name="' + this.streetName + '"]').val(address.street);
            this.$el.find('[name="' + this.cityName + '"]').val(address.city);
            this.$el.find('[name="' + this.stateName + '"]').val(address.state);
            this.$el.find('[name="' + this.countryName + '"]').val(address.country);
            this.$el.find('[name="' + this.postalCodeName + '"]').val(address.postalCode);

            this.$el.find('.autocomplete-input').val('');
        }
    });
});
```

## Using Custom Field Types

After creating the field type, use it in entity definitions:

```json
{
    "fields": {
        "customerRating": {
            "type": "rating",
            "maxValue": 5,
            "allowHalf": true
        },
        "businessAddress": {
            "type": "addressAutocomplete",
            "provider": "google"
        }
    }
}
```

## Best Practices

### DO:
- Extend appropriate base view (`views/fields/base`, `views/fields/varchar`, etc.)
- Implement all view modes (detail, edit, list, search)
- Add proper validation (frontend and backend)
- Support export/import functionality
- Clear cache after adding field types
- Add translations for Entity Manager

### DON'T:
- Skip validation
- Hardcode labels (use translations)
- Forget to handle null/empty values
- Skip the search template if field is filterable
- Modify core field types (extend instead)

## Resources

- [EspoCRM Custom Field Types](https://docs.espocrm.com/development/custom-field-type/)
- [Frontend Views Reference](https://docs.espocrm.com/development/view/)
- [Existing Field Types](https://github.com/espocrm/espocrm/tree/master/client/src/views/fields)
