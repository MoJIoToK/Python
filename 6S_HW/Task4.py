"""
# Используем map
1. В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, чтобы выполнялось условие
A[i] - 1 = A[i-1]. Найдите это число.

5 6 7 8 9 10 12 13
"""


str_ = '5 6 7 8 9 10 12 13'

lst = list(map(int, str_.split()))

res = 0

# Стало:
res = [item + 1 for key, item in enumerate(lst) if key + 1 < len(lst) and item + 1 != lst[key + 1]]

# Было
# for key, item in enumerate(lst):
#     if key + 1 < len(lst) and item + 1 != lst[key + 1]:
#         res = item + 1
    
print(res)

