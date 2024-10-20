from utils import *
import allure

class TestCreateOrder(UserData):  # Класс для тестирования создания заказа

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_with_authorization_and_ingredients(self):
        ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]
        self.authorize_user()  # Убедитесь, что пользователь авторизован
        response = self.user_client.create_order(self.token, ingredients)
        # Ожидаем 200, если заказ успешно создан
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get("success"))

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorization(self):
        ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]
        response = self.user_client.create_order(None, ingredients)  # Передаем None для токена
        # Ожидаем 401, если запрос без авторизации
        self.assertEqual(response.status_code, 401)
        self.assertFalse(response.json().get("success"))

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        self.authorize_user()  # Убедитесь, что пользователь авторизован
        response = self.user_client.create_order(self.token, [])  # Передаем пустой список
        # Ожидаем 400, если не переданы ингредиенты
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.json().get("success"))
        self.assertEqual(response.json().get("message"), "Ingredient ids must be provided")

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredient_hash(self):
        self.authorize_user()  # Убедитесь, что пользователь авторизован
        ingredients = ["invalid_hash_1", "invalid_hash_2"]
        response = self.user_client.create_order(self.token, ingredients)
        # Ожидаем 500, если передан невалидный хеш ингредиента
        self.assertEqual(response.status_code, 500)



