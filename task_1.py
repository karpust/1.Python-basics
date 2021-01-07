"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Data():  # 26-12-1986
    def __init__(self, data_s):
        self.data_s = data_s

    @classmethod
    def make_num(cls, data_s):  # to 26121986
        return data_s.replace("-", "")

    @staticmethod
    def valid(data_s):
        s = ""
        lst = data_s.split("-")
        lst_val = [[1, 32], [1, 13], [1900, 2022]]
        for i in range(len(lst)):
            if int(lst[i]) in range(*lst_val[i]):
                s = "Input date is valid"
            else:
                return f"Wrong input, the date {data_s} is not valid"
        return s


date = "01-01-2021"
d_1 = Data(date)
print(d_1.make_num(date))
print(d_1.valid(date))
# print(Data.make_num(date))
# print(Data.valid(date))
