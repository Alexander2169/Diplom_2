import allure
from helpers import *
from conftest import *

class TestUserCreation:  # Тесты для создания пользователей
    @allure.title('Проверка создания уникального пользователя')
    def test_create_unique_user(self, base_url):
        user = User.generate_random_user()
        response = create_user(user)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка создания уже зарегистрированного пользователя')
    def test_create_registered_user(self, base_url):
        # Сначала создаем пользователя
        user = User.generate_random_user()
        create_user(user)  # Регистрация пользователя

        # Теперь пробуем зарегистрировать его снова
        response = create_user(user)
        assert response.status_code == 403
        assert response.json()["success"] is False

    @allure.title('Проверка создания пользователя без email')
    def test_create_user_without_email(self, base_url):
        user = User.generate_random_user()
        user.email = None
        response = create_user(user)
        assert response.status_code == 403
        assert response.json()["success"] is False




