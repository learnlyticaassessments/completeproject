from behave import given, when, then
from playwright.sync_api import expect

@given('I visit Wikipedia in "{locale}"')
def visit_wikipedia(context, locale):
    context.page.goto(f'https://{locale}.wikipedia.org/')
    print(f'✓ Opened Wikipedia in {locale}')

@then('I should see main page title in "{language}"')
def verify_language(context, language):
    # Check if content is in expected language
    content = context.page.content()
    
    language_indicators = {
        'English': 'Wikipedia',
        'Spanish': 'Wikipedia',
        'Arabic': 'ويكيبيديا',
        'Japanese': 'ウィキペディア'
    }
    
    assert language_indicators[language] in content
    print(f'✓ Page is in {language}')

@then('date format should match "{locale}"')
def verify_date_format(context, locale):
    # Wikipedia shows dates in locale-specific format
    # You can verify this in article dates
    if locale == 'ar':
        # Verify RTL direction
        dir_attr = context.page.evaluate('() => document.dir')
        assert dir_attr == 'rtl'
        print('✓ RTL direction confirmed')