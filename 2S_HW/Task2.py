"""
2 Напишите программу, которая принимает на вход число N и выдает набор произведений 
чисел от 1 до N.

*Пример:*
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
Запрещено использовать функцию factorial из библиотеки math
"""

print("Введите число N: ")
num = int(input())

prod = 1

for i in range(1, num + 1):
    prod *= int(i)

print(prod)


def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n


print()
print(factorial(num))
