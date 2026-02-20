# Internationalization Testing Guide

## Overview

This guide covers best practices for testing internationalized applications.

## Translation Files

### Structure

```
locales/
├── en-US/
│   └── common.json
├── es-ES/
│   └── common.json
└── ...
```

### JSON Format

```json
{
  "key": "value",
  "nested": {
    "key": "value"
  },
  "with_variable": "Hello, {{name}}"
}
```

## Testing Strategies

### 1. Key Consistency

Validate all locales have same keys:

```bash
python utils/translation_validator.py
```

### 2. Text Display

Test translated text appears correctly:

```gherkin
Scenario: Spanish navigation
  Given locale is "es-ES"
  When I visit homepage
  Then I should see "Inicio"
  And I should see "Productos"
```

### 3. Text Length

Test longer translations don't break layout:

```gherkin
Scenario: German long text
  Given locale is "de-DE"
  And viewport is 375x667
  Then text does not overflow containers
```

### 4. RTL Languages

Test right-to-left languages:

```gherkin
Scenario: Arabic RTL
  Given locale is "ar-SA"
  Then text direction should be "rtl"
  And navigation is right-aligned
```

### 5. Date Formats

Test locale-specific date formats:

```python
@then('date format matches locale')
def verify_date_format(context):
    formats = {
        'en-US': 'MM/DD/YYYY',
        'es-ES': 'DD/MM/YYYY',
        'de-DE': 'DD.MM.YYYY',
        'ja-JP': 'YYYY/MM/DD'
    }
    expected = formats[context.current_locale]
    # Verify format
```

### 6. Number Formats

Test number formatting:

```python
# US: 1,234.56
# EU: 1.234,56
# FR: 1 234,56
```

### 7. Currency

Test currency display:

```gherkin
Scenario Outline: Currency display
  Given locale is "<locale>"
  Then currency symbol is "<symbol>"
  
  Examples:
    | locale | symbol |
    | en-US  | $      |
    | es-ES  | €      |
    | ja-JP  | ¥      |
```

## Common Issues

### 1. Missing Translations

**Problem:** Key exists in en-US but not in es-ES

**Solution:** Run validator before tests

### 2. Text Overflow

**Problem:** German text is 30% longer

**Solution:** Test on small viewports

### 3. RTL Layout Breaks

**Problem:** Icons and text misaligned

**Solution:** Test RTL-specific CSS

### 4. Placeholder Variables

**Problem:** {{name}} shown instead of value

**Solution:** Test variable substitution

## Best Practices

1. ✅ Test all supported locales
2. ✅ Validate keys before running tests
3. ✅ Test on multiple viewports
4. ✅ Check both LTR and RTL
5. ✅ Verify date/number formats
6. ✅ Test character sets (CJK, Arabic)
7. ✅ Check pluralization rules
8. ✅ Verify sorting/collation

## Pluralization

Different languages have different plural forms:

- **English:** 2 forms (1 item, 2 items)
- **Arabic:** 6 forms
- **Russian:** 3 forms
- **Japanese:** 1 form (no plurals)

Test with:
```gherkin
Scenario: Plural forms
  Given locale is "ar-SA"
  Then "0 items" shows "لا توجد عناصر"
  And "1 item" shows "عنصر 1"
  And "2 items" shows "عنصران"
```

## Timezone Testing

```python
@given('timezone is "{tz}"')
def set_timezone(context, tz):
    context.browser_context = context.browser.new_context(
        timezone_id=tz
    )
```

Test timezones:
- America/New_York
- Europe/London
- Asia/Tokyo
- Australia/Sydney

## Performance

Monitor translation loading time:

```python
@then('translations load in under {ms:d}ms')
def check_load_time(context, ms):
    # Measure translation fetch time
    pass
```

## CI/CD Integration

Test all locales in parallel:

```yaml
strategy:
  matrix:
    locale: [en-US, es-ES, fr-FR, de-DE, ja-JP, ar-SA]
    browser: [chromium, firefox, webkit]
```

This creates 18 parallel jobs (6 locales × 3 browsers).
