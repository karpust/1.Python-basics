"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
from os.path import join


p = join(".", "fil_3.txt")
with open(p) as file:
    all_salary, count = 0, 0
    for line in file:
        lst = line.split(" ")
        if float(lst[1]) < 20000:
            print(f"Salary of {lst[0]} is {lst[1]}", end=" ")
        all_salary += float(lst[1])
        count += 1
    print('average salary is ' + '%.2f' % (all_salary/count))


