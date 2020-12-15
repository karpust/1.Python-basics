"""1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль."""

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))


def division(num, den):
    try:
        num / den
    except ZeroDivisionError:
        print("You cannot divide by zero.")
        den = int(input("Enter a number other than zero: "))
    return num / den


print(division(a, b))

