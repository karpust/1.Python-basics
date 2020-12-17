"""3. Реализовать функцию my_func(), которая принимает три
позиционных аргумента, и возвращает сумму наибольших двух аргументов."""


def sum_of_max(arg_1, arg_2, arg_3):
    lst = sorted([arg_1, arg_2, arg_3], reverse=True)
    lst.pop()
    return sum(lst)


print(sum_of_max(arg_1=4, arg_2=0, arg_3=15))


