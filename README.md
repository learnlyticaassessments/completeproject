# Playwright BDD i18n Complete Solution

Complete testing framework for Playwright with BDD (Behave) and comprehensive i18n support.

## 🚀 Quick Start (5 Minutes)

### 1. Extract and Navigate
```bash
unzip playwright-bdd-i18n-solution.zip
cd playwright-bdd-i18n-complete
```

### 2. Setup Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
playwright install
```

### 3. Configure Test Site
```bash
# Use TodoMVC (recommended for learning)
cp .env.todomvc .env

# OR use other pre-configured sites:
# cp .env.saucedemo .env
# cp .env.theinternet .env
```

### 4. Run Your First Test
```bash
behave features/todomvc.feature --tags=@smoke
```

---

## 🌐 Available Test Sites

The project comes with pre-configured environments for multiple test sites:

### 1. TodoMVC (Recommended for Beginners)
```bash
cp .env.todomvc .env
behave features/todomvc.feature
```
**Best for:** Learning basic Playwright interactions

### 2. SauceDemo (E-commerce)
```bash
cp .env.saucedemo .env
behave features/login.feature
```
**Best for:** Testing complete user flows

### 3. The Internet (Multiple Scenarios)
```bash
cp .env.theinternet .env
behave features/login.feature
```
**Best for:** Practicing different test scenarios

📖 **See `docs/TEST_SITES.md` for complete list of available test sites**

---

## 📁 Project Structure

```
playwright-bdd-i18n-complete/
├── features/              # Test scenarios
│   ├── todomvc.feature   # TodoMVC tests (ready to run!)
│   ├── login.feature     # Login tests
│   ├── i18n_*.feature    # i18n tests
│   ├── steps/            # Step definitions
│   ├── pages/            # Page objects
│   └── environment.py    # Setup/teardown
├── locales/              # Translation files (6 languages)
│   ├── en-US/
│   ├── es-ES/
│   ├── fr-FR/
│   ├── de-DE/
│   ├── ja-JP/
│   └── ar-SA/
├── utils/                # Helper scripts
├── docs/                 # Documentation
│   ├── TESTING_GUIDE.md
│   ├── I18N_GUIDE.md
│   └── TEST_SITES.md    # ⭐ Test sites guide
├── .env.example          # Template
├── .env.todomvc          # TodoMVC config
├── .env.saucedemo        # SauceDemo config
└── .env.theinternet      # The Internet config
```

---

## 🎯 Running Tests

### Run All Tests
```bash
behave
```

### Run Specific Feature
```bash
behave features/todomvc.feature
behave features/login.feature
behave features/i18n_login.feature
```

### Run with Tags
```bash
# Smoke tests only
behave --tags=@smoke

# TodoMVC tests only
behave --tags=@todomvc

# i18n tests only
behave --tags=@i18n

# Login tests only
behave --tags=@login
```

### Run with Different Locales
```bash
LOCALE=es-ES behave --tags=@i18n
LOCALE=ja-JP behave --tags=@i18n
LOCALE=ar-SA behave --tags=@i18n
```

### Run with Different Browsers
```bash
BROWSER=firefox behave
BROWSER=webkit behave
```

### Run in Parallel
```bash
behave --parallel 2
```

### Generate HTML Report
```bash
behave -f html -o reports/report.html
```

---

## 🌍 Supported Locales

- 🇺🇸 **en-US** - English (United States)
- 🇪🇸 **es-ES** - Spanish (Spain)
- 🇫🇷 **fr-FR** - French (France)
- 🇩🇪 **de-DE** - German (Germany)
- 🇯🇵 **ja-JP** - Japanese (Japan)
- 🇸🇦 **ar-SA** - Arabic (Saudi Arabia) - RTL support

---

## 🔧 Configuration

### Environment Variables (.env)

```bash
# Application URL
BASE_URL=https://demo.playwright.dev/todomvc/

# Browser (chromium, firefox, webkit)
BROWSER=chromium

# Headless mode
HEADLESS=false

# Default locale
DEFAULT_LOCALE=en-US

# Test credentials (if needed)
TEST_USERNAME=
TEST_PASSWORD=
```

---

## 📊 Testing Patterns

### Basic Test
```gherkin
Scenario: Add a todo
  Given I am on the TodoMVC page
  When I add a new todo "Buy milk"
  Then I should see "Buy milk" in the todo list
```

### Data-Driven Test
```gherkin
Scenario Outline: Login with different users
  Given I am on the login page
  When I login as "<user>"
  Then I see "<message>"
  
  Examples:
    | user     | message   |
    | admin    | Dashboard |
    | guest    | Limited   |
```

### i18n Test
```gherkin
Scenario Outline: Multi-language UI
  Given locale is "<locale>"
  When I visit homepage
  Then I see "<welcome>" message
  
  Examples:
    | locale | welcome    |
    | en-US  | Welcome    |
    | es-ES  | Bienvenido |
```

---

## 🛠️ Utilities

### Validate Translation Keys
```bash
python utils/translation_validator.py
```

This checks:
- All locales have same keys
- No missing translations
- No extra keys

---

## 🐛 Debugging

### Interactive Debugging
```bash
PWDEBUG=1 behave features/todomvc.feature
```

### View Traces
```bash
playwright show-trace traces/scenario_name.zip
```

### Screenshots
Failed test screenshots automatically saved to `screenshots/`

---

## 📈 CI/CD

GitHub Actions workflow included for automated testing:
- Runs on push to main/develop
- Tests all 6 locales × 3 browsers = 18 parallel jobs
- Uploads screenshots, traces, and reports on failure

---

## 📚 Documentation

- **README.md** - This file (quick start)
- **QUICKSTART.md** - 5-minute setup guide
- **docs/TESTING_GUIDE.md** - Comprehensive testing guide
- **docs/I18N_GUIDE.md** - i18n testing best practices
- **docs/TEST_SITES.md** - ⭐ Available test sites guide

---

## 🎓 Learning Path

1. **Start with TodoMVC** (included!)
   ```bash
   cp .env.todomvc .env
   behave features/todomvc.feature --tags=@smoke
   ```

2. **Explore Different Sites**
   ```bash
   cp .env.saucedemo .env
   behave features/login.feature
   ```

3. **Try i18n Testing**
   ```bash
   LOCALE=es-ES behave features/i18n_login.feature
   ```

4. **Practice Debugging**
   ```bash
   PWDEBUG=1 behave features/todomvc.feature
   ```

---

## ❓ Common Issues

### "Command not found: behave"
**Solution:** Activate virtual environment
```bash
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### "Browser not found"
**Solution:** Install browsers
```bash
playwright install
```

### "Module not found"
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

1. Create feature branch
2. Add tests for new functionality
3. Ensure all tests pass
4. Submit pull request

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🎉 Credits

**Created by LEARNLYTICA**
*Zero-Risk Workforce Transformation*

For training and support:
- Website: learnlytica.com
- Documentation: This repository

---

## 🚀 Next Steps

1. ✅ Run your first test with TodoMVC
2. ✅ Read `docs/TEST_SITES.md` for more test sites
3. ✅ Check `docs/TESTING_GUIDE.md` for patterns
4. ✅ Review `docs/I18N_GUIDE.md` for i18n testing
5. ✅ Customize for your project

**Happy Testing!** 🎉
