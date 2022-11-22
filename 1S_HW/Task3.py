'''
3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''

#First variation
print('Введите координату Х точки, отличную от нуля: ')
coordinate_X = int(input())

print('Введите координату Y точки, отличную от нуля: ')
coordinate_Y = int(input())

if coordinate_X !=0 and coordinate_Y !=0:
    if coordinate_X > 0 and coordinate_Y > 0:
        print('Четверть - 1')
    elif coordinate_X < 0 and coordinate_Y > 0:
        print('Четверть - 2')
    elif coordinate_X < 0 and coordinate_Y < 0:
        print('Четверть - 3')
    elif coordinate_X > 0 and coordinate_Y < 0:
        print('Четверть - 4')
else:
    print('Неверно введены значения')

#Second variation
list_coordinates = []
for i in range(1, 3):
    cooradinate = int(input(f'Введите число {i}: '))
    list_coordinates.append(cooradinate)  # добавление в конец
if list_coordinates[0] !=0 and list_coordinates[1] !=0:
    if list_coordinates[0] > 0 and list_coordinates[1] > 0:
        print('Четверть - 1')
    elif list_coordinates[0] < 0 and list_coordinates[1] > 0:
        print('Четверть - 2')
    elif list_coordinates[0] < 0 and list_coordinates[1] < 0:
        print('Четверть - 3')
    elif list_coordinates[0] > 0 and list_coordinates[1] < 0:
        print('Четверть - 4')
else:
    print('Неверно введены значения')


