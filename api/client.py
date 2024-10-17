import requests
from .urls import AUTH_REGISTER_URL, AUTH_LOGIN_URL, AUTH_USER_URL, ORDER_URL

class UserClient:
    def register_user(self, email, password, name):
        response = requests.post(AUTH_REGISTER_URL, json={"email": email, "password": password, "name": name})
        return response

    def login_user(self, email, password):
        response = requests.post(AUTH_LOGIN_URL, json={"email": email, "password": password})
        return response

    def update_user(self, token, data):
        headers = {"Authorization": token}
        response = requests.patch(AUTH_USER_URL, json=data, headers=headers)
        return response

    def create_order(self, token, ingredients):
        headers = {"Authorization": token}
        response = requests.post(ORDER_URL, json={"ingredients": ingredients}, headers=headers)
        return response

    def get_user_orders(self, token):
        headers = {"Authorization": token}
        response = requests.get(ORDER_URL, headers=headers)
        return response
