"""
# Используем filter
2. Напишите программу, удаляющую из текста все слова, содержащие "абв".
"""

# lst = [2, 33, 12, 34, 3, 13]

# a = filter(lambda x: x % 2 == 0, lst)

# print(*a)

a = "привет абв пока абвг"
res = " ".join(list(filter(lambda x: not 'абв' in x, a.split())))
print(res)

print(" ".join(list(filter(lambda x: not 'абв' in x, "привет абв пока абвг".split()))))


# txt = input()
# txt = txt.split()
# new_txt = list(filter(lambda x: 'абв' not in x, txt))
# print(new_txt)


# string_text = "абв гарпорвыпав проабвал абцв попакл длывао" \
#          "олаывдлор" \
#          "абвнк" \
#          "покра"
# substring = 'абв'
# text_lst = string_text.split(" ")
# print(text_lst)
# output_txt = filter(lambda x: x.lower().find(substring) == -1, text_lst)
# print(*output_txt)
