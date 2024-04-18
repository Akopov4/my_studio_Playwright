from pages.log_in_page.log_in_page import LogInPage

from constants import MANGER_EMAIL, MANAGER_PASS, STAFF_EMAIl, STAFF_PASS


class LogInTest:
    def test_manager_log_in(self, playwright_fixture):
        log_in_page = LogInPage(playwright_fixture)
        log_in_page.enter_login(MANGER_EMAIL)
        log_in_page.enter_psswd(MANAGER_PASS)
        log_in_page.click_submit()
        assert log_in_page.verify_text('caption_selector', 'Analytics2222') == 'Analytics'

    def test_staff_log_in(self, playwright_fixture):
        log_in_page = LogInPage(playwright_fixture)
        log_in_page.enter_login(STAFF_EMAIl)
        log_in_page.enter_psswd(STAFF_PASS)
        log_in_page.click_submit()
        assert log_in_page.verify_text('caption_selector', "Customers333333") == 'Customers'
