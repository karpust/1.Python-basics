"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""
from os.path import join


p = join(".", "fil_1.txt")
file = open(p, 'w')
while True:
    c = file.write(input("Enter data: ") + "\n") - 1
    if c == 0:
        break
file.close()


