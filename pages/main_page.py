import allure

from pages.base_page import BasePage
from base.locators import Urls, MainPageLocators as MPL


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open feed page')
    def open_feed_page(self):
        self.open_page(Urls.FEED_PAGE)

    @allure.step('Clicking on personal account button')
    def go_to_personal_account(self, locator):
        self.click(locator)

    @allure.step('Click on constructor link')
    def click_on_constructor_link(self):
        self.click(MPL.CONSTRUCTOR_BUTTON)

    @allure.step('Click on order feed link')
    def click_on_order_feed_link(self):
        self.click(MPL.ORDER_FEED_BUTTON)

    @allure.step('Click on bun detail info')
    def click_on_bun_ingredient(self):
        self.click(MPL.BUN_INGREDIENT)

    @allure.step('Close modal window')
    def click_on_close_modal_window_cross(self):
        self.click(MPL.CLOSE_MODAL_WINDOW)

    @allure.step('Add bun to burger')
    def drag_and_drop_ingredient(self):
        source = self.element_is_visible(MPL.BUN_INGREDIENT)
        target = self.element_is_visible(MPL.CONSTRUCTOR_BASKET)
        self.drag_and_drop(source, target)

    @allure.step('Get count of ingredients in burger')
    def get_count_ingredients_value(self):
        return self.get_count_value(MPL.COUNTER)

    @allure.step('Crate order')
    def click_on_create_order_btn(self):
        self.click(MPL.CREATE_ORDER)

    @allure.step('Checking the activity of the constructor page')
    def check_constructor_is_active(self):
        self.focus_on_element(MPL.CONSTRUCTOR_BUTTON, 'class', MPL.FOCUSED_TEXT)

    @allure.step('Checking the activity of the order feed page')
    def check_order_feed_is_active(self):
        self.focus_on_element(MPL.ORDER_FEED_BUTTON, 'class', MPL.FOCUSED_TEXT)

    @allure.step('Checking if a modal window is open')
    def check_modal_window_is_open(self):
        self.modal_window_is_open(MPL.MODAL_WINDOW)

    @allure.step('Check if a modal window is closed')
    def check_modal_window_is_closed(self):
        return self.element_is_invisible(MPL.MODAL_WINDOW)

    @allure.step('Checking the ingredient quantity counter change')
    def check_ingredient_counter(self, count_before, count_after):
        assert count_after > count_before, 'The number of ingredients has not changed'
