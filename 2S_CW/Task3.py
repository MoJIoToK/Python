"""
3. Напишите программу, в которой пользователь будет задавать две строки, 
   а программа - определять количество вхождений одной строки в другой.

s1 = 'aaababaewfwef'
s2 = 'aba'

print(s1.count(s2))
"""
print('Введите первую строку: ')
first_str = str(input())

print('Введите вторую строку: ')
second_str = str(input())
count = 0


for i in range(0, len(first_str)):
    text = i+len(second_str)
    if second_str == text:
        count = count + 1
"""
print('Введите первую строку: ')

string_1 = input()

print('Введите вторую строку: ')

string_2 = input()

count = 0

for i in range(0, len(string_1) - 1):
    text = string_1[i:i + len(string_2)]
    if text == string_2:
        count = count + 1
print(count)
"""
"""
count = 0

for i in range(len(str1) - (len(str2) - 1)):
    if str2 == str1[i:i+len(str2)]:
        count += 1


print(f"Вторая строка входит в первую {count} раз(а).")
"""

"""
for i in range(len(string_1)):
    if string_1[i:i+len(string_2)] == string_2:
        count+= 1
print(count)
"""

print(count)
