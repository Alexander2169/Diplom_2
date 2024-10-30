import pytest
from helpers import generate_random_user

@pytest.fixture(scope="function")  # Создает временного пользователя
def clean_user():
    return generate_random_user()

@pytest.fixture(scope="function")  # Создает пользователя с уникальным email
def user_with_email():
    return generate_random_user()





