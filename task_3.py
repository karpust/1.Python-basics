"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры
класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname, end=" ")

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])


pos_1 = Position("Jake", "Jackson", "engineer", 20000, 3000)
pos_1.get_full_name()
pos_1.get_total_income()

pos_2 = Position("Nate", "Lahey", "undercover agent", 3500000, 500000)
pos_2.get_full_name()
pos_2.get_total_income()