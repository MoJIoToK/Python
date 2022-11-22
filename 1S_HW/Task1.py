'''1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
'''

# First variation
print('Введите число от 1 до 7 обозначающее день недели: ')
day = int(input())

if day == 1:
    print('Нет')
elif day == 2:
    print('Нет')
elif day == 3:
    print('Нет')
elif day == 4:
    print('Нет')
elif day == 5:
    print('Нет')
elif day == 6:
    print('Да')
elif day == 7:
    print('Да')
else:
    print('Неверно указан день! Попробуйте снова')

#Second variation
print()
print('Введите число от 1 до 7 обозначающее день недели: ')
day = int(input())

if day > 5 and day < 8:
    print('Да')
elif day < 6 and day > 0:
    print('Нет')
else:
    print('Неверно указан день! Попробуйте снова')
