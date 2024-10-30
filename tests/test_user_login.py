import allure
from api.api_requests import ApiRequests
from helpers import generate_random_user


class TestUserLogin:  # Тесты для логина пользователей
    @allure.title('Проверка логина под существующим пользователем')
    def test_login_existing_user(self):
        # Сначала создаем пользователя
        user = generate_random_user()
        ApiRequests.create_user(user)
        response = ApiRequests.login_user(user)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Проверка логина с неверными данными')
    def test_login_with_wrong_credentials(self):
        user = generate_random_user()  #
        response = ApiRequests.login_user(user)
        response_data = response.json()  # Парсим ответ

        assert response.status_code == 401 and response_data["success"] is False and "message" in response_data







