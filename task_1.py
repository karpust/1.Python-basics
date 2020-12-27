"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт."""

from itertools import cycle


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        color_dict = {"red": 7, "yellow": 2, "green": 45}
        color_lst = list(color_dict.keys())
        cyc = cycle(color_lst)
        for el in color_lst:
            if next(cyc) == self.__color:
                print(self.__color, color_dict[self.__color])
                for i in range(8):
                    c = next(cyc)
                    print(c, color_dict[c])


g = TrafficLight("green")
g.running()

