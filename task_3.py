"""3. Реализовать функцию my_func(), которая принимает три
позиционных аргумента, и возвращает сумму наибольших двух аргументов."""


def sum_of_max(arg_1, arg_2, arg_3):
    lst = [arg_1, arg_2, arg_3]
    lst.remove(min(lst))
    return sum(lst)


print(sum_of_max(arg_1=2, arg_2=3, arg_3=10))



