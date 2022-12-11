"""
1 Напишите программу, удаляющую из файла все слова, содержащие "абв".

Первая задача из домешнего задания к пятому семинару
"""


# I Variation:
with open("6S_HW\My text", "r", encoding='utf-8') as f:
    string_text = f.read()
    print(string_text)


substring = 'абв'
text_lst = string_text.split(' ')
#print(text_lst)

output_text = filter(lambda x: x.lower().find(substring) == -1, text_lst)
print(*output_text)


# II Variation:

print()
with open("6S_HW\My text", "r", encoding="utf-8") as f:
    string_text = list(map(str, f.read().split()))

#print(string_text)

substring = 'абв'
output_text = filter(lambda x: x.lower().find(substring) == -1, string_text)
print(*output_text)