"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""

a = 10 + 25j
b = 10 + 2j
c = a + b
d = a * b
print(c, type(c))
print(d, type(d))


class MyComplexNum():
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return MyComplexNum(self.num + other.num)

    def __mul__(self, other):
        return MyComplexNum(self.num * other.num)

    def __str__(self):
        return str(self.num)


aa = MyComplexNum(a)
bb = MyComplexNum(b)
cc = aa + bb
dd = aa * bb
print(cc, type(cc))
print(dd, type(dd))
