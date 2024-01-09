import allure
import pytest

from pages.password_recovery_page import PasswordRecoveryPage
from pages.main_page import MainPage
from base.locators import MainPageLocators as MPL


@allure.suite('Test recovery form')
class TestRecoveryForm:

    @allure.title('Checking transition to recovery form')
    @allure.description('Checking transition to recovery form by clicking on recovery button on login form page'
                        'ER: Password recovery page is open')
    def test_transition_to_recovery_form_by_clicking_on_recovery_button(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_recovery_form()
        recovery_page.click_on_recovery_form_link()
        recovery_page.check_transition_to_recovery_form()

    @allure.title('Checking fill email and click on recovering button ')
    @allure.description('Checking fill email field and click on recovering button.'
                        ' ER: Password reset page open')
    @pytest.mark.parametrize('locator', [MPL.LOGIN_BUTTON, MPL.PERSONAL_ACCOUNT_BUTTON])
    def test_fill_email_and_click_on_recovery_button(self, driver, locator):
        main_page = MainPage(driver)
        main_page.go_to_personal_account(locator)
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.click_on_recovery_form_link()
        recovery_page.fill_email_field()
        recovery_page.click_recovery_btn()
        recovery_page.check_transition_to_reset_password_page()

    @allure.title('Click on eye button')
    @allure.description('Clicking on eye button in password field. '
                        'ER: Email field is active active')
    @pytest.mark.parametrize('locator', [MPL.LOGIN_BUTTON, MPL.PERSONAL_ACCOUNT_BUTTON])
    def test_click_on_eye_button(self, driver, locator):
        main_page = MainPage(driver)
        main_page.go_to_personal_account(locator)
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.click_on_recovery_form_link()
        recovery_page.fill_email_field()
        recovery_page.click_recovery_btn()
        recovery_page.clicking_on_eye_btn()
        recovery_page.checking_focus_on_password_field()
