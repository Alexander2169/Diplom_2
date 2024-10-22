from helpers import *
from conftest import *


class TestUserUpdate:
    def test_update_email_with_auth(self, clean_user, base_url):
        response = login_user(clean_user)
        token = response.json()["accessToken"]

        # Уникальный email
        updated_email = f"{clean_user.email.split('@')[0]}_updated@mail.ru"
        clean_user.email = updated_email

        response = update_user(clean_user, token)
        print(f"Response for email update: {response.status_code}, {response.json()}")  # Логирование
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == updated_email

    def test_update_name_with_auth(self, clean_user, base_url):
        response = login_user(clean_user)
        token = response.json()["accessToken"]

        updated_name = "NewName"
        clean_user.name = updated_name

        response = update_user(clean_user, token)
        print(f"Response for name update: {response.status_code}, {response.json()}")  # Логирование
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["name"] == updated_name

    def test_update_user_without_auth_email(self, base_url):
        updated_user = User.generate_random_user()
        updated_user.email = "new_email@example.com"

        response = update_user(updated_user, "")
        print(f"Response for email update without auth: {response.status_code}, {response.json()}")  # Логирование
        assert response.status_code == 401
        assert response.json()["success"] is False

    def test_update_user_without_auth_name(self, base_url):
        updated_user = User.generate_random_user()
        updated_user.name = "NewName"

        response = update_user(updated_user, "")
        print(f"Response for name update without auth: {response.status_code}, {response.json()}")  # Логирование
        assert response.status_code == 401
        assert response.json()["success"] is False





