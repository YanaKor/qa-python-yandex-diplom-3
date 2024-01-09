from base.locators import Urls


class Endpoints:
    REGISTER_USER = f'{Urls.BASE_URL}/api/auth/register'
    DELETE_USER = f'{Urls.BASE_URL}/api/auth/user'
    GET_ORDERS = f'{Urls.BASE_URL}/api/orders'
