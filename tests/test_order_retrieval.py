import allure
from api.api_requests import ApiRequests
from helpers import generate_random_user

class TestOrderRetrieval:  # Тесты для получения заказов
    @allure.title('Проверка получения заказов авторизованным пользователем')
    def test_get_orders_as_authorized_user(self):
        clean_user = generate_random_user()
        ApiRequests.create_user(clean_user)
        response = ApiRequests.login_user(clean_user)
        token = response.json().get("accessToken")
        response = ApiRequests.get_orders(token)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Проверка получения заказов неавторизованным пользователем')
    def test_get_orders_as_unauthorized_user(self):
        response = ApiRequests.get_orders("")
        response_data = response.json()  # Парсим ответ

        assert response.status_code == 401 and response_data["success"] is False and "message" in response_data









