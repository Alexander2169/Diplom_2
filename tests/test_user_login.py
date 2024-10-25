import allure
from helpers import login_user
from conftest import *

class TestUserLogin: # Тесты для логина пользователей
    @allure.title('Проверка логина под существующим пользователем')
    def test_login_existing_user(self, clean_user, base_url):
        response = login_user(clean_user)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка логина с неверными данными')
    def test_login_with_wrong_credentials(self, base_url):
        user = User.generate_random_user()
        response = login_user(user)
        assert response.status_code == 401
        assert response.json()["success"] is False


