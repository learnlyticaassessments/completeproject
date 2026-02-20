# Testing Guide

## Test Writing Guidelines

### Gherkin Best Practices

1. **Use Business Language**

   - ✅ Good: "When I log in as a customer"
   - ❌ Bad: "When I click #loginButton"
2. **One Scenario = One Test Case**

   - Each scenario should test one specific thing
   - Don't combine multiple unrelated checks
3. **Keep Scenarios Independent (important)**

   - Tests should not depend on each other
   - Each test should set up its own data
4. **Use Background for Common Steps**

   ```gherkin
   Background:
     Given I am logged in

   Scenario: View profile
     When I click profile
     Then I see my information
   ```

### Step Definition Patterns

1. **Reusable Steps**

   ```python
   @when('I click "{button_text}"')
   def step_click_button(context, button_text):
       context.page.click(f"text={button_text}")
   ```
2. **Parameterized Steps**

   ```python
   @given('viewport is {width:d}x{height:d}')
   def step_set_viewport(context, width, height):
       context.page.set_viewport_size({"width": width, "height": height})
   ```
3. **Data Tables**

   ```gherkin
   When I fill the form:
     | Field    | Value      |
     | Name     | John Doe   |
     | Email    | john@ex.com|
   ```

## i18n Testing

### Testing Different Locales

1. **Set locale in scenario**

   ```gherkin
   Given locale is "es-ES"
   ```
2. **Use Scenario Outline for multiple locales**

   ```gherkin
   Scenario Outline: Test in <locale>
     Given locale is "<locale>"
     Then I should see "<text>"

     Examples:
       | locale | text      |
       | en-US  | Welcome   |
       | es-ES  | Bienvenido|
   ```

### Testing RTL Languages

```gherkin
Scenario: Arabic RTL layout
  Given locale is "ar-SA"
  When I visit homepage
  Then text direction should be "rtl"
  And navigation is right-aligned
```

### Testing Responsive i18n

```gherkin
Scenario Outline: Responsive text
  Given locale is "<locale>"
  And viewport is <width>x<height>
  Then text does not overflow
  
  Examples:
    | locale | width | height |
    | de-DE  | 375   | 667    |
    | ja-JP  | 375   | 667    |
```

## Debugging Tests

### Using PWDEBUG

```bash
PWDEBUG=1 behave features/login.feature
```

Features:

- Step through tests
- Inspect elements
- Try selectors
- Pause/resume

### Viewing Traces

```bash
playwright show-trace traces/failed_test.zip
```

Shows:

- Timeline of actions
- Screenshots
- Network activity
- Console logs

### Screenshots

Automatically taken on failure in `screenshots/` directory.

## Common Patterns

### Waiting for Elements

```python
# Wait for selector
context.page.wait_for_selector("#element")

# Wait for load state
context.page.wait_for_load_state("networkidle")

# Use expect (auto-waits)
expect(context.page.locator("#element")).to_be_visible()
```

### Handling Dynamic Content

```python
# Wait for specific text
expect(context.page.locator("text=Success")).to_be_visible()

# Wait for URL
expect(context.page).to_have_url("**/dashboard")
```

### Testing Forms

```gherkin
Scenario: Submit form
  When I fill "name" with "John"
  And I fill "email" with "john@test.com"
  And I click "Submit"
  Then I should see "Success"
```

## Performance Testing

### Measuring Load Time

```python
@then('page loads in under {ms:d}ms')
def check_load_time(context, ms):
    metrics = context.page.evaluate("""
        () => {
            const p = performance.getEntriesByType('navigation')[0];
            return p.loadEventEnd - p.fetchStart;
        }
    """)
    assert metrics < ms
```

## Running Tests

### Local Development

```bash
# All tests
behave

# Specific feature
behave features/login.feature

# Specific scenario
behave -n "Successful login"

# With tags
behave --tags=@smoke
behave --tags="@i18n and not @slow"
```

### CI/CD

```bash
# Headless
HEADLESS=true behave

# With specific locale
LOCALE=es-ES behave --tags=@i18n

# Parallel execution
behave --parallel 4
```

## Troubleshooting

### Element Not Found

1. Check selector is correct
2. Wait for element to appear
3. Use Playwright Inspector
4. Check if in iframe

### Timing Issues

1. Use `expect()` (auto-waits)
2. Avoid `time.sleep()`
3. Wait for load states
4. Check network activity

### Translation Missing

1. Run validation script
2. Check locale file exists
3. Verify key names match
4. Check fallback locale
