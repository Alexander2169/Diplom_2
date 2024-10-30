import requests
from urls import USER_REGISTER, USER_LOGIN, USER_UPDATE, ORDER_CREATE, ORDER_GET

class User:  # Содержит классы и методы для работы с данными пользователей
    def __init__(self, email, password, name):  # Инициализирует объект пользователя с email, паролем и именем
        self.email = email
        self.password = password
        self.name = name

def create_user(user):  # Создает пользователя через API
    return requests.post(USER_REGISTER, json=user.__dict__)

def login_user(user):  # Логинит пользователя через API
    return requests.post(USER_LOGIN, json=user.__dict__)

def delete_user(token):  # Удаляет пользователя через API
    return requests.delete(USER_UPDATE, headers={"Authorization": token})

def update_user(user, token):  # Обновляет данные пользователя через API
    return requests.patch(USER_UPDATE, json=user.__dict__, headers={"Authorization": token})

def create_order(ingredient_ids, token):  # Создает заказ с указанными ингредиентами
    return requests.post(ORDER_CREATE, json={"ingredients": ingredient_ids}, headers={"Authorization": token})

def get_orders(token):  # Получает заказы пользователя
    return requests.get(ORDER_GET, headers={"Authorization": token})
