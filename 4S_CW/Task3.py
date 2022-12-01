"""
1. Задайте строку из набора чисел. Напишите программу,
    которая покажет большее и меньшее число.
    В качестве символа-разделителя используйте пробел.
"""

test_list = []

for i in input("Введите числа через пробел: ").split():
    test_list.append(int(i))

min = test_list[0]
max = test_list[0]

for i in range(1, len(test_list)):
    if max > test_list[i]:
        if min > test_list[i]:
            min = test_list[i]
    else:
        max = test_list[i]

print(max, min)

#
test_list = []
for i in input("Введите числа через пробел: ").split():
    test_list.append(int(i))

min = test_list[0]
max = test_list[0]

for i in test_list:
    if i > max:
        max = i
    if i < min:
        min = i

print(min, max)
