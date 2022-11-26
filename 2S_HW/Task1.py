"""
1 Напишите программу, которая принимает на вход вещественное число и показывает 
сумму его цифр.

*Пример:*
- 6782 -> 23
- 0.56 -> 11
"""

print("Введите вещественное число: ")
num = input()

sum = 0

for i in num:
    if i.isdigit():
        sum += int(i)

print(sum)

# num = '0.56'
# for i in num:
#     print(i)
#     if i.isdigit():
#         sum = sum + int(i)

# print(sum)  
