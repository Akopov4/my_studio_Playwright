
from playwright.sync_api import Locator, Playwright, expect

from constants import MAIN_PAGE


class BasePage:

    def __init__(self, playwright: Playwright):
        self.playwright = playwright
        self.browser = self.playwright.firefox.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.browser.new_page()

    def navigate_to_main_page(self):
        self.page.goto(MAIN_PAGE)

    def find_element_by(self, selector) -> Locator:
        return self.page.locator(selector)

    def enter_text(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def click_on_element(self, selector):
        self.page.locator(selector).click()

    def verify_text(self, selector: str, text_to_compare: str):
        expect(self.page.locator(selector)).to_have_text(text_to_compare)

    def wait_element_to_be_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()
