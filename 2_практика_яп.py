# ===== 1. ПРОСТОЙ ДЕКОРАТОР ЛОГИРОВАНИЯ =====

def logger(func):
    # Создаем декоратор - функцию, которая принимает другую функцию
    def wrapper(a, b=None):
        if b is None:
            print(f"Вызов функции {func.__name__} с аргументом: {a}")
        else:
            print(f"Вызов функции {func.__name__} с аргументами: {a} и {b}")

        # Вызываем оригинальную функцию
        if b is None:
            result = func(a)  # Для функции с одним аргументом
        else:
            result = func(a, b)  # Для функции с двумя аргументами

        # После выполнения функции
        print(f"Функция {func.__name__} вернула: {result}")

        return result

    return wrapper


# Функция сложения
@logger
def add(a, b):
    return a + b


# Функция деления
@logger
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b


# Функция приветствия
@logger
def greet(name):
    return f"Привет, {name}!"


# ===== 2. ПРОСТОЙ ДЕКОРАТОР ДОСТУПА =====

def require_role(allowed_roles):
    # Декоратор с параметром - принимает список разрешенных ролей
    def decorator(func):
        # Вторая функция - принимает оригинальную функцию
        def wrapper(user):
            # Проверяем роль пользователя
            user_role = user['role']
            user_name = user['name']

            # Если роль пользователя есть в списке разрешенных
            if user_role in allowed_roles:
                # Выполняем функцию
                return func(user)
            else:
                print(f"Доступ запрещён пользователю {user_name}")
                return None

        return wrapper

    return decorator


# Функция удаления базы данных (только для админов)
@require_role(['admin'])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")
    return "Успешно удалено"


# Функция изменения настроек (для админов и менеджеров)
@require_role(['admin', 'manager'])
def edit_settings(user):
    print(f"Настройки изменены пользователем {user['name']}")
    return "Настройки изменены"


# ===== ТЕСТИРУЕМ КОД =====

print("=== ТЕСТ ДЕКОРАТОРА ЛОГИРОВАНИЯ ===")
print("\n1. Тест сложения:")
add(2, 9)

print("\n2. Тест деления:")
divide(16, 2)

print("\n3. Тест деления на ноль:")
divide(10, 0)

print("\n4. Тест приветствия:")
greet("Екатерина")

print("\n=== ТЕСТ ДЕКОРАТОРА ДОСТУПА ===")

# Создаем пользователей
user1 = {'name': 'Анна', 'role': 'admin'}
user2 = {'name': 'Кристина', 'role': 'manager'}
user3 = {'name': 'Ольга', 'role': 'user'}

print("\nПользователь Анна (admin):")
delete_database(user1)
edit_settings(user1)

print("\nПользователь Кристина (manager):")
delete_database(user2)
edit_settings(user2)

print("\nПользователь Ольга (user):")
delete_database(user3)
edit_settings(user3)
