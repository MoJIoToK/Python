"""
1 Вычислить число π c заданной точностью d

*Пример:* 
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
https://completerepair.ru/kak-vychislit-chislo-pi
"""

import math


def Finding_Digit(precision):
    rank = 0
    while precision < 1:
        precision = precision*10
        rank += 1
    return rank


d = float(input("Введите точность: "))
rank = Finding_Digit(d)

sum = 0

for i in range(0, int(1/d)):
    sum += ((1/(2*i+1))*(-1)**i)

# print(sum*4)
# print(math.pi)
# print(math.pi - sum*4)

print(f"При d = {d}, pi равно {round((sum*4), rank)}, а число из модуля "\
    f"math равно {round((math.pi), rank)} -> {round((math.pi - sum*4), rank)}")



