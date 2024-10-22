# базовый URL и эндпоинты API
BASE_URL = "https://stellarburgers.nomoreparties.site"

# Эндпоинт для регистрации нового пользователя
USER_REGISTER = f'{BASE_URL}/api/auth/register'  # Регистрация пользователя

# Эндпоинт для входа в систему
USER_LOGIN = f'{BASE_URL}/api/auth/login'  # Логин пользователя

# Эндпоинт для обновления данных пользователя
USER_UPDATE = f'{BASE_URL}/api/auth/user'  # Обновление данных пользователя

# Эндпоинт для создания нового заказа
ORDER_CREATE = f'{BASE_URL}/api/orders'  # Создание заказа

# Эндпоинт для получения заказов пользователя
ORDER_GET = f'{BASE_URL}/api/orders'  # Получение заказов пользователя