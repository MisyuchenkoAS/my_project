print('Hello, GitHub!') 

# 0. Генерация списка случайных чисел
numbers = [random.randint(-50, 50) for _ in range(10)]
print("Случайные числа:", numbers)

# 1. Чётные элементы
even_numbers = [num for num in numbers if num % 2 == 0]
print("Чётные элементы:", even_numbers)

# 2. Максимум и минимум
print("Максимум:", max(numbers))
print("Минимум:", min(numbers))

# 3. Ввод и сортировка
user_list = []
for _ in range(5):
    user_list.append(int(input("Введите число: ")))
user_list.sort()
print("Отсортированный список:", user_list)

# 4. Удаление дубликатов
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print("Без дубликатов:", unique_list)

# 5. Обмен первого и последнего
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("После обмена первого и последнего элемента:", numbers)

#Словари
#1. Средний балл студентов
grades = {"Анна": 91, "Мария": 86, "Иван": 78}
average = sum(grades.values()) / len(grades)
print("Средний балл:", average)