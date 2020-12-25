"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""
from os.path import join


p = join(".", "fil_4.txt")
p2 = join(".", "fil_41.txt")
trans_lst = ["раз", "два", "три", "четыре"]
count = 0
with open(p) as sours_file:
    with open(p2, 'w') as file_x:
        for line in sours_file:
            c = line.split(" ")
            c[0] = trans_lst[count]
            print(" ".join(c), file=file_x, end="")
            count += 1



