import allure

from pages.base_page import BasePage
from base.locators import Urls, PasswordRecoveryLocators as PRL


class PasswordRecoveryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open login form page')
    def open_recovery_form(self):
        self.open_page(Urls.LOGIN_PAGE)

    @allure.step('Clicking on recovery form link')
    def click_on_recovery_form_link(self):
        self.click(PRL.RECOVERY_PAGE_LINK)

    @allure.step('Fill email field')
    def fill_email_field(self):
        self.click(PRL.RECOVERY_EMAIL_FIELD)
        self.fill_field(PRL.RECOVERY_EMAIL_FIELD, PRL.RECOVERY_EMAIL)

    @allure.step('Clicking on recovery button')
    def click_recovery_btn(self):
        self.click(PRL.RECOVERY_BUTTON)

    @allure.step('Clicking on eye button')
    def clicking_on_eye_btn(self):
        self.click(PRL.EYE_BUTTON)

    @allure.step('Checking focus on a password field')
    def checking_focus_on_password_field(self):
        return self.focus_on_element(PRL.FOCUSED_FIELD, PRL.FOCUSED_TEXT)

    @allure.step('Checking the transition to the password recovery page')
    def check_transition_to_recovery_form(self):
        return self.get_current_url() == Urls.RECOVERY_PAGE

    @allure.step('Checking the transition to the password reset page')
    def check_transition_to_reset_password_page(self):
        return self.checking_text_in_current_url(Urls.RESET_PASSWORD_PAGE)
