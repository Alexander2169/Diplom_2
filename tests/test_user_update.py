import allure
from helpers import *
from conftest import *


class TestUserUpdate: # Тесты для обновления данных пользователей
    @allure.title('Проверка обновления email с авторизацией')
    def test_update_email_with_auth(self, clean_user, base_url):
        response = login_user(clean_user)
        token = response.json()["accessToken"]

        # Уникальный email
        updated_email = f"{clean_user.email.split('@')[0]}_updated@mail.ru"
        clean_user.email = updated_email

        response = update_user(clean_user, token)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == updated_email
    @allure.title('Проверка обновления имени с авторизацией')
    def test_update_name_with_auth(self, clean_user, base_url):
        response = login_user(clean_user)
        token = response.json()["accessToken"]

        updated_name = "NewName"
        clean_user.name = updated_name

        response = update_user(clean_user, token)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["name"] == updated_name
    @allure.title('Проверка обновления email без авторизации')
    def test_update_user_without_auth_email(self, base_url):
        updated_user = User.generate_random_user()
        updated_user.email = "new_email@example.com"

        response = update_user(updated_user, "")
        assert response.status_code == 401
        assert response.json()["success"] is False
    @allure.title('Проверка обновления имени без авторизации')
    def test_update_user_without_auth_name(self, base_url):
        updated_user = User.generate_random_user()
        updated_user.name = "NewName"

        response = update_user(updated_user, "")
        assert response.status_code == 401
        assert response.json()["success"] is False





