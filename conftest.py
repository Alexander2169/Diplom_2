import pytest
from urls import BASE_URL
from helpers import generate_random_user

@pytest.fixture(scope="module")  # Возвращает базовый URL для API
def base_url():
    return BASE_URL

@pytest.fixture(scope="function")  # Создает временного пользователя
def clean_user(base_url):
    return generate_random_user()

@pytest.fixture(scope="function")  # Создает пользователя с уникальным email
def user_with_email(base_url):
    return generate_random_user()





