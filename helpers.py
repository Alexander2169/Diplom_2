import random
import string
import allure

@allure.step("Генерирует случайного пользователя")
def generate_random_user():  # Генерирует случайного пользователя
    email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@mail.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    name = ''.join(random.choices(string.ascii_letters, k=7))
    return {
        "email": email,
        "password": password,
        "name": name
    }










