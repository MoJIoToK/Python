import csv
with open('7S_HW\Book.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter = ';')
    for row in reader:
        print(row[3])


