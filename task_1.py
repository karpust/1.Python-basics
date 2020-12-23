"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""
from os import remove
remove("/media/sf_D_DRIVE/karpust/Github/1.Python-basics/file_5.txt")
file = open('/home/n/Documents/file_1.txt', 'x')
while True:
    c = file.write(input("Enter data: ") + "\n") - 1
    if c == 0:
        break
file.close()
                                   """ВСЕ НЕ ТАК Я СЕГОДНЯ ВСЕ ИСПРАВЛЮ, НЕ УСПЕВАЮ.."""

