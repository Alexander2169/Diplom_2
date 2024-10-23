import pytest
import requests
from urls import BASE_URL
from data import User

@pytest.fixture(scope="module") # Возвращает базовый URL для API
def base_url():
    return BASE_URL

@pytest.fixture(scope="function") # Создает временного пользователя и удаляет его после теста
def clean_user(base_url):
    user = User.generate_random_user()
    response = requests.post(f"{base_url}/api/auth/register", json=user.__dict__)
    yield user
    requests.delete(f"{base_url}/api/auth/user", headers={"Authorization": response.json()["accessToken"]})

@pytest.fixture(scope="function") # Создает пользователя с уникальным email и удаляет его после теста
def user_with_email(base_url):
    user = User.generate_random_user()
    response = requests.post(f"{base_url}/api/auth/register", json=user.__dict__)
    yield user
    requests.delete(f"{base_url}/api/auth/user", headers={"Authorization": response.json()["accessToken"]})


