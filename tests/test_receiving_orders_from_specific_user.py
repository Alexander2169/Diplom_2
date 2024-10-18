from utils import *
import allure


class TestReceivingOrdersFromSpecific(UserData): # Получение заказов конкретного пользователя

    def setUp(self):
        self.auth_token = get_auth_token() # Получаем токен авторизованного пользователя из api_actions.py

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders_authorized_user(self):
        headers = {
            "Authorization": self.auth_token
        }
        response = requests.get(ORDER_PEN, headers=headers)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIn('orders', data)
        self.assertIsInstance(data['orders'], list)
    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_orders_unauthorized_user(self):
        response = requests.get(ORDER_PEN, headers=headers)
        self.assertEqual(response.status_code, 401)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], "You should be authorised")



