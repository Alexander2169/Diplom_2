import allure
from helpers import *
from conftest import *

class TestUserLogin:  # Тесты для логина пользователей
    @allure.title('Проверка логина под существующим пользователем')
    def test_login_existing_user(self, base_url):
        # Сначала создаем пользователя
        user = generate_random_user()  # Используем функцию из helpers
        create_user(user)  # Регистрация пользователя

        # Теперь пробуем войти
        response = login_user(user)
        assert response.status_code == 200, "Login failed"
        assert response.json()["success"] is True

    @allure.title('Проверка логина с неверными данными')
    def test_login_with_wrong_credentials(self, base_url):
        user = generate_random_user()  # Используем функцию из helpers
        response = login_user(user)
        assert response.status_code == 401
        assert response.json()["success"] is False




