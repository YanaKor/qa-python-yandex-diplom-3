import requests
from faker import Faker
from api.endpoints import Endpoints
from api.helpers import generate_random_string

faker = Faker()


class RegisterUserByApi:
    @staticmethod
    def register_new_user_and_return_login_password():
        login_pass = []

        email = faker.email()
        password = generate_random_string(10)
        username = faker.name()

        payload = {
            "email": email,
            "password": password,
            "name": username
        }

        response = requests.post(f"{Endpoints.REGISTER_USER}", data=payload)

        if response.status_code == 200:
            login_pass.append(email)
            login_pass.append(password)
            login_pass.append(username)

        return login_pass, response
