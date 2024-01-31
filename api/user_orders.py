import requests
from api.endpoints import Endpoints


class CreateOrderByAPI:
    @staticmethod
    def create_new_order(access_token):
        headers = {"Authorization": f"{access_token}"}
        payload = {
            'ingredients': ['61c0c5a71d1f82001bdaaa6c', '61c0c5a71d1f82001bdaaa71']
        }
        requests.post(f'{Endpoints.GET_ORDERS}', data=payload, headers=headers)

    @staticmethod
    def get_user_orders(access_token):
        headers = {"Authorization": f"{access_token}"}
        response = requests.get(f'{Endpoints.GET_ORDERS}', headers=headers)
        return response.json().get('orders')
