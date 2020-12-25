"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
from os.path import join


p = join(".", "fil_1.txt")
with open(p) as file_r:
    content = file_r.read()
    content_lst = content.split("\n")
    count = 0
    for i, el in enumerate(content_lst):
        if el:
            num_words = len(el.split(" "))
            print(f"string {i+1} include {num_words} word(s)")
            count += 1
    print(f"file include {count} strings")

