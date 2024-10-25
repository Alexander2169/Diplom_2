import allure
from helpers import *
from conftest import *

class TestOrderRetrieval: # Тесты для получения заказов
    @allure.title('Проверка получения заказов авторизованным пользователем')
    def test_get_orders_as_authorized_user(self, clean_user, base_url):
        response = login_user(clean_user)
        token = response.json()["accessToken"]
        response = get_orders(token)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка получения заказов неавторизованным пользователем')
    def test_get_orders_as_unauthorized_user(self, base_url):
        response = get_orders("")
        assert response.status_code == 401
        assert response.json()["success"] is False

