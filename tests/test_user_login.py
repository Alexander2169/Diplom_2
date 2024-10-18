from data import *

class UserTestsLogin(TestData, UserData):
    def test_login_existing_user(self):
        response = self.user_client.post_login_user(self.user.email, self.user.password)
        assert response.status_code == 200
        assert response.json().get("accessToken") is not None

    def test_login_with_invalid_credentials(self):
        response = self.user_client.post_login_user("invalid@mail.com", "wrongpassword")
        assert response.status_code == 401
        assert response.json().get("success") is False
        assert response.json().get("message") == "email or password are incorrect"