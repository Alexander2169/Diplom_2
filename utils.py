from api_actions import *
import unittest

class UserData(unittest.TestCase):
    def setUp(self):
        self.name = "Alex"
        self.email = "dadic3333@mail.ru"
        self.password = "password"
        self.user_client = UserClient()
        self.user = User(self.name, self.email, self.password)
        self.token = None  # Здесь будет храниться токен для удаления пользователя

    def tearDown(self):
        if self.token:
            self.user_client.delete_user(self.token)


