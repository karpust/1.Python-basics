"""6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка
из слов, разделенных пробелом. Каждое слово состоит из латинских
букв в нижнем регистре. Сделать вывод исходной строки, но каждое
слово должно начинаться с заглавной буквы. Необходимо использовать
написанную ранее функцию int_func()."""

# input_string1 = input("Enter word by latin lowercase letters: ")
input_string2 = input("Enter space separated words by latin lowercase letters: ")


def cap_word(b):
    return b.capitalize()


def cap_string(s):
    list_of_str = s.split(" ")
    for i in range(len(list_of_str)):
        list_of_str[i] = cap_word(list_of_str[i])
    return " ".join(list_of_str)


# print(cap_word(input_string1))
print(cap_string(input_string2))


