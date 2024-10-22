from helpers import *
from conftest import *
from data import INGREDIENTS

class TestOrderCreation:

    def test_create_order_with_auth(self, clean_user, base_url):
        response = login_user(clean_user)
        token = response.json()["accessToken"]
        ingredient_ids = INGREDIENTS.INGREDIENT_IDS
        response = create_order(ingredient_ids, token)
        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_create_order_without_auth(self, base_url):
        ingredient_ids = INGREDIENTS.INGREDIENT_IDS
        response = create_order(ingredient_ids, "")
        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_create_order_without_ingredients(self, clean_user, base_url):
        response = login_user(clean_user)
        token = response.json()["accessToken"]
        response = create_order([], token)
        assert response.status_code == 400
        assert response.json()["success"] is False

    def test_create_order_with_wrong_ingredient_hash(self, clean_user, base_url):
        response = login_user(clean_user)
        token = response.json()["accessToken"]
        ingredient_ids = ['61c0c5a71d1f088107773887']  # Неправильный ID
        response = create_order(ingredient_ids, token)
        assert response.status_code == 400
        assert response.json()["success"] is False
