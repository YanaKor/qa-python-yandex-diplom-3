import allure
import pytest

from base.locators import MainPageLocators as MPL, OrderFeedLocators as OFL
from pages.main_page import MainPage
from pages.order_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


@allure.suite('Test order feed area')
class TestOrderFeed:

    @allure.title('Order details')
    @allure.description('Checking for order details popup to open')
    def test_order_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_link()
        order_page = OrderFeedPage(driver)
        order_page.click_on_order()
        order_page.check_order_modal_window_is_visible()

    @allure.title("User's orders displayed in order feed")
    @allure.description("Orders from the user's order history are displayed in the order feed")
    def test_user_orders_displayed_in_order_feed(self, driver, login_user, get_order_number):
        main_page = MainPage(driver)
        main_page.go_to_personal_account(MPL.PERSONAL_ACCOUNT_BUTTON)
        personal_acc = PersonalAccountPage(driver)
        personal_acc.click_on_order_history_btn()
        order_page = OrderFeedPage(driver)
        order_page.get_user_orders_on_history_page(get_order_number)
        main_page.click_on_order_feed_link()
        order_page.check_user_orders_in_order_feed(get_order_number)

    @allure.title('Check order count after making a new order')
    @allure.description('When creating a new order, the counter increases')
    @pytest.mark.parametrize('counter', [OFL.TODAY_COUNTER, OFL.ALL_TIME_COUNTER])
    def test_order_count_in_day(self, driver, create_new_user_by_api, login_user, counter):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_link()
        order_page = OrderFeedPage(driver)
        previous_num = order_page.get_orders_counter_value(counter)
        data = create_new_user_by_api
        order_page.create_new_order(data[1].json()["accessToken"])
        present_num = order_page.get_orders_counter_value(counter)
        order_page.checking_the_increase_num_of_orders(previous_num, present_num)

    @allure.title('Check orders in progress')
    @allure.description('After placing an order, its number appears in the In progress section')
    def test_order_in_progress(self, driver, login_user, get_order_number):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_link()
        order_page = OrderFeedPage(driver)
        new_order = order_page.get_user_orders(get_order_number)
        order_in_progress = order_page.get_user_order_in_progress(new_order)
        order_page.checking_num_of_a_new_order_and_an_order_in_progress(new_order, order_in_progress)
