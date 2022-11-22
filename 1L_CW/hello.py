value = None
a = 123
b = 1.23

# print(type(a))
# print(type(b))

value = 12334
# print(value)

s = "hello 'world"
s1 = 'hello "world'
s2 = 'hello \nworld'
# print(s)
# print(s1)
# print(s2)
# Комментарий делается с помощью #

# print (a,'-',b, '-',s,'-',s2)
# print ('{1} - {2} - {0}'.format(a,b,s))


# list = [1, 2, 3]
# col = ['hello', 1, 2, 4.5, True]
# print(list)
# print(col)


# print('A');
# a = float(input())
# print('B');
# b = float(input())

# print(a+b)10

# Арифметические операции
# a = +2  # унарный плюс
# b = 8
# c = a**b
# print(c)
# # ** - возведение в степень

# a = 1.3213
# b = 3
# c = round(a*b, 3)
# print(c)

# Логические операции
# a = 1 < 4 and 5 > 2
# print(a)

# b = 1 < 3 < 4 < 6
# print(a)

# func = 1
# T = 4
# x = 123
# print(func < T > (x))

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# # print(f)
# # print(2 in f)
# # print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции
# if, if-else

# a=int(input())
# b=int(input())

# if a>b:
#     print(a)
# else:
#     print (b)

# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted*10+(original%10)
#     original//= 10
#     print(original)
# else:
#     print('Хватит')

# for

# list=[1,2,3,4,10,5]
# for i in list:
#     print(i**2)

# for i in range(1, 10, 2):
#     print(i)


# Строки
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))  # 39
# print('ещё' in text)  # True
# print(text.isdigit())  # False
# print(text.islower())  # True
# print(text.replace('ещё', 'ЕЩЁ'))
# for c in text:
#     print(c)

# help(str)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])  # c
# print(text[1])  # ъ
# print(text[len(text)-1])  # к
# print(text[-5])  # б
# print(text[:])  # print(text)
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# text = text[2:9] + text[-5] + text[:2]  # ...

# Списки
# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)  # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)  # red green blue
# for e in colors:
#     print(e*2)  # redred greengreen blueblue
# colors.append('gray')  # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])  # True
# colors.remove('red')  # del colors[0] # удалить элемент

# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

print(f(1))  # Целое
print(f(2.3))  # 23
print(f(28))  # None
print(type(f(1)))  # str
print(type(f(2.3)))  # int
print(type(f(28)))  # NoneType
