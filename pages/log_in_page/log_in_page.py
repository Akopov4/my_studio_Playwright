from pages.base_page import BasePage


class LogInPage(BasePage):
    def enter_login(self, email:str):
        self.enter_text('#login', email)

    def enter_psswd(self, psswd:str):
        self.enter_text('#pwd', psswd)

    def click_submit(self):
        self.click_on_element('#smbt')

    



