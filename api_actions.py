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
        url = USER_PEN
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
        url = ORDER_PEN

        # Проверка на наличие ингредиентов
        if not ingredients:
            return requests.Response()  # Возвращаем пустой объект Response для обработки в тестах

        headers = {"Authorization": f"Bearer {token}"} if token else {}
        response = requests.post(url, json={"ingredients": ingredients}, headers=headers)

        # Обработка ошибок
        if response.status_code == 400:
            return response  # Возвращаем оригинальный ответ для 400
        elif response.status_code == 500:
            return response  # Возвращаем оригинальный ответ для 500

        return response  # Возвращаем оригинальный ответ для успешного запроса

    @staticmethod
    def get_ingredients():
        url = INGREDIENTS_PEN
        response = requests.get(url)
        return response

    @staticmethod
    def get_orders(token):
        url = ORDER_PEN
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def get_all_orders():
        url = ORDER_PEN_ALL
        response = requests.get(url)
        return response

    @staticmethod
    def get_auth_token():
        return ("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
                "eyJpZCI6IjY3MTI5YmViOWVkMjgwMDAxYjRlNzBmZCIsImlhdCI6MTcyOTI3MjgxMSwiZXhwIjoxNzI5Mjc0MDExfQ."
                "hnZgWt6AYESWLEOEUKZU_vfYeCh0ZW7XE1vobFiWIL8")
