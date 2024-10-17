from data import *

class UserTestsCreation(UserData):

    def test_check_create_user(self):
        response = self.user_client.post_create_new_user(self.user)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json().get("accessToken") is not None
        assert response.json().get("refreshToken") is not None
        assert response.json().get("user").get("email") is not None
        assert response.json().get("user").get("name") is not None
        self.token = response.json().get("accessToken")  # Сохраним токен для удаления

    def test_check_registered_user(self):
        self.user_client.post_create_new_user(self.user)
        response = self.user_client.post_create_new_user(self.user)
        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == "User already exists"

    def test_create_user_without_name(self):
        self.user.email = self.email
        self.user.password = self.password
        response = self.user_client.post_create_new_user(self.user)
        self.user_client.check_failed_response_auth_register(response)

    def test_create_user_without_email(self):
        self.user.name = self.name
        self.user.password = self.password
        response = self.user_client.post_create_new_user(self.user)
        self.user_client.check_failed_response_auth_register(response)

    def test_create_user_without_password(self):
        self.user.email = self.email
        self.user.name = self.name
        response = self.user_client.post_create_new_user(self.user)
        self.user_client.check_failed_response_auth_register(response)

    def test_create_user_without_name_and_email(self):
        self.user.password = self.password
        response = self.user_client.post_create_new_user(self.user)
        self.user_client.check_failed_response_auth_register(response)

    def test_create_user_without_name_and_password(self):
        self.user.email = self.email
        response = self.user_client.post_create_new_user(self.user)
        self.user_client.check_failed_response_auth_register(response)

if __name__ == "__main__":
    unittest.main()
