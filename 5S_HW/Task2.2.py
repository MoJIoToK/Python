from random import randint

def Input_Dates(player):
    x = int(input(f"{player}, введите количество конфет, от 1 до 28: "))
    while x < 1 or x > 28:
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

queue = randint(0,1) # определение очередности хода

if queue == 1:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

count1 = 0 #Количество конфет у первого игрока 
count2 = 0 #Количество конфет у второго игрока

while amount > 28:
    if queue == 1:
        x = Input_Dates(player1)
        count1 += x
        amount -= x
        queue = False
        Print_Info(player1, x, count1, amount)
    else:
        x = randint(1,28)
        count2 += x
        amount -= x
        queue = True
        Print_Info(player2, x, count2, amount)

if queue:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")