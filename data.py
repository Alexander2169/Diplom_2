import random
import string

class User: # Содержит классы и методы для работы с данными пользователей
    def __init__(self, email, password, name): # Инициализирует объект пользователя с email, паролем и именем
        self.email = email
        self.password = password
        self.name = name

    @staticmethod
    def generate_random_user(): # Статический метод, который генерирует случайного пользователя с уникальным email и паролем
        email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@mail.ru"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        name = ''.join(random.choices(string.ascii_letters, k=7))
        return User(email, password, name)

class INGREDIENTS: # Список идентификаторов ингредиентов для заказов
    INGREDIENT_IDS = [
        '61c0c5a71d1f82001bdaaa73',
        '61c0c5a71d1f82001bdaaa6c',
    ]





