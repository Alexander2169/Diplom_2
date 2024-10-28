import allure
from helpers import *
from data import INGREDIENTS
from conftest import *

class TestOrderCreation:  # Тесты для создания заказов
    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_with_auth(self, clean_user, base_url):
        # Сначала зарегистрируем пользователя
        registration_response = create_user(clean_user)
        assert registration_response.status_code == 200, "User registration failed"

        # Теперь попробуем войти
        response = login_user(clean_user)
        assert response.status_code == 200, "Login failed"

        token = response.json().get("accessToken")
        assert token is not None, "Access token is missing"

        ingredient_ids = INGREDIENTS.INGREDIENT_IDS
        response = create_order(ingredient_ids, token)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_without_auth(self, base_url):
        ingredient_ids = INGREDIENTS.INGREDIENT_IDS
        response = create_order(ingredient_ids, "")
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self, clean_user, base_url):
        # Сначала зарегистрируем пользователя
        registration_response = create_user(clean_user)
        assert registration_response.status_code == 200, "User registration failed"

        # Теперь попробуем войти
        response = login_user(clean_user)
        assert response.status_code == 200, "Login failed"

        token = response.json().get("accessToken")
        assert token is not None, "Access token is missing"

        response = create_order([], token)
        assert response.status_code == 400
        assert response.json()["success"] is False

    @allure.title('Проверка создания заказа с неверным ID ингредиента')
    def test_create_order_with_wrong_ingredient_hash(self, clean_user, base_url):
        # Сначала зарегистрируем пользователя
        registration_response = create_user(clean_user)
        assert registration_response.status_code == 200, "User registration failed"

        # Теперь попробуем войти
        response = login_user(clean_user)
        assert response.status_code == 200, "Login failed"

        token = response.json().get("accessToken")
        assert token is not None, "Access token is missing"

        ingredient_ids = ['61c0c5a71d1f088107773887']  # Неправильный ID
        response = create_order(ingredient_ids, token)
        assert response.status_code == 400
        assert response.json()["success"] is False




