"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран."""

from os.path import join


p = join(".", "fil_5.txt")

with open(p, 'w') as file_x:
    for i in range(1, 25, 3):
        print(i, file=file_x, end=" ")
with open(p) as file_x:
    for line in file_x:
        c = line.split(" ")
        print(sum(float(i) for i in c if i))

