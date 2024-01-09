import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def element_is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def all_elements_is_visible(self, locator):
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def element_is_invisible(self, locator):
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def find_element(self, locator):
        self.driver.find_elements(*locator)

    @allure.step('Open page')
    def open_page(self, url):
        return self.driver.get(url)

    @allure.step('Fill text')
    def fill_field(self, locator, text):
        self.element_is_visible(locator).send_keys(text)

    @allure.step('Clicking on element')
    def click(self, locator):
        return self.element_is_clickable(locator).click()

    @allure.step('Get text')
    def get_text(self, locator):
        return self.element_is_visible(locator).text

    @allure.step('Get current url address')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Checking that the current url contains text')
    def checking_text_in_current_url(self, text):
        return self.wait.until(ec.url_contains(text))

    @allure.step('Focus on element')
    def focus_on_element(self, locator, attribute, text):
        return self.wait.until(ec.text_to_be_present_in_element_attribute(locator, attribute, text))

    @allure.step('')
    def drag_and_drop(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    def modal_window_is_open(self, locator):
        return self.element_is_visible(locator)

    def get_count_value(self, locator):
        return self.get_text(locator)

    def wait_element_text_to_be_present(self, locator, text):
        self.wait.until(ec.text_to_be_present_in_element(locator, text))
