import requests
from requests.auth import HTTPBasicAuth
import unittest
from hamcrest import assert_that, is_
from allure import description, title

class ChangeUserTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://stellarburgers.nomoreparties.site"
        self.name = "Izum"
        self.email = "Izum057436@yandex.ru"
        self.password = "GHkdjd68362"
        self.user_client = UserClient()
        self.user = User(self.name, self.email, self.password)
        UserClient.post_create_new_user(self.user)
        self.access_token = UserClient.check_request_auth_login(self.user).json().get("accessToken")

        self.modified_name = "DGHsan"
        self.modified_email = "DGHann@yandex.ru"
        self.modified_password = "1645sv"
        self.change_user = User()

    @title("Изменение имени пользователя с авторизацией.")
    @description("Успешное изменение имени пользователя с авторизацией.")
    def test_change_user_name_with_authorization(self):
        self.change_user.set_name(self.modified_name)
        self.user.set_name(self.modified_name)
        response = self.user_client.send_patch_request_with_authorization_api_auth_user(self.change_user, self.access_token)
        response_data = response.json()
        assert_that(response.status_code, is_(200))
        assert_that(response_data.get("success"), is_(True))

    @title("Изменение email пользователя с авторизацией.")
    @description("Успешное изменение email пользователя с авторизацией.")
    def test_change_user_email_with_authorization(self):
        self.change_user.set_email(self.modified_email)
        self.user.set_email(self.modified_email)
        response = self.user_client.send_patch_request_with_authorization_api_auth_user(self.change_user, self.access_token)
        response_data = response.json()
        assert_that(response.status_code, is_(200))
        assert_that(response_data.get("success"), is_(True))

    @title("Изменение пароля пользователя с авторизацией.")
    @description("Успешное изменение пароля пользователя с авторизацией.")
    def test_change_user_password_with_authorization(self):
        self.change_user.set_password(self.modified_password)
        self.user.set_password(self.modified_password)
        response = self.user_client.send_patch_request_with_authorization_api_auth_user(self.change_user, self.access_token)
        self.user_client.check_success_response_auth_user(response, self.email, self.name)

    def tearDown(self):
        # Удаление созданного пользователя
        if self.access_token is not None:
            self.user_client.delete_user(self.access_token)



