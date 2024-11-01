import allure
from api.api_requests import ApiRequests
from helpers import generate_random_user

class TestUserUpdate:  # Тесты для обновления данных пользователей
    @allure.title('Проверка обновления email с авторизацией')
    def test_update_email_with_auth(self):
        # Сначала создаем пользователя
        user = generate_random_user()
        ApiRequests.create_user(user)
        response = ApiRequests.login_user(user)
        token = response.json().get("accessToken")
        updated_email = f"{user['email'].split('@')[0]}_updated@mail.ru"
        user["email"] = updated_email  # Обновляем email
        response = ApiRequests.update_user(user, token)

        assert response.status_code == 200 and response.json()["success"] is True and response.json()["user"]["email"] == updated_email

    @allure.title('Проверка обновления имени с авторизацией')
    def test_update_name_with_auth(self):
        # Сначала создаем пользователя
        user = generate_random_user()
        ApiRequests.create_user(user)
        response = ApiRequests.login_user(user)
        token = response.json().get("accessToken")
        updated_name = "NewName"
        user["name"] = updated_name  # Обновляем имя
        response = ApiRequests.update_user(user, token)

        assert response.status_code == 200 and response.json()["success"] is True and response.json()["user"]["name"] == updated_name

    @allure.title('Проверка обновления email без авторизации')
    def test_update_user_without_auth_email(self):
        updated_user = generate_random_user()
        updated_user["email"] = "new_email@mail.ru"
        response = ApiRequests.update_user(updated_user, "")
        response_data = response.json()  # Парсим ответ

        assert response.status_code == 401 and response_data["success"] is False and "message" in response_data

    @allure.title('Проверка обновления имени без авторизации')
    def test_update_user_without_auth_name(self):
        updated_user = generate_random_user()
        updated_user["name"] = "NewName"
        response = ApiRequests.update_user(updated_user, "")
        response_data = response.json()  # Парсим ответ

        assert response.status_code == 401 and response_data["success"] is False and "message" in response_data










