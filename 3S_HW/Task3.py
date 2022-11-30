"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

"""
# First Variation
test_list = []
list_2 = []

for i in input("Введите числа через пробел: ").split():
    test_list.append(float(i))

for i in test_list:
    if i % 1 != 0:
        list_2.append(i % 1)

print(list_2)


def Difference_Numbers(list_1):
    min = list_1[0]
    max = list_1[0]
    for i in range(1, len(list_1)):
        if max > list_1[i]:
            if min > list_1[i]:
                min = list_1[i]
        else:
            max = list_1[i]
    result = max - min
    return result


a = Difference_Numbers(list_2)
print(f"{test_list} => {round(a,2)}")

# Second Variation
test_list = []

for i in input("Введите числа через пробел: ").split():
    test_list.append(float(i))

list_2 = []
for i in test_list:
    if i % 1 != 0:
        list_2.append(round(i % 1, 2))
print(max(list_2) - min(list_2))
