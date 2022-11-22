"""2.Напишите программу, которая на вход принимает 
5 чисел и находит максимальное из них.
    Примеры:
    
    - 1, 4, 8, 7, 5 -> 8
    - 78, 55, 36, 90, 2 -> 90
"""
# Первый вариант
count = 1
list_numbers = []
for i in range(1, 6):
    number = int(input(f'Введите число {i}: '))
    list_numbers.append(number)  # добавление в конец

print(list_numbers)
max_number = list_numbers[0]
for item in list_numbers:
    if max_number < item:
        max_number = item

print(f'Минимальное число {max_number}')

# Второй вариант
a = int(input('введите число a'))
b = int(input('введите число b'))
c = int(input('введите число c'))
d = int(input('введите число d'))
e = int(input('введите число e'))

print(max(a, b, c, d, e))

# Третий вариант
max_number = float('-inf')

for i in range(1, 6):
    number = int(input(f'Введите число {i}: '))
    if number > max_number:
        max_number = number

print(max_number)
