"""
Base Page Object
Common functionality for all page objects
"""
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url: str):
        """Navigate to URL"""
        self.page.goto(url)
    
    def wait_for_load(self, state: str = "networkidle"):
        """Wait for page to load"""
        self.page.wait_for_load_state(state)
    
    def click(self, selector: str):
        """Click element"""
        self.page.click(selector)
    
    def fill(self, selector: str, text: str):
        """Fill input field"""
        self.page.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        """Get element text content"""
        return self.page.text_content(selector)
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.is_visible(selector)
    
    def wait_for_selector(self, selector: str, timeout: int = 30000):
        """Wait for selector to appear"""
        self.page.wait_for_selector(selector, timeout=timeout)
    
    def get_attribute(self, selector: str, attribute: str) -> str:
        """Get element attribute"""
        return self.page.get_attribute(selector, attribute)
    
    def screenshot(self, path: str):
        """Take screenshot"""
        self.page.screenshot(path=path)
