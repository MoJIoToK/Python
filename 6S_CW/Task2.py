# s = "22+54-6*40"
# s_list = list(s)
# print(s_list)


str_ = '10+5*2*3-50+6'

# lst = list(str.split('+', '-', '*', '/')) # получаем СПИСОК
# print(lst)
# temp = ' '.join(lst)
# print(temp)
# print(type(temp))

lst = []
last = -1
for i, symbol in enumerate(str_):
    if not symbol.isdigit():
        lst.append(int(str_[last + 1:i]))
        lst.append(symbol)
        last = i
    print(i, symbol, lst, last)

lst.append(int(str_[last + 1:i + 1]))
print(lst)

lst_1 = []
if type(lst[0]) is int:
    lst_1.append(lst[0]) 

for i, symbol in enumerate(lst):
    if symbol == "*":
        print('1', lst_1[-1])
        lst_1[-1] = lst_1[-1] * lst[i + 1]
        print('2', lst_1[-1])
    elif symbol == "/":
        print('3', lst_1[-1])
        lst_1[-1] = lst_1[-1] / lst[i + 1]
        print('4', lst_1[-1])
    elif symbol == "+":
        print('5', lst_1)
        lst_1.append(lst[i + 1])
        print('6', lst_1)
    elif symbol == "-":
        print('7', lst_1)
        lst_1.append(-lst[i + 1])
        print('8', lst_1)

print(sum(lst_1))









