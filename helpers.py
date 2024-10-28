import requests
from urls import USER_REGISTER, USER_LOGIN, USER_UPDATE, ORDER_CREATE, ORDER_GET

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

def register_and_delete_user(user):  # Регистрация и удаление пользователя
    response = create_user(user)
    if response.status_code == 200:
        token = response.json()["accessToken"]
        delete_user(token)




