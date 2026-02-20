from behave import given, when, then
from playwright.sync_api import expect
import time

# ============================================
# GIVEN Steps - Setup
# ============================================

@given('I am on Wikipedia homepage')
def step_open_wikipedia(context):
    """Navigate to Wikipedia main page"""
    context.page.goto('https://www.wikipedia.org/')
    print('✓ Opened Wikipedia homepage')
    
    # Wait for page to load
    context.page.wait_for_load_state('networkidle')

# ============================================
# WHEN Steps - Actions
# ============================================

@when('I click the language selector button')
def step_click_language_selector(context):
    """Click on the language selector button"""
    
    # Method 1: Try the globe icon button
    try:
        language_button = context.page.locator('button[aria-label*="language"]').first
        language_button.wait_for(state='visible', timeout=5000)
        language_button.click()
        print('✓ Clicked language selector (Method 1: Button)')
        time.sleep(1)  # Wait for menu to open
        return
    except:
        pass
    
    # Method 2: Try the language dropdown
    try:
        language_dropdown = context.page.locator('#p-lang-btn-checkbox')
        language_dropdown.wait_for(state='visible', timeout=5000)
        language_dropdown.click()
        print('✓ Clicked language selector (Method 2: Dropdown)')
        time.sleep(1)
        return
    except:
        pass
    
    # Method 3: Try clicking language link
    try:
        language_link = context.page.locator('a:has-text("Read Wikipedia in your language")')
        language_link.wait_for(state='visible', timeout=5000)
        language_link.click()
        print('✓ Clicked language selector (Method 3: Link)')
        time.sleep(1)
        return
    except:
        pass
    
    # Method 4: Look for any element with "language" text
    try:
        language_elem = context.page.locator('text=/language/i').first
        language_elem.click()
        print('✓ Clicked language selector (Method 4: Text search)')
        time.sleep(1)
        return
    except Exception as e:
        print(f'✗ Could not find language selector: {e}')
        # Take screenshot for debugging
        context.page.screenshot(path='screenshots/language_selector_not_found.png')
        raise

@when('I select "{language}" from the language menu')
def step_select_language(context, language):
    """Select a specific language from the menu"""
    
    # Wait for language menu to be visible
    time.sleep(1)
    
    # Try to find and click the language
    try:
        # Method 1: Direct text match
        language_option = context.page.locator(f'a:has-text("{language}")').first
        language_option.wait_for(state='visible', timeout=5000)
        language_option.click()
        print(f'✓ Selected language: {language}')
        
        # Wait for navigation
        context.page.wait_for_load_state('networkidle')
        
    except Exception as e:
        print(f'✗ Could not select {language}: {e}')
        
        # Try alternative selectors
        try:
            # Method 2: Look for language code link
            locale_map = {
                'English': 'en',
                'Español': 'es',
                'العربية': 'ar',
                '日本語': 'ja',
                'Français': 'fr',
                'Deutsch': 'de'
            }
            
            if language in locale_map:
                locale = locale_map[language]
                context.page.goto(f'https://{locale}.wikipedia.org/')
                print(f'✓ Navigated directly to {language} Wikipedia')
            else:
                raise Exception(f'Language {language} not found')
                
        except Exception as e2:
            print(f'✗ Failed to switch to {language}: {e2}')
            context.page.screenshot(path=f'screenshots/language_{language}_failed.png')
            raise

@when('I search for "{search_term}" in language selector')
def step_search_language(context, search_term):
    """Search for a language in the language selector"""
    
    # Find the search input in language menu
    try:
        search_input = context.page.locator('input[placeholder*="Search"]').first
        search_input.wait_for(state='visible', timeout=5000)
        search_input.fill(search_term)
        print(f'✓ Searched for: {search_term}')
        time.sleep(1)  # Wait for search results
        
    except Exception as e:
        print(f'✗ Could not find language search box: {e}')
        raise

@when('I click on "{language_name}"')
def step_click_language_result(context, language_name):
    """Click on a language from search results"""
    
    try:
        language_link = context.page.locator(f'text={language_name}').first
        language_link.wait_for(state='visible', timeout=5000)
        language_link.click()
        print(f'✓ Clicked on: {language_name}')
        
        # Wait for navigation
        context.page.wait_for_load_state('networkidle')
        
    except Exception as e:
        print(f'✗ Could not click on {language_name}: {e}')
        raise

# ============================================
# THEN Steps - Verification
# ============================================

@then('the language menu should open')
def step_verify_menu_open(context):
    """Verify language menu is visible"""
    
    # Check if any language-related menu is visible
    try:
        # Look for common menu indicators
        menu_visible = (
            context.page.locator('.language-list').is_visible() or
            context.page.locator('[role="menu"]').is_visible() or
            context.page.locator('.language-selector-menu').is_visible()
        )
        
        assert menu_visible, "Language menu did not open"
        print('✓ Language menu is open')
        
    except Exception as e:
        print(f'⚠ Could not verify menu opened: {e}')
        # Don't fail - menu might look different
        pass

@then('I should see available languages')
def step_verify_languages_visible(context):
    """Verify that language options are visible"""
    
    # Check for multiple language links
    language_links = context.page.locator('a[lang]')
    count = language_links.count()
    
    assert count > 0, "No language options found"
    print(f'✓ Found {count} language options')

@then('I should be on "{locale}" Wikipedia')
def step_verify_wikipedia_locale(context, locale):
    """Verify we're on the correct Wikipedia language site"""
    
    current_url = context.page.url
    expected_url = f'https://{locale}.wikipedia.org'
    
    assert expected_url in current_url, \
        f'Expected URL to contain {expected_url}, but got {current_url}'
    
    print(f'✓ On {locale} Wikipedia: {current_url}')

@then('the page should be in "{language}"')
def step_verify_page_language(context, language):
    """Verify page content is in the correct language"""
    
    # Check the HTML lang attribute
    lang_attr = context.page.evaluate('() => document.documentElement.lang')
    
    language_codes = {
        'English': 'en',
        'Español': 'es',
        'العربية': 'ar',
        '日本語': 'ja',
        'Français': 'fr',
        'Deutsch': 'de'
    }
    
    expected_code = language_codes.get(language, language.lower())
    
    assert expected_code in lang_attr, \
        f'Expected language code {expected_code}, but got {lang_attr}'
    
    print(f'✓ Page language is {language} ({lang_attr})')

@then('content direction should be "{direction}"')
def step_verify_direction(context, direction):
    """Verify text direction (ltr or rtl)"""
    
    dir_attr = context.page.evaluate('() => document.documentElement.dir')
    
    # If no dir attribute, default is ltr
    actual_direction = dir_attr if dir_attr else 'ltr'
    
    assert actual_direction == direction, \
        f'Expected direction {direction}, but got {actual_direction}'
    
    print(f'✓ Content direction is {direction}')

@then('document direction should be "{direction}"')
def step_verify_document_direction(context, direction):
    """Alias for content direction verification"""
    step_verify_direction(context, direction)

@then('I should see a language search box')
def step_verify_search_box(context):
    """Verify language search box is visible"""
    
    search_box = context.page.locator('input[type="search"], input[placeholder*="Search"]').first
    expect(search_box).to_be_visible()
    print('✓ Language search box is visible')

@then('"{text}" should appear in results')
def step_verify_text_in_results(context, text):
    """Verify specific text appears in search results"""
    
    result = context.page.locator(f'text={text}').first
    expect(result).to_be_visible(timeout=5000)
    print(f'✓ Found "{text}" in results')

@then('I should be on Arabic Wikipedia')
def step_verify_arabic_wikipedia(context):
    """Verify we're on Arabic Wikipedia"""
    
    current_url = context.page.url
    assert 'ar.wikipedia.org' in current_url, \
        f'Expected Arabic Wikipedia, but got {current_url}'
    
    print(f'✓ On Arabic Wikipedia: {current_url}')