import requests
from requests import Response
import unittest

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class UserClient:
    base_uri = "https://stellarburgers.nomoreparties.site"

    @staticmethod
    def post_create_new_user(user):
        response = requests.post(f"{UserClient.base_uri}/api/users",
                                 json={"email": user.email, "password": user.password, "name": user.name})
        return response

    @staticmethod
    def check_request_auth_login(user):
        response = requests.post(f"{UserClient.base_uri}/api/auth/login",
                                 json={"email": user.email, "password": user.password})
        return response

    @staticmethod
    def check_failed_response_auth_login(response):
        assert response.status_code != 200

    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": f"Bearer {access_token}"}
        requests.delete(f"{UserClient.base_uri}/api/users", headers=headers)

class LoginUserTests(unittest.TestCase):
    def setUp(self):
        self.name = "Alex"
        self.email = "dadic5555@mail.ru"
        self.password = "password"
        self.user_client = UserClient()
        self.user = User(self.name, self.email, self.password)

    def test_authorization(self):
        self.user_client.post_create_new_user(self.user)
        response = self.user_client.check_request_auth_login(self.user)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json().get("accessToken") is not None
        assert response.json().get("refreshToken") is not None
        assert response.json().get("user").get("email") is not None
        assert response.json().get("user").get("name") is not None

    def test_authorization_incorrect_login(self):
        self.user.email = "Hdnasjdhbajhnwjdnakljndj2783o127" + self.email
        response = self.user_client.check_request_auth_login(self.user)
        self.user_client.check_failed_response_auth_login(response)

    def test_authorization_incorrect_password(self):
        self.user.password = "6482HSVbsj" + self.password
        response = self.user_client.check_request_auth_login(self.user)
        self.user_client.check_failed_response_auth_login(response)

    def test_authorization_without_login(self):
        self.user.password = self.password
        response = self.user_client.check_request_auth_login(self.user)
        self.user_client.check_failed_response_auth_login(response)

    def test_authorization_without_password(self):
        self.user.email = self.email
        response = self.user_client.check_request_auth_login(self.user)
        self.user_client.check_failed_response_auth_login(response)

    def test_authorization_without_login_and_password(self):
        response = self.user_client.check_request_auth_login(self.user)
        self.user_client.check_failed_response_auth_login(response)

    def tearDown(self):
        response = self.user_client.check_request_auth_login(self.user)
        access_token = response.json().get("accessToken")
        if access_token is not None:
            self.user_client.delete_user(access_token)

if __name__ == "__main__":
    unittest.main()

