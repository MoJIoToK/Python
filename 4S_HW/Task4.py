"""
4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

*Пример:* 
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

# from random import randint

# # natural_degree = int(input("Введите натуральную степень: "))


# def Create_Polinimial(natural_degree):
#     polinomial_size = natural_degree
#     factor = []

#     for i in range(0, polinomial_size+1):
#         factor.append(randint(-10, 10))

#     str_polinomial = []

#     if factor[0] != 0:
#         str_polinomial.insert(0, factor[0]) #коэффициенты перед членом равны элементу списка с тем же индексом
#                                             #например 3X^3 + 2X^2 + X + 2 -> [2, 1, 2, 3] 

#     for j in range(1, len(factor)):
#         if factor[j] != 0:
#             a = f'{factor[j]} * X ** {j}'
#             # str_polinomial.append(a)
#             str_polinomial.insert(0, a)
#         else:
#             continue

#     print(f'\nКоэффициенты многочлена   -   {factor}')
#     print(f"k = {natural_degree}   =>   {str_polinomial} = 0")
#     return factor


# file = open('4S_HW\Polinomial_1', 'w')

# natural_degree = int(input("Введите натуральную степень: "))
# factor1 = Create_Polinimial(natural_degree)
# file.write(str(factor1)[1:-1])

# file.close()


# file = open('4S_HW\Polinomial_2', 'w')

# factor2 = Create_Polinimial(natural_degree - randint(0, natural_degree-1))
# file.write(str(factor2)[1:-1])

# file.close()



from random import randint

n = int(input())
lst = [f'{randint(0, 100)}x**{n}']
for i in range(n - 1, -1 , -1):
    if randint(0, 10) > 4:
        lst.append(f'{randint(-100, 100)}x**{i}')

print(' '.join(lst))
