"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

number_10 = int(input("Введите число: "))
str_number = ''

while number_10 != 0:
    str_number = str(number_10 % 2) + str_number
    number_10 //= 2

print(str_number)

