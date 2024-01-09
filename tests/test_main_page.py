import time

import allure

from pages.main_page import MainPage


@allure.suite('Test main functionality')
class TestMainPage:

    @allure.title('Transition to constructor page ')
    @allure.description('Checking the transition from the order feed page to the constructor page')
    def test_transition_to_constructor_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_feed_page()
        main_page.click_on_constructor_link()
        main_page.check_constructor_is_active()

    @allure.title('Transition to order page')
    @allure.description('Checking the transition from the main page to the order feed page')
    def test_transition_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_link()
        main_page.check_order_feed_is_active()

    @allure.title('Open modal window')
    @allure.description('Checking the opening of an ingredient detailed information modal window')
    def test_ingredients_info_modal_window_is_open(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_ingredient()
        main_page.check_modal_window_is_open()

    @allure.title('Close modal window')
    @allure.description('Checking the closing of the ingredient detailed information modal window')
    def test_close_ingredients_info_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_ingredient()
        main_page.click_on_close_modal_window_cross()
        main_page.check_modal_window_is_closed()

    @allure.title('Append ingredient in order')
    @allure.description('Checking the increase in the number of ingredients in the order')
    def test_append_ingredient_in_order(self, driver):
        main_page = MainPage(driver)
        count_before = main_page.get_count_ingredients_value()
        time.sleep(3)
        main_page.drag_and_drop_ingredient()
        time.sleep(3)
        count_after = main_page.get_count_ingredients_value()
        main_page.check_ingredient_counter(count_before, count_after)

    @allure.title('Create order')
    @allure.description('Verifying that an order has been created by an authorized user')
    def test_create_order_by_authorized_user(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()
        main_page.click_on_create_order_btn()
        main_page.check_modal_window_is_open()
