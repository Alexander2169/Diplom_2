from utils import *
import allure

class UserTestsLogin(UserData): # Проверяем логин пользователя
    @allure.title('Проверяем логин под существующим пользователем')
    def test_login_existing_user(self):
        response = self.user_client.post_login_user(self.user.email, self.user.password)
        assert response.status_code == 200
        assert response.json().get("accessToken") is not None
    @allure.title('Проверяем логин с неверным логином и паролем')
    def test_login_with_invalid_credentials(self):
        response = self.user_client.post_login_user("invalid@mail.com", "wrongpassword")
        assert response.status_code == 401
        assert response.json().get("success") is False
        assert response.json().get("message") == "email or password are incorrect"