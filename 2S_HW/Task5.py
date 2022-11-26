"""
5 Реализуйте алгоритм перемешивания списка.
Из библиотеки random использовать можно только randint
"""

from random import randint

ran = randint(0, 10)
list_1 = []

for i in range(0, ran+1):
    list_1.append(randint(0, 10))


def Mix_List(list_original):
    list_copy = list_original
    for i in range(0, len(list_copy)):
        index_mix = randint(0, len(list_copy) - 1)
        temp = list_copy[i]
        list_copy[i] = list_copy[index_mix]
        list_copy[index_mix] = temp
    return list_copy


print(f"Исходный массив: {list_1}")
print(f"Перемещанный массив: {Mix_List(list_1)}")