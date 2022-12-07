"""
3. Дан список чисел. Создайте список, в который попадают числа, описываемые
  возрастающую последовательность. Порядок элементов менять нельзя.

    *Пример:*

    [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
"""

# lst = [1, 5, 2, 3, 4, 6, 1, 7]
# res = []
# i = 0
# j = 0
# k = 0
# for i, item in enumerate(lst):
#     res.append([item])
#     print(res)
#     for item in lst:
#         if item > res[j][k]:
#             res[j].append(item)
#             k += 1
#     j += 1
#     k = 0
# print(res)



# lst = [1, 5, 2, 9, 3, 4, 6, 1, 7]
# res = []
# i = 0
# # j = 0
# k = 0
# for j, item in enumerate(lst):
#     res.append([item])
#     print(res)
#     for i in range(j, len(lst)):
#         if lst[i] > res[j][k]:
#             res[j].append(lst[i])
#             k += 1
#     k = 0
# print(res)


# array = [1, 5, 2, 3, 4, 6, 1, 7]



array = [1, 5, 2, 9, 10, 3, 4, 6, 1, 7]

for i in range(len(array)):
  arr_n = [1]
  arr_n[0] = array[0]
  for j in range(i, len(array)):
    if array[j] > arr_n[-1]:
      arr_n.append(array[j])
  print(arr_n)
