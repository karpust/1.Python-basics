"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("/home/n/Documents/file_1.txt", 'r') as file:
    content = file.read()
    content_lst = content.split("\n")
    count = 0
    for i, el in enumerate(content_lst):
        if el:
            num_words = len(el.split(" "))
            print(f"string {i+1} include {num_words} word(s)")
            count += 1
    print(f"file include {count} strings")

                            """ВСЕ НЕ ТАК Я СЕГОДНЯ ВСЕ ИСПРАВЛЮ, НЕ УСПЕВАЮ.."""