"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт 
сумму элементов списка, стоящих на нечётной позиции.

Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

test_list = []

# Стало:
test_list = list(map(int, input("Введите числа через пробел: ").split()))

# Было:
# for i in input("Введите числа через пробел: ").split():
#     test_list.append(int(i))

# Стало:
def Sum_Number(list_1):
    list_result = []
    sum = 0
    for i, element in enumerate(list_1):
        if i % 2 != 0:
            sum += element
            list_result.append(element)
    return sum, list_result

# Было:
# def Sum_Number(list_1):
#     list_result = []
#     sum = 0
#     for i in range(0, len(list_1)):
#         if i % 2 != 0:
#             sum += list_1[i]
#             list_result.append(list_1[i])
#     return sum, list_result

a = Sum_Number(test_list)
print(f"{test_list} -> на нечётных позициях элементы {a[1:len(a)]}, ответ {a[0]}")