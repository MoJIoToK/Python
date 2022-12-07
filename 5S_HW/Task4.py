"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.

aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff
"""

def Coding(text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    return res



def Decoding(text):
    amount = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            amount += text[i]
        else:
            res = res + text[i] * int(amount)
            amount = ''
    return res


with open('5S_HW\RLE_Coding', 'r') as data:
    text = data.read()

str_code = Coding(text)
print(str_code)


with open('5S_HW\RLE_encoding', 'r') as data:
    code = data.read()

str_text = Decoding(code)
print(str_text)# в файле 'RLE_encoding' изменен код


with open('5S_HW\RLE_result', 'w') as data:
    data.write(f'\n{str_code}\n')
    data.write(f'\n{str_text}\n')
