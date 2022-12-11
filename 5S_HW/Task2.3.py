"""
 Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
"""

from random import randint

def Input_Dates(player, step):
    x = int(input(f"{player}, введите количество конфет, от 1 до {step}: "))
    while x < 1 or x > step:
        x = int(input(f"{player}, введите корректное количество конфет: "))  
    return x


def Print_Info(player, a, count, amount):
    print(f"{player} совершил ход. Взято {a}, теперь у {player} - {count} конфет. "
            f"На столе осталось - {amount} конфет.")


print("Приветствую, Уважаемые гости! \nПредставляю Вашему вниманию игру 'Забери все конфеты'!\n"
    "Основные правила игры:\n"
    "Вам будет дано некоторое количество конфет, за один ход Вы можете взять не более\n"
    "определённого количества конфет, о котором мы с Вами договоримся."
    "Ну, что Вы готовы?'")


player1 = input("Введите имя первого игрока: ")
player2 = "Гами"
print(f"{player1} познакомьтесь с Вашим соперником! Вы играете против бота - '{player2}'")
amount = int(input("Введите количество конфет на столе: "))
max_step = int(input("Введите максимальное значение конфет которое можно взять за один раз: "))

queue = randint(0,1) # определение очередности хода

if queue == 1:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

count1 = 0 #Количество конфет у первого игрока 
count2 = 0 #Количество конфет у второго игрока

while amount > max_step:
    if queue == 1:
        x = Input_Dates(player1, max_step)
        count1 += x
        amount -= x
        queue = False
        Print_Info(player1, x, count1, amount)
    else:
        x = amount % (max_step + 1)
        if x == 0:
            x = amount % (max_step + 1) + randint(1, max_step)
        count2 += x
        amount -= x
        queue = True
        Print_Info(player2, x, count2, amount)

if queue:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")