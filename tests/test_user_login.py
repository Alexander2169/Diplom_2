from utils import *

class UserTestsLogin(UserData): # Логин пользователя
    def test_login_existing_user(self): # Проверяем логин под существующим пользователем
        response = self.user_client.post_login_user(self.user.email, self.user.password)
        assert response.status_code == 200
        assert response.json().get("accessToken") is not None

    def test_login_with_invalid_credentials(self): # Проверяем логин с неверным логином и паролем
        response = self.user_client.post_login_user("invalid@mail.com", "wrongpassword")
        assert response.status_code == 401
        assert response.json().get("success") is False
        assert response.json().get("message") == "email or password are incorrect"