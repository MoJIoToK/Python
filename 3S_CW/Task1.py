"""
b = 22


def f():
    b = 55

    def f_():
        nonlocal b
        b = 44


print(b)
f()
print(b)


1. Реализуйте алгоритм задания случайных чисел без использования встроенного 
   генератора псевдослучайных чисел.

"""

from time import time

num = time() % 1 * 1000

print(round(num))

"""
from time import time

def randfromtime(max):
    time1 = time()
    time1 = (time1 - int(time1))
    return int(time1 * max)

print(randfromtime(1000))
"""