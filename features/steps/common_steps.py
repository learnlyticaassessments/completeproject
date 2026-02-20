"""
Common Step Definitions
Reusable steps across features
"""
from behave import given, when, then
from playwright.sync_api import expect
import os

@given('I am on the "{page_name}" page')
def step_navigate_to_page(context, page_name):
    """Navigate to a specific page"""
    base_url = os.getenv('BASE_URL', 'http://localhost:3000')
    page_map = {
        'login': '/login',
        'home': '/',
        'products': '/products',
        'cart': '/cart'
    }
    
    url = f"{base_url}{page_map.get(page_name.lower(), '/')}"
    context.page.goto(url)
    print(f"✓ Navigated to {page_name} page: {url}")

@given('locale is "{locale}"')
def step_set_locale(context, locale):
    """Set locale for the test"""
    # Close existing context and page
    context.page.close()
    context.browser_context.close()
    
    # Create new context with specified locale
    context.browser_context = context.browser.new_context(
        locale=locale,
        timezone_id=os.getenv('TIMEZONE', 'America/New_York')
    )
    context.page = context.browser_context.new_page()
    context.current_locale = locale
    print(f"✓ Set locale to: {locale}")

@when('I wait for {seconds:d} seconds')
def step_wait_seconds(context, seconds):
    """Wait for specified seconds"""
    context.page.wait_for_timeout(seconds * 1000)

@then('I should see "{text}"')
def step_verify_text(context, text):
    """Verify text is visible on page"""
    expect(context.page.locator(f"text={text}")).to_be_visible()
    print(f"✓ Found text: {text}")

@then('I should not see "{text}"')
def step_verify_text_not_visible(context, text):
    """Verify text is not visible"""
    expect(context.page.locator(f"text={text}")).to_be_hidden()
    print(f"✓ Text not visible: {text}")

@then('the page title should be "{title}"')
def step_verify_title(context, title):
    """Verify page title"""
    expect(context.page).to_have_title(title)
    print(f"✓ Page title is: {title}")

@then('the URL should contain "{url_part}"')
def step_verify_url_contains(context, url_part):
    """Verify URL contains text"""
    expect(context.page).to_have_url(f"**{url_part}**")
    print(f"✓ URL contains: {url_part}")
