"""
4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.
"""

print("Введите число N: ")
num = int(input())

print("Введите первый множитель: ")
multiplier = int(input())

print("Введите второй множитель: ")
multiplicand = int(input())

list_1 = []
product = 1

for i in range(-num, num + 1):
    list_1.append(i)

product = list_1[multiplier] * list_1[multiplicand]

print(f"Для n = {num}: {list_1} -> {product} ")
