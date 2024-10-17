from conftest import *
class TestCreateUser:

    # Проверяем, что можно создать уникального пользователя
    def test_create_unique_user(self, unique_user):
        response = requests.post(AUTH_REGISTER_URL, json=unique_user)
        assert response.status_code == 200
        assert response.json()["success"] is True

    # Проверяем, что нельзя зарегистрировать пользователя с уже существующим адресом электронной почты
    def test_create_registered_user(self, unique_user):
        response = requests.post(AUTH_REGISTER_URL, json=unique_user)
        assert response.status_code == 403
        assert response.json()["success"] is False

    # Проверяем, что нельзя зарегистрировать пользователя, если отсутствует одно из обязательных полей "name"
    def test_create_user_with_one_blank_field(self):
        user_data = {
            "email": "dadic2169@mail.ru",
            "password": "password777"

        }
        response = requests.post(AUTH_REGISTER_URL, json=user_data)
        assert response.status_code == 403
        assert response.json()["success"] is False
