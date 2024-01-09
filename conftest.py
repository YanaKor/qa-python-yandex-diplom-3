import pytest
import requests
from selenium import webdriver

from api.register_new_user import RegisterUserByApi
from api.endpoints import Endpoints
from api.user_orders import CreateOrderByAPI
from base.locators import MainPageLocators as MPL, Urls
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)

    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)

    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_new_user_by_api():
    data = RegisterUserByApi.register_new_user_and_return_login_password()

    yield data

    access_token = data[1].json()["accessToken"]
    requests.delete(f"{Endpoints.DELETE_USER}", headers={'Authorization': f'{access_token}'})


@pytest.fixture
def login_user(driver, create_new_user_by_api):
    main_page = MainPage(driver)
    main_page.go_to_personal_account(MPL.PERSONAL_ACCOUNT_BUTTON)
    personal_account = PersonalAccountPage(driver)
    user_data = create_new_user_by_api
    personal_account.enter_email_and_password(user_data[0][0], user_data[0][1])
    personal_account.click_on_login_btn()


@pytest.fixture
def get_order_number(create_new_user_by_api):
    data = create_new_user_by_api
    access_token = data[1].json()["accessToken"]
    CreateOrderByAPI.create_new_order(access_token)
    orders = CreateOrderByAPI.get_user_orders(access_token)
    orders_numbers = []
    for order in orders:
        orders_numbers.append(order["number"])
    return orders_numbers
