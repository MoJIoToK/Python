"""
5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов 
могут отличаться.
"""

def Read_File(route):
    a = []
    file = open(route, 'r')
    for i in file.read().split(','):
        a.append(int(i))
    file.close()
    print(f"Коэффициенты многочлена - {a}\n")
    return a


def Create_Polinimial_Sum(factor_1, factor_2, temp):

    sum = []
    i = 0
    min_pol = min(len(factor_1), len(factor_2))

    while i < min_pol:
        sum.append(factor_1[i] + factor_2[i])
        i += 1

    if temp == True:
        for i in range(min_pol, len(factor_1)):
            sum.append(factor_1[i])
            i += 1
    else:
        for i in range(min_pol, len(factor_2)):
            sum.append(factor_2[i])
            i += 1

    # for i in range(0, max(len(polinomial_1), len(polinomial_2))):
    #     #print(max(len(polinomial_1), len(polinomial_2)))
    #     sum.append(polinomial_1[i] + polinomial_2[i])

    return sum


def Print_Polinom(factor):
    
    str_factor = []
    if factor[0] != 0:
        str_factor.insert(0, factor[0])
    
    for i in range(1, len(factor)):
        if factor[i] != 0:
            a = f'{factor[i]} * X ** {i}'
            str_factor.insert(0, a)
        else:
            continue

    # print(f'Коэффициенты многочлена   -   {factor}')
    # print(f"Многочлен {str_factor} = 0")
    return str_factor


factor_1 = Read_File(str(input("Введите путь первого файла: ")))
factor_2 = Read_File(str(input("Введите путь второго файла: ")))

temp = False
if len(factor_1) > len(factor_2):
    temp = True

sum_factores = Create_Polinimial_Sum(factor_1, factor_2, temp)
str_factor = (Print_Polinom(sum_factores))
print(str_factor)


file = open('4S_HW\Polinomial_3 result', 'w')

file.write(f'{str(Print_Polinom(factor_1))[1:-1]}\n')
file.write(f'{str(Print_Polinom(factor_2))[1:-1]}\n')
file.write(f'{str(Print_Polinom(sum_factores))[1:-1]}\n')
#file.write(str(sum_factores)[1:-1])

file.close()


