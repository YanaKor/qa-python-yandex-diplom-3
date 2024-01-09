import allure

from pages.base_page import BasePage
from base.locators import PersonalAccountLocators as PAL, Urls


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Fill email and password field')
    def enter_email_and_password(self, email, password):
        self.fill_field(PAL.LOGIN_EMAIL_FIELD, email)
        self.fill_field(PAL.LOGIN_PASSWORD_FIELD, password)

    @allure.step('Clicking on login button')
    def click_on_login_btn(self):
        self.click(PAL.LOGIN_BUTTON)

    @allure.step('Clicking on order history button')
    def click_on_order_history_btn(self):
        self.click(PAL.ORDERS_HISTORY)

    @allure.step('Clicking on logout button')
    def click_on_logout_btn(self):
        self.click(PAL.LOGOUT_BUTTON)

    @allure.step('Checking the transition to personal account page')
    def check_transition_to_personal_account_page(self):
        self.checking_text_in_current_url(Urls.PERSONAL_ACCOUNT), \
            'The page link is not what you expected. ' \
            f'Expected {Urls.PERSONAL_ACCOUNT}, but got {self.get_current_url()}'

    @allure.step('Checking the transition to order history page')
    def check_transition_to_order_history_page(self):
        self.checking_text_in_current_url(Urls.ORDER_HISTORY), \
            'The page link is not what you expected. ' \
            f'Expected {Urls.ORDER_HISTORY}, but got {self.get_current_url()}'

    @allure.step('Checking logout from personal account')
    def check_transition_to_login_page(self):
        self.checking_text_in_current_url(Urls.LOGIN_PAGE), \
            'The page link is not what you expected. ' \
            f'Expected {Urls.LOGIN_PAGE}, but got {self.get_current_url()}'
