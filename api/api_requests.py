import requests
from api.urls import USER_REGISTER, USER_LOGIN, USER_UPDATE, ORDER_CREATE, ORDER_GET

class ApiRequests:  # Класс для работы с API
    @staticmethod
    def create_user(user):  # Создает пользователя через API
        return requests.post(USER_REGISTER, json=user)

    @staticmethod
    def login_user(user):  # Логинит пользователя через API
        return requests.post(USER_LOGIN, json=user)

    @staticmethod
    def delete_user(token):  # Удаляет пользователя через API
        return requests.delete(USER_UPDATE, headers={"Authorization": token})

    @staticmethod
    def update_user(user, token):  # Обновляет данные пользователя через API
        return requests.patch(USER_UPDATE, json=user, headers={"Authorization": token})

    @staticmethod
    def create_order(ingredient_ids, token):  # Создает заказ с указанными ингредиентами
        return requests.post(ORDER_CREATE, json={"ingredients": ingredient_ids}, headers={"Authorization": token})

    @staticmethod
    def get_orders(token):  # Получает заказы пользователя
        return requests.get(ORDER_GET, headers={"Authorization": token})

