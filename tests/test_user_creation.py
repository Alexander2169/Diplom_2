import allure
from api.api_requests import ApiRequests
from helpers import generate_random_user


class TestUserCreation:  # Тесты для создания пользователей
    @allure.title('Проверка создания уникального пользователя')
    def test_create_unique_user(self):
        user = generate_random_user()
        response = ApiRequests.create_user(user)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Проверка создания уже зарегистрированного пользователя')
    def test_create_registered_user(self):
        # Сначала создаем пользователя
        user = generate_random_user()
        ApiRequests.create_user(user)
        response = ApiRequests.create_user(user)
        response_data = response.json()  # Парсим ответ
        #
        assert response.status_code == 403 and response_data["success"] is False and "message" in response_data

    @allure.title('Проверка создания пользователя без email')
    def test_create_user_without_email(self):
        user = generate_random_user()
        user["email"] = None
        response = ApiRequests.create_user(user)
        response_data = response.json()  # Парсим ответ

        assert response.status_code == 403 and response_data["success"] is False and "message" in response_data







