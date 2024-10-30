import random
import string
import allure

class User:  # Содержит классы и методы для работы с данными пользователей
    def __init__(self, email, password, name):  # Инициализирует объект пользователя с email, паролем и именем
        self.email = email
        self.password = password
        self.name = name

@allure.step("Генерирует случайного пользователя")
def generate_random_user():  # Генерирует случайного пользователя
    email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@mail.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    name = ''.join(random.choices(string.ascii_letters, k=7))
    return User(email, password, name)









