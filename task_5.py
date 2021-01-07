"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за
приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь."""

import task_4 as tsk

p_1 = tsk.Printer("Samsung", "0103", 20, 1200)
p_2 = tsk.Printer("Digital", "0g0213", 10, 600)
s_1 = tsk.Scanner("Xiaomi", "2017", 50, "pdf", "CCD")
s_2 = tsk.Scanner("Pioneer", "5d500", 11, "pdf", "CCD")
x_1 = tsk.Xerox("Asus", "0509", 10, "A0")
x_2 = tsk.Xerox("Siemens", "0420c", 30, "A3")
# print(p_1, p_2, s_1, s_2, x_1, x_2, sep="\n")


class Warehouse():
    storage = {}

    @classmethod
    def receive(cls, name, number):
        if cls.storage.get(name):
            cls.storage[name] += number
        else:
            cls.storage[name] = number
        return

    @classmethod
    def send(cls, name, number):
        if cls.storage.get(name) and cls.storage[name] >= number:
            cls.storage[name] -= number
        else:
            return f"Failed to send. Not enough {name}s in the warehouse"
        return


a = Warehouse()
# print(type(a))
a.receive(str(p_1), 150)
a.receive(str(p_2), 100)
a.receive(str(s_1), 50)
a.receive(str(s_2), 100)
a.receive(str(x_1), 20)
a.receive(str(x_2), 10)
print(a.storage)
a.send(str(p_1), 50)
a.send(str(p_2), 10)
a.send(str(s_1), 30)
a.send(str(s_2), 50)
a.send(str(x_1), 30)
a.send(str(x_2), 10)
print(a.storage)

# a.receive(str(tsk.Printer("Samsung", "0103", 20, 1200)), 150)
