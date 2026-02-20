"""
Login Step Definitions
"""
from behave import given, when, then
from playwright.sync_api import expect
from features.pages.login_page import LoginPage

@given('I am on the login page')
def step_navigate_to_login(context):
    """Navigate to login page"""
    context.login_page = LoginPage(context.page)
    context.login_page.navigate_to_login()
    print("✓ Navigated to login page")

@when('I enter username "{username}"')
def step_enter_username(context, username):
    """Enter username"""
    context.login_page.enter_username(username)
    print(f"✓ Entered username: {username}")

@when('I enter password "{password}"')
def step_enter_password(context, password):
    """Enter password"""
    context.login_page.enter_password(password)
    print(f"✓ Entered password")

@when('I click the login button')
def step_click_login(context):
    """Click login button"""
    context.login_page.click_login()
    print("✓ Clicked login button")

@when('I login with username "{username}" and password "{password}"')
def step_complete_login(context, username, password):
    """Complete login action"""
    if not hasattr(context, 'login_page'):
        context.login_page = LoginPage(context.page)
        context.login_page.navigate_to_login()
    
    context.login_page.login(username, password)
    print(f"✓ Logged in as: {username}")

@then('I should see the dashboard')
def step_verify_dashboard(context):
    """Verify dashboard is shown"""
    expect(context.page).to_have_url("**/dashboard")
    print("✓ On dashboard page")

@then('I should see error message "{message}"')
def step_verify_error(context, message):
    """Verify error message"""
    error_text = context.login_page.get_error_message()
    assert message in error_text, f"Expected '{message}' in '{error_text}'"
    print(f"✓ Error message shown: {message}")

@then('the login title should be "{expected_title}"')
def step_verify_login_title(context, expected_title):
    """Verify login page title"""
    title = context.login_page.get_title()
    assert title == expected_title, f"Expected '{expected_title}', got '{title}'"
    print(f"✓ Login title: {title}")
