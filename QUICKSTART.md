# 🚀 Quick Start Guide

## Installation (5 minutes)

### Step 1: Extract Files
```bash
unzip playwright-bdd-i18n-solution.zip
cd playwright-bdd-i18n-complete
```

### Step 2: Setup Python Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Step 4: Copy Environment File
```bash
cp .env.example .env
```

## Running Your First Test

### Run All Tests
```bash
behave
```

### Run Specific Tests
```bash
# Login tests only
behave --tags=@login

# i18n tests only
behave --tags=@i18n

# Smoke tests only
behave --tags=@smoke
```

### Run with Different Locales
```bash
# Spanish
LOCALE=es-ES behave --tags=@i18n

# Arabic (RTL)
LOCALE=ar-SA behave --tags=@i18n

# Japanese
LOCALE=ja-JP behave --tags=@i18n
```

### Run with Different Browsers
```bash
# Firefox
BROWSER=firefox behave

# Safari (WebKit)
BROWSER=webkit behave
```

## Viewing Results

### Screenshots
Failed test screenshots are saved in:
```
screenshots/
```

### Traces
Detailed execution traces in:
```
traces/
```

View traces with:
```bash
playwright show-trace traces/your_test.zip
```

### HTML Reports
Generate HTML report:
```bash
behave -f html -o reports/report.html
```

Open `reports/report.html` in your browser.

## Project Structure

```
📁 playwright-bdd-i18n-complete/
├── 📁 features/           # Test files
│   ├── login.feature      # Login tests
│   ├── i18n_login.feature # Multi-language login
│   ├── 📁 steps/          # Step definitions (Python)
│   ├── 📁 pages/          # Page objects
│   └── environment.py     # Setup/teardown
├── 📁 locales/            # Translation files
│   ├── en-US/
│   ├── es-ES/
│   ├── fr-FR/
│   ├── de-DE/
│   ├── ja-JP/
│   └── ar-SA/
├── 📁 utils/              # Helper scripts
│   ├── translation_validator.py
│   └── test_helpers.py
├── 📁 docs/               # Documentation
└── requirements.txt       # Python dependencies
```

## Common Commands

```bash
# Run all tests
behave

# Run with verbose output
behave -v

# Run specific feature
behave features/login.feature

# Run specific scenario
behave -n "Successful login"

# Run in parallel
behave --parallel 2

# Generate HTML report
behave -f html -o reports/report.html

# Validate translations
python utils/translation_validator.py

# Debug mode (step through)
PWDEBUG=1 behave features/login.feature
```

## Next Steps

1. ✅ Read `README.md` for detailed documentation
2. ✅ Check `docs/TESTING_GUIDE.md` for testing patterns
3. ✅ Review `docs/I18N_GUIDE.md` for i18n best practices
4. ✅ Explore feature files in `features/`
5. ✅ Customize `.env` for your environment

## Troubleshooting

### "Command not found: behave"
Make sure virtual environment is activated:
```bash
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### "Browser not found"
Install Playwright browsers:
```bash
playwright install
```

### "Translation validation failed"
Check that all locale files have matching keys:
```bash
python utils/translation_validator.py
```

## Need Help?

- 📚 Read the full documentation in `README.md`
- 🐛 Check `docs/TESTING_GUIDE.md` for debugging
- 🌍 See `docs/I18N_GUIDE.md` for i18n testing

## Example Test Run

```bash
$ behave --tags=@smoke

Feature: User Login

  Scenario: Successful login with valid credentials
    Given I am on the login page               ✓ passed
    When I enter username "test@example.com"   ✓ passed
    And I enter password "Test@123"            ✓ passed
    And I click the login button               ✓ passed
    Then I should see the dashboard            ✓ passed

1 feature passed, 0 failed
1 scenario passed, 0 failed
5 steps passed, 0 failed
```

Happy Testing! 🎉
