"""
3. Задайте два числа. Напишите программу, которая найдёт НОК
   (наименьшее общее кратное) этих двух чисел.
"""

a, b = 3, 7
maxx = max(a, b)
i = maxx
while True:
    if i % a == 0 and i % b == 0:
        print(i)
        break
    i += maxx



dividing_list = []
for i in input("Введите два числа: ").split():
    dividing_list.append(int(i))

product = dividing_list[0] * dividing_list[1]
list1 = []
list2 = []

for i in range(dividing_list[0], product + 1, dividing_list[0]):
    list1.append(i)

for j in range(dividing_list[1], product + 1, dividing_list[1]):
    list2.append(j)

list3 = []

for k in list1:
    for l in list2:
        if k == l:
           list3.append(k)

print(list1)
print(list2)
print(list3[0])
