import logger as lg
import operation as op

print('Добро пожаловать! Вас приветствует телефонная книга')


def Menu():

    flag = True
    result = []
    
    while flag:
        print('Выберите и введите необходимое дейтсвие:\n'
                '1 - Добавление записи\n'
                '2 - Вывод книги на экран\n'
                '3 - Импорт\n'
                '4 - Экспорт\n'
                '5 - Выход\n')
        command = int(input('Выберите команду: '))

        if command == 1:
            lg.Log('User has selected command 1')
            name = input('Введите имя: ')
            lg.Log(f'User has entered name; {name}')
            surname = input('Введите фамилию: ')
            lg.Log(f'User has entered surname; {surname}')
            phone = input('Введите телефон: ')
            lg.Log(f'User has entered name; {phone}')
            description = input('Введите примечание: ')
            lg.Log(f'User has entered surname; {description}')
            op.Create(name, surname, phone, description)
        
        if command == 2:
            lg.Log('User has selected command 2')
            print('Введите желаемый формат вывода: ')
            subcommand = int(input('1 - Разделитель пустая строка;\n'
                                    '2 - Разделитель точка с запятой(;)'))
            lg.Log(f'User has selected {subcommand}')
            result = op.Print(subcommand)
            print(result)

        if command == 3:
            lg.Log('User has selected command 3')
            Import()

        if command == 4:
            lg.Log('User has selected command 4')
            print('Введите желаемый формат экспорта: ')
            subcommand = int(input('1 - Разделитель пустая строка;\n'
                                    '2 - Разделитель точка с запятой(;)'))
            lg.Log(f'User has selected {subcommand}')
            name_phonebook = str(input('Введите желаемое название файла: '))
            lg.Log(f'User has entered {name_phonebook}')
            op.Export(subcommand, name_phonebook)
            
        if command == 5:
            lg.Log('User has selected command 5')
            flag = False
    

            



    
        