"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний 
элемент, второй и предпоследний и т.д.

Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

test_list = []

for i in input("Введите числа через пробел: ").split():
    test_list.append(int(i))

print(test_list)


def Product_Numbers(list_1):
    list_result = []
    if len(list_1)/2 % 2 == 0:
        for i in range(0, int(len(list_1)/2)):
            list_result.append(list_1[i] * list_1[len(list_1)-1-i])
    else:
        for i in range(0, int(len(list_1)/2+1)):
            list_result.append(list_1[i] * list_1[len(list_1)-1-i])
    return list_result


a = Product_Numbers(test_list)
print(f"{test_list} => {a}")