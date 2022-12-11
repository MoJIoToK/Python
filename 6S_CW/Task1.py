#Шаблон для второй задачи

from random import randint
 
CANDIES = 60
MAX_STEP = 28
 
human = True
cur_candies = CANDIES
 
 
def get_ai_step():
    return randint(1, min(MAX_STEP, cur_candies))
 
 
def get_human_step():
    while True:
        cnt = input('Введите количество конфет: ')
        if cnt.isdigit() and 1 <= int(cnt) <= min(MAX_STEP, cur_candies):
            return int(cnt)
        print('Введено некорректное значение')
 
 
while cur_candies:
    if human:
        cnt = get_human_step()
        cur_candies -= cnt
        print(f'Пользователь взял {cnt} конфет. Осталось {cur_candies}.')
    else:
        cnt =get_ai_step()
        cur_candies -= cnt
        print(f'Бот взял {cnt} конфет. Осталось {cur_candies}.')
    human = not human
 
if human:
    print('Победил БОТ')
else:
    print('Победил человек')