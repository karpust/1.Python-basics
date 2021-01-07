"""6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум
# возможностей, изученных на уроках по ООП."""
from datetime import datetime
# import task_4 as tsk

now = datetime.now().strftime("%d-%m-%y %H:%M:%S")

# а теперь наверное надо сделать чтобы все что вводится отправлялось в класс конкретной оргтехники,
# а потом на склад, но как я не пойму((

class Warehouse():
    storage = {}

    @classmethod
    def __str__(cls):
        return f"Total in the warehouse: {cls.storage}"

    @classmethod
    def receive(cls):
        name = input("Enter the type of equipment received by the warehouse: ")
        number = cls.check_number(name)
        if cls.storage.get(name):
            cls.storage[name] += number
        else:
            cls.storage[name] = number
        return f"{now} - delivered to the warehouse, {name}s: {number}"

    @classmethod
    def send(cls):
        name = input("Enter the type of equipment to sent from the warehouse: ")
        number = cls.check_number(name)
        if cls.storage.get(name) and cls.storage[name] >= number:
            cls.storage[name] -= number
        else:
            return f"\tFailed to send. Not enough {name}s in the warehouse"
        return f"{now} - sent from the warehouse, {name}s: {number}"

    @staticmethod
    def check_number(name):
        if name:
            while True:
                number = input(f"Enter a number of {name}s: ")
                try:
                    if not number.isdigit():
                        raise MyNotNumberError("\tThis is not a number")
                except MyNotNumberError as err:
                    print(err.text)
                else:
                    return int(number)


class MyNotNumberError(Exception):
    def __init__(self, text):
        self.text = text


a = Warehouse()
print(a.receive())
# a.receive()
# a.send()
# a.send()
print(Warehouse())





