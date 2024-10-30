import random
import string
import requests
import allure
from urls import USER_REGISTER, USER_LOGIN, USER_UPDATE, ORDER_CREATE, ORDER_GET

class User:  # Содержит классы и методы для работы с данными пользователей
    def __init__(self, email, password, name):  # Инициализирует объект пользователя с email, паролем и именем
        self.email = email
        self.password = password
        self.name = name

@allure.step("Генерирует случайного пользователя")
def generate_random_user():  # Генерирует случайного пользователя
    email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@mail.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    name = ''.join(random.choices(string.ascii_letters, k=7))
    return User(email, password, name)

@allure.step("Создает временного пользователя")
def clean_user():  # Создает временного пользователя
    return generate_random_user()

@allure.step("Создает пользователя с уникальным email")
def user_with_email():  # Создает пользователя с уникальным email
    return generate_random_user()

@allure.step("Создает пользователя через API")
def create_user(user):  # Создает пользователя через API
    return requests.post(USER_REGISTER, json=user.__dict__)

@allure.step("Логинит пользователя через API")
def login_user(user):  # Логинит пользователя через API
    return requests.post(USER_LOGIN, json=user.__dict__)

@allure.step("Удаляет пользователя через API")
def delete_user(token):  # Удаляет пользователя через API
    return requests.delete(USER_UPDATE, headers={"Authorization": token})

@allure.step("Обновляет данные пользователя через API")
def update_user(user, token):  # Обновляет данные пользователя через API
    return requests.patch(USER_UPDATE, json=user.__dict__, headers={"Authorization": token})

@allure.step("Создает заказ с указанными ингредиентами")
def create_order(ingredient_ids, token):  # Создает заказ с указанными ингредиентами
    return requests.post(ORDER_CREATE, json={"ingredients": ingredient_ids}, headers={"Authorization": token})

@allure.step("Получает заказы пользователя")
def get_orders(token):  # Получает заказы пользователя
    return requests.get(ORDER_GET, headers={"Authorization": token})

@allure.step("Регистрация и удаление пользователя")
def register_and_delete_user(user):  # Регистрация и удаление пользователя
    response = create_user(user)
    if response.status_code == 200:
        token = response.json()["accessToken"]
        delete_user(token)






