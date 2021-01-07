"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class MyExceptZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(a, b):
    try:
        a / b
    except ZeroDivisionError:
        raise MyExceptZeroDiv("\tYou can not divide by zero")
    else:
        return a / b


a = int(input("Enter numerator a: "))
b = int(input("Enter denominator b: "))

while True:
    try:
        div(a, b)
    except MyExceptZeroDiv as err:
        print(err.txt)
        b = int(input("Enter denominator b: "))
    else:
        print(div(a, b))
        break


