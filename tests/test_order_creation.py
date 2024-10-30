import allure
from api_requests import ApiRequests
from helpers import generate_random_user
from data import *

class TestOrderCreation:  # Тесты для создания заказов
    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_with_auth(self):
        clean_user = generate_random_user()
        ApiRequests.create_user(clean_user)
        response = ApiRequests.login_user(clean_user)
        token = response.json().get("accessToken")
        ingredient_ids = INGREDIENTS.INGREDIENT_IDS
        response = ApiRequests.create_order(ingredient_ids, token)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_without_auth(self):
        ingredient_ids = INGREDIENTS.INGREDIENT_IDS
        response = ApiRequests.create_order(ingredient_ids, "")

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        clean_user = generate_random_user()
        ApiRequests.create_user(clean_user)
        response = ApiRequests.login_user(clean_user)
        token = response.json().get("accessToken")
        # Пытаемся создать заказ без ингредиентов
        response = ApiRequests.create_order([], token)
        response_data = response.json()  # Парсим ответ

        assert response.status_code == 400 and response_data["success"] is False and "message" in response_data

    @allure.title('Проверка создания заказа с неверным ID ингредиента')
    def test_create_order_with_wrong_ingredient_hash(self):
        clean_user = generate_random_user()
        ApiRequests.create_user(clean_user)
        response = ApiRequests.login_user(clean_user)
        token = response.json().get("accessToken")
        ingredient_ids = ['61c0c5a71d1f088107773887']  # Неправильный ID
        response = ApiRequests.create_order(ingredient_ids, token)
        response_data = response.json()  # Парсим ответ

        assert response.status_code == 400 and response_data["success"] is False and "message" in response_data










