### Дипломный проект. Задание 2: Тестирование ручек API для Stellar Burgers.

### Проект для тестирования API Stellar Burgers имеет следующую структуру. 

DIPLOM_2/
│
├── conftest.py          # Конфигурация тестов и фикстуры
├── data.py              # Определение классов и методов для работы с пользователями
├── helpers.py           # Вспомогательные функции для работы с API
├── urls.py              # Определение базового URL и эндпоинтов API
│
└── tests/               # Папка с тестами
    ├── test_order_creation.py      # Тесты для создания заказов
    ├── test_order_retrieval.py     # Тесты для получения заказов
    ├── test_user_creation.py        # Тесты для создания пользователей
    ├── test_user_login.py           # Тесты для логина пользователей
    └── test_user_update.py          # Тесты для обновления данных пользователей

### Структура пректа

### 1. conftest.py - cодержит фикстуры для тестов, которые обеспечивают подготовку данных перед выполнением тестов.
*Фикстуры:*
  base_url" - возвращает базовый URL для API.
  clean_user - создает временного пользователя и удаляет его после теста.
  user_with_email - создает пользователя с уникальным email и удаляет его после теста.

### 2. data.py - содержит Классы и Методы для работы с данными пользователей.
*Класс User:*
  __init__(self, email, password, name) - инициализирует объект пользователя с email, паролем и именем.
  generate_random_user() - статический метод, который генерирует случайного пользователя с уникальным email и паролем.
*Класс INGREDIENTS:*
  INGREDIENT_IDS - список идентификаторов ингредиентов для заказов.

### 3. helpers.py
*Содержит функции для выполнения запросов к API.*
*Функции:*
  create_user(user) - создает пользователя через API.
  login_user(user) - логинит пользователя через API.
  update_user(user, token) - обновляет данные пользователя через API.
  create_order(ingredient_ids, token) - создает заказ с указанными ингредиентами.
  get_orders(token) - получает заказы пользователя.

### 4. urls.py
*Содержит базовый URL и эндпоинты API.*
*Константы:*
  BASE_URL - базовый URL для API.
  USER_REGISTER, USER_LOGIN, USER_UPDATE, ORDER_CREATE, ORDER_GET - эндпоинты для работы с пользователями и заказами.

### Описание тестов
### 1. test_user_creation.py - Тесты для создания пользователей.

  test_create_unique_user - проверяет создание уникального пользователя.
  test_create_registered_user - проверяет создание уже зарегистрированного пользователя.
  test_create_user_without_email - проверяет создание пользователя без email.

### 2. test_user_login.py - Тесты для логина пользователей.

  test_login_existing_user - проверяет логин под существующим пользователем.
  test_login_with_wrong_credentials - проверяет логин с неверными данными.

### 3. test_user_update.py - Тесты для обновления данных пользователей.

  test_update_email_with_auth - проверяет обновление email с авторизацией.
  test_update_name_with_auth - проверяет обновление имени с авторизацией.
  test_update_user_without_auth_email - проверяет обновление email без авторизации.
  test_update_user_without_auth_name - проверяет обновление имени без авторизации.

### 4. test_order_creation.py - Тесты для создания заказов.

  test_create_order_with_auth - проверяет создание заказа с авторизацией.
  test_create_order_without_auth - проверяет создание заказа без авторизации.
  test_create_order_without_ingredients - проверяет создание заказа без ингредиентов.
  test_create_order_with_wrong_ingredient_hash - проверяет создание заказа с неверным ID ингредиента.

### 5. test_order_retrieval.py - Тесты для получения заказов.

  test_get_orders_as_authorized_user - проверяет получение заказов авторизованным пользователем.
  test_get_orders_as_unauthorized_user - проверяет получение заказов неавторизованным пользователем.

### gitignore - файл, содержащий локальные файлы;
### README.md - файл, содержащий текстовую часть о проделанной работе; 
### requirements.txt - файл, содержащий список внешних зависимостей.

### Тесты для вывода из терминала - проверены командой: pytest -v.
### Команда для запуска с записью отчета в allure_results: `pytest tests --alluredir=allure_results`.









