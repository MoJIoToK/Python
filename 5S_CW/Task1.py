#lst = [1, 2, -3, 44, -76]
#lst = [(1,8), (6,2), (4,2), (6,1)]

#def f1(x): return x * x

#f1 = lambda x: x * x

# print(max(lst,))

# print(max(lst))

#print(max(lst, key=lambda x: x[1]))


# a, b, c = map(int, input().split()) # распаковка
# print(a, b, c)


# items = list(map(int, input().split()))

# print(*items)


# a = int('1011', 2)
# print(a)

#Фильтры

# lst = [2, 33, 12, 34, 3, 13]

# a = filter(lambda x: x % 2 == 0, lst)

# print(*a)


#enumerate
# lst = [2, 33, 12, 34, 3, 13]

# for index, x in enumerate(lst):
#     print(index, x) # Распакованный кортеж, если написать for tup ... print(tup), то получим кортеж

# print(list(enumerate(lst)))  


# Пример с одним вариантом
# lst = []

# for x in range(-2, 7):
#     if x % 2 == 0:
#         lst.append(x * x)

# print(lst)

# lst1 = [x * x for x in range(-2, 7) if x % 2 == 0]
# print(lst1)

# Пример с двумя вариантами
lst = []

for x in range(-2, 7):
    if x % 2 == 0:
        lst.append(x * x)
    else:
        lst.append(x * x * x)

print(lst)

lst1 = [x * x if x % 2 == 0 else x * x * x for x in range(-2, 7)]
print(lst1)
