# Test Sites for Playwright BDD i18n Testing

## Overview

This document lists free, publicly accessible websites you can use for practicing Playwright BDD testing with i18n support.

---

## 🌟 Recommended Test Sites

### 1. TodoMVC (Best for Learning)
**URL:** https://demo.playwright.dev/todomvc/

**Features:**
- ✅ Simple, stable interface
- ✅ No login required
- ✅ Perfect for learning basic interactions
- ✅ Maintained by Playwright team

**What you can test:**
- Add, edit, delete todos
- Mark items as complete
- Filter todos (All, Active, Completed)
- Clear completed items

**Example in .env:**
```bash
BASE_URL=https://demo.playwright.dev/todomvc/
```

---

### 2. Playwright Demo API (For API + UI Testing)
**URL:** https://demo.playwright.dev/api-mocking/

**Features:**
- ✅ Demonstrates API mocking
- ✅ Shows network interception
- ✅ Good for advanced scenarios

---

### 3. The Internet (Herokuapp)
**URL:** https://the-internet.herokuapp.com/

**Features:**
- ✅ Multiple test scenarios in one place
- ✅ Login authentication (/login)
- ✅ Dynamic content (/dynamic_content)
- ✅ Dropdowns, hovers, frames
- ✅ File upload/download

**Useful Pages:**
- Login: https://the-internet.herokuapp.com/login
  - Username: `tomsmith`
  - Password: `SuperSecretPassword!`
- Dropdown: https://the-internet.herokuapp.com/dropdown
- Hovers: https://the-internet.herokuapp.com/hovers
- Dynamic Content: https://the-internet.herokuapp.com/dynamic_content

**Example in .env:**
```bash
BASE_URL=https://the-internet.herokuapp.com
```

---

### 4. Sauce Demo (E-commerce)
**URL:** https://www.saucedemo.com/

**Features:**
- ✅ Full e-commerce flow
- ✅ Multiple user accounts
- ✅ Shopping cart, checkout
- ✅ Great for realistic scenarios

**Test Accounts:**
- Standard user: `standard_user` / `secret_sauce`
- Locked user: `locked_out_user` / `secret_sauce`
- Problem user: `problem_user` / `secret_sauce`
- Performance glitch: `performance_glitch_user` / `secret_sauce`

**Example in .env:**
```bash
BASE_URL=https://www.saucedemo.com
```

---

### 5. OrangeHRM Demo
**URL:** https://opensource-demo.orangehrmlive.com/

**Features:**
- ✅ HR management system
- ✅ Complex forms and tables
- ✅ Multiple user roles
- ✅ Real-world application

**Credentials:**
- Username: `Admin`
- Password: `admin123`

**Example in .env:**
```bash
BASE_URL=https://opensource-demo.orangehrmlive.com
```

---

### 6. Demoblaze (E-commerce with Categories)
**URL:** https://www.demoblaze.com/

**Features:**
- ✅ Product categories
- ✅ Shopping cart
- ✅ User registration/login
- ✅ Modal dialogs

**Example in .env:**
```bash
BASE_URL=https://www.demoblaze.com
```

---

### 7. Automation Practice (Comprehensive)
**URL:** http://automationpractice.com/

**Features:**
- ✅ Full e-commerce site
- ✅ User registration
- ✅ Search functionality
- ✅ Complex forms

**Example in .env:**
```bash
BASE_URL=http://automationpractice.com
```

---

### 8. UI Testing Playground
**URL:** http://uitestingplayground.com/

**Features:**
- ✅ Specific testing challenges
- ✅ Dynamic content
- ✅ AJAX requests
- ✅ Hidden elements
- ✅ Visibility scenarios

**Useful Pages:**
- Dynamic ID: /dynamicid
- Class Attribute: /classattr
- Hidden Layers: /overlapped
- AJAX Data: /ajax
- Client Side Delay: /clientdelay

**Example in .env:**
```bash
BASE_URL=http://uitestingplayground.com
```

---

## 🌍 Sites with i18n Support

### 1. Wikipedia
**URL:** https://www.wikipedia.org/

**Features:**
- ✅ Available in 300+ languages
- ✅ Stable interface
- ✅ Good for i18n testing

**Language URLs:**
- English: https://en.wikipedia.org/
- Spanish: https://es.wikipedia.org/
- French: https://fr.wikipedia.org/
- German: https://de.wikipedia.org/
- Japanese: https://ja.wikipedia.org/
- Arabic: https://ar.wikipedia.org/

---

### 2. Mozilla MDN Web Docs
**URL:** https://developer.mozilla.org/

**Features:**
- ✅ Multiple language support
- ✅ Stable technical documentation
- ✅ Good for RTL testing

**Languages:**
- English: /en-US/
- Spanish: /es/
- French: /fr/
- Japanese: /ja/

---

## 📝 Configuration Examples

### Example 1: TodoMVC (Recommended for Beginners)

**.env:**
```bash
BASE_URL=https://demo.playwright.dev/todomvc/
BROWSER=chromium
HEADLESS=false
TIMEOUT=30000
DEFAULT_LOCALE=en-US
SCREENSHOT_ON_FAILURE=true
```

### Example 2: The Internet (Multiple Scenarios)

**.env:**
```bash
BASE_URL=https://the-internet.herokuapp.com
BROWSER=chromium
HEADLESS=false
TIMEOUT=30000
DEFAULT_LOCALE=en-US
SCREENSHOT_ON_FAILURE=true
```

### Example 3: SauceDemo (E-commerce)

**.env:**
```bash
BASE_URL=https://www.saucedemo.com
BROWSER=chromium
HEADLESS=false
TIMEOUT=30000
DEFAULT_LOCALE=en-US
SCREENSHOT_ON_FAILURE=true
TEST_USERNAME=standard_user
TEST_PASSWORD=secret_sauce
```

---

## 🎯 Quick Start with TodoMVC

### Step 1: Update .env
```bash
BASE_URL=https://demo.playwright.dev/todomvc/
```

### Step 2: Create a Simple Test

**features/todo.feature:**
```gherkin
Feature: Todo Management
  
  @smoke
  Scenario: Add a new todo item
    Given I am on the todo page
    When I add a new todo "Buy groceries"
    Then I should see "Buy groceries" in the list
```

**features/steps/todo_steps.py:**
```python
from behave import given, when, then
from playwright.sync_api import expect

@given('I am on the todo page')
def step_open_todo(context):
    context.page.goto("https://demo.playwright.dev/todomvc/")

@when('I add a new todo "{todo_text}"')
def step_add_todo(context, todo_text):
    input_box = context.page.locator(".new-todo")
    input_box.fill(todo_text)
    input_box.press("Enter")

@then('I should see "{text}" in the list')
def step_verify_todo(context, text):
    todos = context.page.locator(".todo-list li")
    expect(todos).to_contain_text(text)
```

### Step 3: Run the Test
```bash
behave features/todo.feature
```

---

## 🛠️ Creating Your Own Test Site

If you want to test with your own application:

### Option 1: Local Development Server
```bash
# Your app running locally
BASE_URL=http://localhost:3000
```

### Option 2: Staging Environment
```bash
# Your staging server
BASE_URL=https://staging.yourapp.com
```

### Option 3: Mock Server
```bash
# Using tools like json-server or WireMock
BASE_URL=http://localhost:3001
```

---

## ⚠️ Important Notes

### Sites to Avoid

❌ **Production sites without permission**
- Never run automated tests against live production sites
- Can cause issues or get your IP blocked

❌ **Sites with rate limiting**
- May block automated requests
- Can lead to failed tests

❌ **Sites with CAPTCHAs**
- Automated tests will fail
- Requires special handling

### Best Practices

✅ **Use demo/test environments**
- Specifically designed for testing
- No real data impact

✅ **Respect robots.txt**
- Check site's crawling policy
- Follow rate limits

✅ **Use stable sites**
- Avoid sites that change frequently
- Prefer maintained test sites

---

## 🔄 Switching Between Sites

You can easily switch test sites by:

### Method 1: Environment Variable
```bash
BASE_URL=https://demo.playwright.dev/todomvc/ behave
```

### Method 2: Update .env File
```bash
# Edit .env
BASE_URL=https://www.saucedemo.com
```

### Method 3: Multiple .env Files
```bash
# .env.todomvc
BASE_URL=https://demo.playwright.dev/todomvc/

# .env.saucedemo
BASE_URL=https://www.saucedemo.com

# Use specific env
cp .env.todomvc .env
behave
```

---

## 📚 Additional Resources

- **Playwright Demo Sites:** https://demo.playwright.dev/
- **Test Automation Practice Sites:** https://github.com/atinfo/awesome-test-automation
- **UI Testing Sites List:** https://github.com/BMayhew/awesome-sites-to-test-on

---

## 🎓 Recommended Learning Path

1. **Start with TodoMVC** - Learn basic interactions
2. **Move to The Internet** - Practice different elements
3. **Try SauceDemo** - Test complete user flows
4. **Explore UI Testing Playground** - Handle edge cases
5. **Test Your Own App** - Apply to real projects

---

**Created by LEARNLYTICA - Zero-Risk Workforce Transformation**
