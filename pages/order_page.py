import allure

from pages.base_page import BasePage
from base.locators import OrderFeedLocators as OFL
from api.user_orders import CreateOrderByAPI


class OrderFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Click on order in list')
    def click_on_order(self):
        self.click(OFL.THIRD_ORDER)

    @allure.step('Create new order')
    def create_new_order(self, token):
        CreateOrderByAPI.create_new_order(token)

    @allure.step("Getting a list of orders on the user's order history page")
    def get_user_orders_on_history_page(self, orders):
        last_order = ('#0' + str(orders[-1]))
        self.wait_element_text_to_be_present(OFL.USER_ORDERS_HISTORY, last_order)
        return last_order

    @allure.step('Getting a complete list of orders in the order feed')
    def get_orders_number_in_order_feed(self):
        all_numbers = self.all_elements_is_visible(OFL.ORDER_NUMBERS)
        order_list = []
        for number in all_numbers:
            num1 = number.text
            order_list.append(num1)
        return order_list

    @allure.step('Receiving an order number')
    def get_user_orders(self, orders):
        last_order = ('0' + str(orders[-1]))
        self.wait_element_text_to_be_present(OFL.USER_ORDERS_HISTORY, last_order)
        return last_order

    @allure.step("Getting the user's order number in progress")
    def get_user_order_in_progress(self, num):
        self.wait_element_text_to_be_present(OFL.ORDER_IN_PROGRESS, num)
        return self.get_text(OFL.ORDER_IN_PROGRESS)

    @allure.step('Getting the order counter value')
    def get_orders_counter_value(self, locator):
        self.element_is_visible(OFL.ORDER_FEED_HEADER)
        nums = self.get_count_value(locator)
        return int(str(nums))

    @allure.step('Check order modal window is visible')
    def check_order_modal_window_is_visible(self):
        return self.modal_window_is_open(OFL.MODAL_ORDER_WINDOW)

