import logger 


def Create(name='', surname='', number='', description=''):

    book = []

    book.append(name.title())
    book.append(surname.title())
    book.append(number)
    book.append(description)

    with open('7S_HW\Book.csv', 'a', encoding='utf-8') as book_csv:
        book_csv.write('{}; {}; {}; {}\n'
                    .format(book[0], book[1], book[2], book[3]))
    
    with open('7S_HW\Book.txt', 'a', encoding='utf-8') as book_txt:
        book_txt.write('{}\n{}\n{}\n{}\n\n'
                    .format(book[0], book[1], book[2], book[3]))

    return book


def Print(subcommand):

    if subcommand == 1:
        with open('7S_HW\Book.txt', 'r', encoding='utf-8') as book_txt:
            result = book_txt.read()
        return result
    elif subcommand == 2:
        with open('7S_HW\Book.csv', 'r', encoding='utf-8') as book_csv:
            result = book_csv.read()
        return result


def Import(subcommand):
    if subcommand == 1:
        with open('7S_HW\Import_Book.txt', 'r', encoding='utf-8') as import_txt:
            data = import_txt.read()
            with open('7S_HW\Book.txt', 'a', encoding='utf-8') as file:
                file.write(data)

    elif subcommand == 2:
        with open('7S_HW\Import_Book.csv', 'r', encoding='utf-8') as import_csv:
            data = import_csv.read()
            with open('7S_HW\Book.csv', 'a', encoding='utf-8') as file:
                file.write(data)


def Export(subcommand, name_phonebook):
    if subcommand == 1:
        with open('7S_HW\Book.txt', 'r', encoding='utf-8') as export_txt:
            data = export_txt.read()
            with open(f'7S_HW\{name_phonebook}.txt', 'a', encoding='utf-8') as file:
                file.write(data)
    if subcommand == 2:
        with open('7S_HW\Book.csv', 'r', encoding='utf-8') as export_csv:
            data = export_csv.read()
            with open(f'7S_HW\{name_phonebook}.csv', 'a', encoding='utf-8') as file:
                file.write(data)

        
