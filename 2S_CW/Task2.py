"""
2. Для натурального n создать список, 
   состоящий из элементов последовательности 3n + 1.
    
    *Пример:*
        - Для n = 4: [1, 4, 7, 10, 13] 
"""
print('Введите число N: ')

number = int(input())
list_example = []

for i in range(0, number + 1):
    list_example.append(3 * i + 1)

print(list_example)
