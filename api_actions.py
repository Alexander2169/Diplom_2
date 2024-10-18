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
        url = REGISTER
        response = requests.post(url, json={
            "name": user.name,
            "email": user.email,
            "password": user.password
        })
        return response

    @staticmethod
    def post_login_user(email, password):
        url = LOGIN
        response = requests.post(url, json={
            "email": email,
            "password": password
        })
        return response

    @staticmethod
    def delete_user(token):
        url = DELETE_USER
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(url, headers=headers)
        return response

    @staticmethod
    def check_failed_response_auth_register(response):
        assert response.status_code != 200
