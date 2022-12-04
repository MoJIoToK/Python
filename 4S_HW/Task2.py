"""
2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

*Пример*
- при N=236     ->        [2, 2, 59]
"""

res = []
digit = 2

number_res = number = int(input("Введите число: "))

while digit * digit <= number:
    if number % digit == 0:
        res.append(digit)
        number //= digit
    else:
        digit += 1
if number > 1:
    res.append(number)

print(f"\nПри N = {number_res}   ->   {res}\n")