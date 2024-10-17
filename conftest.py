import pytest
import requests
from urls import *
import random

@pytest.fixture(scope="module")  # создание и удаление уникального пользователя
def unique_user():
    user_data = {
        "email": "unique_user_{}@mail.ru".format(random.randint(1000, 9999)), # Генерация случайного числа для уникальности
        "password": "password777",
        "name": "Username"
    }
    response = requests.post(AUTH_REGISTER_URL, json=user_data)
    assert response.status_code == 200
    yield user_data  # возврат данных пользователя для использования в тестах



