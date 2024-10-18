import requests
from urls import *

class User:
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

class UserClient:

    @staticmethod
    def post_create_new_user(user):
        url = REGISTER_PEN
        response = requests.post(url, json={
            "name": user.name,
            "email": user.email,
            "password": user.password
        })
        return response

    @staticmethod
    def post_login_user(email, password):
        url = LOGIN_PEN
        response = requests.post(url, json={
            "email": email,
            "password": password
        })
        return response

    @staticmethod
    def delete_user(token):
        url = USER_PEN
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(url, headers=headers)
        return response

    @staticmethod
    def patch_user(token, updated_data):
        url = USER_PEN  # Здесь нужно указать правильный URL для PATCH-запроса
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.patch(url, json=updated_data, headers=headers)
        return response

    @staticmethod
    def check_failed_response_auth_register(response):
        assert response.status_code != 200

    @staticmethod
    def get_user(token):
        url = USER_PEN
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def create_order(token, ingredients):
        url = f"{BASE_URL}/orders"
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        response = requests.post(url, json={"ingredients": ingredients}, headers=headers)
        return response
