"""1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль."""

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))


def division(n, m):
    try:
        n / m
    except ZeroDivisionError:
        print("You cannot divide by zero.")
        m = int(input("Enter a number other than zero: "))
    return n / m


print(division(a, b))

