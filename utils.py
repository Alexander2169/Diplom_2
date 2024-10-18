from api_actions import *
import unittest

class UserData(unittest.TestCase):
    def setUp(self):
        self.name = "Alex"
        self.email = "dadic9658@mail.ru"
        self.password = "password"
        self.user_client = UserClient()
        self.user = User(self.name, self.email, self.password)
        self.token = None  # Здесь будет храниться токен для удаления пользователя

    def tearDown(self):
        if self.token:
            self.user_client.delete_user(self.token)

    def authorize_user(self):
        response = self.user_client.post_create_new_user(self.user)
        if response.status_code == 200:
            login_response = self.user_client.post_login_user(self.email, self.password)
            self.token = login_response.json().get("accessToken")


