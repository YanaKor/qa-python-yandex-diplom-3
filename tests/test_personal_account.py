import allure

from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from base.locators import MainPageLocators as MPL


@allure.suite('Test personal account')
class TestPersonalAccount:

    @allure.title('Checking transition to personal account')
    @allure.description('Checking transition to personal account by clicking on "Personal account" button on main page')
    def test_transition_to_personal_account(self, driver, login_user):
        main_page = MainPage(driver)
        personal_account = PersonalAccountPage(driver)
        main_page.go_to_personal_account(MPL.PERSONAL_ACCOUNT_BUTTON)
        personal_account.check_transition_to_personal_account_page()

    @allure.title('Checking transition to "Order history"')
    @allure.description('Checking transition to order history page by clicking on "Order history"'
                        ' button in profile page')
    def test_transition_to_order_history_page(self, driver, login_user):
        main_page = MainPage(driver)
        personal_account = PersonalAccountPage(driver)
        main_page.go_to_personal_account(MPL.PERSONAL_ACCOUNT_BUTTON)
        personal_account.click_on_order_history_btn()
        personal_account.check_transition_to_order_history_page()

    @allure.title('Log out from personal account')
    @allure.description('Checking log out from personal account by clicking on "logout" button')
    def test_logout_from_personal_account(self, driver, login_user):
        main_page = MainPage(driver)
        personal_account = PersonalAccountPage(driver)
        main_page.go_to_personal_account(MPL.PERSONAL_ACCOUNT_BUTTON)

        personal_account.click_on_logout_btn()
        personal_account.check_transition_to_login_page()
