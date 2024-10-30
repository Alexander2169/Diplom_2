from api_requests import *
from helpers import *

class TestUserUpdate:  # Тесты для обновления данных пользователей
    @allure.title('Проверка обновления email с авторизацией')
    def test_update_email_with_auth(self):
        # Сначала создаем пользователя
        user = generate_random_user()  # Используем функцию из helpers
        create_user(user)  # Регистрация пользователя

        # Теперь пробуем войти
        response = login_user(user)
        assert response.status_code == 200, "Login failed"

        token = response.json().get("accessToken")
        assert token is not None, "Access token is missing"

        updated_email = f"{user.email.split('@')[0]}_updated@mail.ru"
        user.email = updated_email
        response = update_user(user, token)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == updated_email

    @allure.title('Проверка обновления имени с авторизацией')
    def test_update_name_with_auth(self):
        # Сначала создаем пользователя
        user = generate_random_user()  # Используем функцию из helpers
        create_user(user)  # Регистрация пользователя

        # Теперь пробуем войти
        response = login_user(user)
        assert response.status_code == 200, "Login failed"

        token = response.json().get("accessToken")
        assert token is not None, "Access token is missing"

        updated_name = "NewName"
        user.name = updated_name
        response = update_user(user, token)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["name"] == updated_name

    @allure.title('Проверка обновления email без авторизации')
    def test_update_user_without_auth_email(self):
        updated_user = generate_random_user()  # Используем функцию из helpers
        updated_user.email = "new_email@mail.ru"
        response = update_user(updated_user, "")
        assert response.status_code == 401
        response_data = response.json()
        assert response_data["success"] is False
        assert "message" in response_data  # Проверяем наличие сообщения об ошибке

    @allure.title('Проверка обновления имени без авторизации')
    def test_update_user_without_auth_name(self):
        updated_user = generate_random_user()  # Используем функцию из helpers
        updated_user.name = "NewName"
        response = update_user(updated_user, "")
        assert response.status_code == 401
        response_data = response.json()
        assert response_data["success"] is False
        assert "message" in response_data  # Проверяем наличие сообщения об ошибке








