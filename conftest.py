import pytest
import requests
import time
from urls import AUTH_REGISTER_URL
from tokens import access_token, refresh_token

@pytest.fixture(scope="module")  # создание и удаление уникального пользователя
def unique_user():
    user_data = {
        "email": f"unique_user_{int(time.time())}@mail.ru",
        "password": "password123",
        "name": "Unique User"
    }
    response = requests.post(AUTH_REGISTER_URL, json=user_data)
    assert response.status_code == 200
    yield user_data  # возврат данных пользователя для использования в тестах


