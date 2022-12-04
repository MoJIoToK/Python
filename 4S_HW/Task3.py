"""
3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
исходной последовательности.

*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]
"""

test_list = []
temp_set_1 = []
#res = {}

for i in input("Введите числа через пробел: ").split():
    test_list.append(int(i))


for i in range(0, len(test_list)-1):
    for j in range(i+1, len(test_list)):
        if test_list[i] == test_list[j]:
            temp_set_1.append(test_list[i])


res = set(set(test_list).difference(set(temp_set_1)))

print(f"При {test_list}   ->   {res}")

#print(test_set, set(test_set))
