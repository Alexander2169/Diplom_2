import allure
from helpers import create_user
from conftest import *

class TestUserCreation: # Тесты для создания пользователей
    @allure.title('Проверка создания уникального пользователя')
    def test_create_unique_user(self, base_url):
        user = User.generate_random_user()
        response = create_user(user)
        assert response.status_code == 200
        assert response.json()["success"] is True
    @allure.title('Проверка создания уже зарегистрированного пользователя')
    def test_create_registered_user(self, user_with_email, base_url):
        response = create_user(user_with_email)
        assert response.status_code == 403
        assert response.json()["success"] is False
    @allure.title('Проверка создания пользователя без email')
    def test_create_user_without_email(self, base_url):
        user = User.generate_random_user()
        user.email = None
        response = create_user(user)
        assert response.status_code == 403
        assert response.json()["success"] is False


