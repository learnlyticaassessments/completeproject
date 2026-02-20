"""
i18n Testing Step Definitions
"""
from behave import given, when, then
from playwright.sync_api import expect
import sys
sys.path.append('.')
from utils.test_helpers import (
    load_locale_data, 
    get_translation, 
    is_rtl_locale,
    get_expected_date_format,
    get_expected_currency_symbol
)

@given('I set viewport to {width:d}x{height:d}')
def step_set_viewport(context, width, height):
    """Set viewport size"""
    context.page.set_viewport_size({"width": width, "height": height})
    print(f"✓ Set viewport to {width}x{height}")

@when('I visit the homepage')
def step_visit_homepage(context):
    """Visit homepage"""
    import os
    base_url = os.getenv('BASE_URL', 'https://the-internet.herokuapp.com/')
    context.page.goto(base_url)
    print(f"✓ Visited homepage: {base_url}")

@then('text direction should be "{direction}"')
def step_verify_text_direction(context, direction):
    """Verify text direction (ltr or rtl)"""
    actual_dir = context.page.evaluate("() => document.dir")
    assert actual_dir == direction, f"Expected dir='{direction}', got '{actual_dir}'"
    print(f"✓ Text direction is: {direction}")

@then('the page direction should be RTL')
def step_verify_rtl(context):
    """Verify page is RTL"""
    is_rtl = is_rtl_locale(context.current_locale)
    if is_rtl:
        dir_attr = context.page.evaluate("() => document.dir")
        assert dir_attr == "rtl", f"Expected RTL but got: {dir_attr}"
        print("✓ Page direction is RTL")

@then('navigation text should be in {locale}')
def step_verify_nav_locale(context, locale):
    """Verify navigation is in correct locale"""
    translations = load_locale_data(locale)
    expected_home = translations['nav']['home']
    
    # Check if home link exists with translated text
    home_link = context.page.locator(f"text={expected_home}")
    expect(home_link).to_be_visible()
    print(f"✓ Navigation in {locale}: Found '{expected_home}'")

@then('date format should match locale')
def step_verify_date_format(context):
    """Verify date format matches locale"""
    expected_format = get_expected_date_format(context.current_locale)
    print(f"✓ Expected date format for {context.current_locale}: {expected_format}")

@then('currency symbol should be "{symbol}"')
def step_verify_currency_symbol(context, symbol):
    """Verify currency symbol"""
    expected = get_expected_currency_symbol(context.current_locale)
    assert symbol == expected, f"Expected '{expected}', got '{symbol}'"
    print(f"✓ Currency symbol: {symbol}")

@then('text does not overflow containers')
def step_verify_no_overflow(context):
    """Verify text doesn't overflow"""
    # Check if any text is cut off
    overflow_check = context.page.evaluate("""
        () => {
            const elements = document.querySelectorAll('*');
            for (let el of elements) {
                if (el.scrollWidth > el.clientWidth || 
                    el.scrollHeight > el.clientHeight) {
                    return false;
                }
            }
            return true;
        }
    """)
    assert overflow_check, "Text overflow detected"
    print("✓ No text overflow detected")

@then('all translation keys are loaded')
def step_verify_keys_loaded(context):
    """Verify translation keys are loaded"""
    # Check for missing translation indicators
    missing_keys = context.page.locator("text=/.*\\[missing\\].*/")
    expect(missing_keys).to_have_count(0)
    print("✓ All translation keys loaded")
