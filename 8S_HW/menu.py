import entry
# import read
# import control
import logger as lg

print('Добро пожаловать! Вас приветствует информационная система "Школик"')


def Menu():

    flag = True

    while flag:
        print('Выберите и введите необходимое дейтсвие:\n'
                '1 - Преподаватель\n'
                '2 - Ученик\n'
                '3 - Администратор\n'
                '4 - Написать администратору\n'
                '5 - Выход\n')
        command = int(input('Выберите команду: '))

        if command == 1:
            # message = ''
            lg.Log('User has selected command 1')
            #password = input('Введите пароль: ')
            lg.Log(f'User has entered password;')
            cnt = entry.Password(command, "Petrov")
            if cnt == True:
                print(True) 
                subcommand1 = input(('Выберите предмет:\n'
                        '1 - Русский язык\n'
                        '2 - Математика\n'))
                subcommand2 = input(('Выберите класс:\n'
                        '1 - 5А\n'
                        '2 - 10Б\n'))
                subcommand3 = input(('Выберите действие:\n'
                        '1 - Поставить оценки\n'
                        '2 - Написать ДЗ\n'))
                entry.Enter_info(subcommand1, subcommand2, subcommand3)
            else:
                password = input('Пароль неверный, попробуйте снова: ')
                entry.Password(command, password)
        
        if command == 2:
            lg.Log('User has selected command 1')
            password = input('Введите пароль: ')
            lg.Log(f'User has entered password;')
            entry.Password(command, password)
            if cnt == True: 
                subcommand1 = input(('Выберите предмет:\n'
                        '1 - Русский язык\n'
                        '2 - Математика\n'))
                subcommand2 = input(('Выберите действие:\n'
                        '1 - Посмотреть оценки\n'
                        '2 - Посмотреть ДЗ\n'))
                entry.Enter_info(subcommand1, subcommand2)
            else:
                while cnt != True:
                    password = input('Пароль неверный, попробуйте снова: ')
                    entry.Password(command, password)

        if command == 5:
            lg.Log('User has selected command 5')
            flag = False


                    
            
