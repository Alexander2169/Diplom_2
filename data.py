import random
import string

class User:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    @staticmethod
    def generate_random_user():
        email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@example.com"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        name = ''.join(random.choices(string.ascii_letters, k=7))
        return User(email, password, name)

class INGREDIENTS:
    INGREDIENT_IDS = [
        '61c0c5a71d1f82001bdaaa73',  # Space краторный бургер
        '61c0c5a71d1f82001bdaaa6c',  # Другой ингредиент
        # Добавьте другие идентификаторы ингредиентов, если необходимо
    ]





