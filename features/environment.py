"""
Behave Environment Configuration
Setup and teardown for tests
"""
import os
from playwright.sync_api import sync_playwright
from pathlib import Path

def before_all(context):
    """Runs once before all tests"""
    print("🚀 Starting test suite...")
    
    # Create directories
    Path("screenshots").mkdir(exist_ok=True)
    Path("reports").mkdir(exist_ok=True)
    Path("traces").mkdir(exist_ok=True)
    
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()

def before_scenario(context, scenario):
    """Runs before each scenario"""
    # Get configuration from environment
    browser_name = os.getenv('BROWSER', 'chromium')
    headless = os.getenv('HEADLESS', 'false').lower() == 'true'
    slow_mo = int(os.getenv('SLOW_MO', '0'))
    
    # Start Playwright
    context.playwright = sync_playwright().start()
    
    # Launch browser
    if browser_name == 'firefox':
        context.browser = context.playwright.firefox.launch(
            headless=headless,
            slow_mo=slow_mo
        )
    elif browser_name == 'webkit':
        context.browser = context.playwright.webkit.launch(
            headless=headless,
            slow_mo=slow_mo
        )
    else:
        context.browser = context.playwright.chromium.launch(
            headless=headless,
            slow_mo=slow_mo
        )
    
    # Get locale from environment or use default
    locale = os.getenv('LOCALE', 'en-US')
    timezone = os.getenv('TIMEZONE', 'America/New_York')
    
    # Create context with locale and timezone
    context.browser_context = context.browser.new_context(
        locale=locale,
        timezone_id=timezone,
        viewport={'width': 1920, 'height': 1080}
    )
    
    # Start tracing
    context.browser_context.tracing.start(screenshots=True, snapshots=True)
    
    # Create page
    context.page = context.browser_context.new_page()
    
    # Store scenario info
    context.scenario_name = scenario.name
    context.current_locale = locale
    
    print(f"✓ Started scenario: {scenario.name} (Locale: {locale})")

def after_scenario(context, scenario):
    """Runs after each scenario"""
    # Take screenshot on failure
    if scenario.status == "failed":
        screenshot_path = f"screenshots/{scenario.name.replace(' ', '_')}.png"
        context.page.screenshot(path=screenshot_path)
        print(f"📸 Screenshot saved: {screenshot_path}")
        
        # Save trace
        trace_path = f"traces/{scenario.name.replace(' ', '_')}.zip"
        context.browser_context.tracing.stop(path=trace_path)
        print(f"📊 Trace saved: {trace_path}")
    else:
        context.browser_context.tracing.stop()
    
    # Clean up
    context.page.close()
    context.browser_context.close()
    context.browser.close()
    context.playwright.stop()
    
    status_icon = "✅" if scenario.status == "passed" else "❌"
    print(f"{status_icon} Finished scenario: {scenario.name} - {scenario.status}")

def after_all(context):
    """Runs once after all tests"""
    print("🎉 Test suite completed!")
