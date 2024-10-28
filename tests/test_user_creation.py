from helpers import *
from conftest import *

class TestUserCreation:  # Тесты для создания пользователей
    @allure.title('Проверка создания уникального пользователя')
    def test_create_unique_user(self, base_url):
        user = generate_random_user()  # Используем функцию из helpers
        response = create_user(user)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка создания уже зарегистрированного пользователя')
    def test_create_registered_user(self, base_url):
        # Сначала создаем пользователя
        user = generate_random_user()  # Используем функцию из helpers
        create_user(user)  # Регистрация пользователя

        # Теперь пробуем зарегистрировать его снова
        response = create_user(user)
        assert response.status_code == 403
        response_data = response.json()
        assert response_data["success"] is False
        assert "message" in response_data  # Проверяем наличие сообщения об ошибке

    @allure.title('Проверка создания пользователя без email')
    def test_create_user_without_email(self, base_url):
        user = generate_random_user()  # Используем функцию из helpers
        user.email = None
        response = create_user(user)
        assert response.status_code == 403
        response_data = response.json()
        assert response_data["success"] is False
        assert "message" in response_data  # Проверяем наличие сообщения об ошибке






