"""
Login Page Object
"""
from .base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    # Selectors
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    ERROR_MESSAGE = ".error-message"
    TITLE = "h1"
    FORGOT_PASSWORD = "a.forgot-password"
    
    def __init__(self, page):
        super().__init__(page)
        self.url = "/login"
    
    def navigate_to_login(self):
        """Navigate to login page"""
        base_url = self.page.context.browser.contexts[0]._impl_obj._options.get('baseURL', 'https://the-internet.herokuapp.com/')
        self.navigate(f"{base_url}{self.url}")
    
    def enter_username(self, username: str):
        """Enter username"""
        self.fill(self.USERNAME_INPUT, username)
    
    def enter_password(self, password: str):
        """Enter password"""
        self.fill(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Click login button"""
        self.click(self.LOGIN_BUTTON)
        self.wait_for_load()
    
    def login(self, username: str, password: str):
        """Complete login action"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self) -> str:
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def get_title(self) -> str:
        """Get page title"""
        return self.get_text(self.TITLE)
    
    def is_error_visible(self) -> bool:
        """Check if error message is visible"""
        return self.is_visible(self.ERROR_MESSAGE)
    
    def verify_on_login_page(self):
        """Verify we're on login page"""
        expect(self.page).to_have_url("**/login")
