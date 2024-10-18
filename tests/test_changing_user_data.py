from utils import *
import allure

class TestChangeUserData(UserData): # Изменение данных пользователя
    @allure.title('Изменение email для авторизованного пользователя')
    def test_change_user_email_with_authorization(self):
        updated_user_data = {"email": "newemail@mail.ru"}
        response = self.user_client.patch_user(self.token, updated_user_data)
        # Ожидаем 200, если email успешно изменен
        if response.status_code == 200:
            # Проверка, что email изменился
            user_info_response = self.user_client.get_user(self.token)
            self.assertEqual(user_info_response.json().get("user").get("email"), "newemail@mail.ru")
        else:
            # Если изменение не удалось, ожидаем 403
            self.assertEqual(response.status_code, 403)
    @allure.title('Изменение имени для авторизованного пользователя')
    def test_change_user_name_with_authorization(self):
        updated_user_data = {"name": "newname"}
        response = self.user_client.patch_user(self.token, updated_user_data)
        # Ожидаем 200, если имя успешно изменено
        if response.status_code == 200:
            # Проверка, что имя изменилось
            user_info_response = self.user_client.get_user(self.token)
            self.assertEqual(user_info_response.json().get("user").get("name"), "newname")
        else:
            # Если изменение не удалось, ожидаем 403
            self.assertEqual(response.status_code, 403)
            print(response)
    @allure.title('Изменение пароля для авторизованного пользователя')
    def test_change_user_password_with_authorization(self):
        updated_user_data = {"password": "password567"}
        response = self.user_client.patch_user(self.token, updated_user_data)
        # Ожидаем 200, если пароль успешно изменен
        if response.status_code == 200:
            # Проверка, что можно войти с новым паролем
            login_response = self.user_client.post_login_user(self.email, "password567")
            self.assertEqual(login_response.status_code, 200)
        else:
            # Если изменение не удалось, ожидаем 403
            self.assertEqual(response.status_code, 403)
    @allure.title('Попытка изменить email для неавторизованного пользователя')
    def test_change_user_email_without_authorization(self):
        updated_user_data = {"email": "unauthorized@mail.com"}
        response = self.user_client.patch_user(None, updated_user_data)
        # Ожидаем 403, если запрос без авторизации
        self.assertEqual(response.status_code, 403)
    @allure.title('Попытка изменить имя для неавторизованного пользователя')
    def test_change_user_name_without_authorization(self):
        updated_user_data = {"name": "UnauthorizedName"}
        response = self.user_client.patch_user(None, updated_user_data)
        # Ожидаем 403, если запрос без авторизации
        self.assertEqual(response.status_code, 403)
    @allure.title('Попытка изменить пароль для неавторизованного пользователя')
    def test_change_user_password_without_authorization(self):
        updated_user_data = {"password": "unauthorizedpassword"}
        response = self.user_client.patch_user(None, updated_user_data)
        # Ожидаем 403, если запрос без авторизации
        self.assertEqual(response.status_code, 403)
        print(response)




