"""6. Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from os.path import join


output_dict = dict()
p = join(".", "fil_6.txt")
with open(p) as file:
    for line in file:
        s = line.rstrip()
        num = 0
        subj = ""
        lst = s.split("   ")
        for i in range(len(lst)):
            str_num = ""
            for liter in lst[i]:
                if i == 0 and liter.isalpha():
                    subj += liter
                if i > 0 and liter.isdigit():
                    str_num += liter
            if str_num:
                num += int(str_num)
                output_dict[subj] = num
    print(output_dict)
