import allure
from api_requests import ApiRequests
from helpers import generate_random_user

class TestOrderRetrieval:  # Тесты для получения заказов
    @allure.title('Проверка получения заказов авторизованным пользователем')
    def test_get_orders_as_authorized_user(self):
        clean_user = generate_random_user()  # Создаем временного пользователя
        # Сначала зарегистрируем пользователя
        registration_response = ApiRequests.create_user(clean_user)
        assert registration_response.status_code == 200, "User registration failed"

        # Теперь попробуем войти
        response = ApiRequests.login_user(clean_user)
        assert response.status_code == 200, "Login failed"

        token = response.json().get("accessToken")
        assert token is not None, "Access token is missing"

        response = ApiRequests.get_orders(token)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка получения заказов неавторизованным пользователем')
    def test_get_orders_as_unauthorized_user(self):
        response = ApiRequests.get_orders("")
        assert response.status_code == 401
        response_data = response.json()  # Парсим ответ
        assert response_data["success"] is False
        assert "message" in response_data  # Проверяем наличие сообщения об ошибке






