"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра."""


class Stationary():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Start drawing {self.title}.")


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing {self.title} with a pen.")


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing {self.title} with a pencil.")


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing {self.title} with a handle.")


h_1 = Handle("dolphins")
h_1.draw()

pnc_1 = Pencil("the sea")
pnc_1.draw()

pn_1 = Pen("the grass")
pn_1.draw()
