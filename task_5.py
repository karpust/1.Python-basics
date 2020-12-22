"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""
# reduce(function, iterable[, initializer])
from functools import reduce


def mult(prev, cur):
    return prev * cur


print(reduce(mult, [*range(100, 1001, 2)]))
