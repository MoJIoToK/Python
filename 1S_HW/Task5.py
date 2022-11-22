'''
5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними 
в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''

import math

#First variation
print('Введите координату Х точки A, отличную от нуля: ')
coordinate_Ax = int(input())

print('Введите координату Y точки A, отличную от нуля: ')
coordinate_Ay = int(input())

print('Введите координату Х точки B, отличную от нуля: ')
coordinate_Bx = int(input())

print('Введите координату Y точки B, отличную от нуля: ')
coordinate_By = int(input())

result = math.sqrt((coordinate_Ax - coordinate_Bx)**2 + (coordinate_Ay-coordinate_By)**2)

print(round(result, 2))

#Second variation
print()
list_coordinates = []
for i in range(1, 5):
    cooradinate = int(input(f'Введите число {i}: '))
    list_coordinates.append(cooradinate)  # добавление в конец
print(round(math.sqrt((list_coordinates[0] - list_coordinates[2])**2 + (list_coordinates[1]-list_coordinates[3])**2), 2))