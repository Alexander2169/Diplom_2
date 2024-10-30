from helpers import *
from conftest import *
from data import *

class TestOrderRetrieval:  # Тесты для получения заказов
    @allure.title('Проверка получения заказов авторизованным пользователем')
    def test_get_orders_as_authorized_user(self, clean_user):
        # Сначала зарегистрируем пользователя
        registration_response = create_user(clean_user)
        assert registration_response.status_code == 200, "User registration failed"

        # Теперь попробуем войти
        response = login_user(clean_user)
        assert response.status_code == 200, "Login failed"

        token = response.json().get("accessToken")
        assert token is not None, "Access token is missing"

        response = get_orders(token)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка получения заказов неавторизованным пользователем')
    def test_get_orders_as_unauthorized_user(self):
        response = get_orders("")
        assert response.status_code == 401
        response_data = response.json()  # Парсим ответ
        assert response_data["success"] is False
        assert "message" in response_data  # Проверяем наличие сообщения об ошибке




