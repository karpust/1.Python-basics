"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат."""


class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"The car {self.color} {self.name} is running")

    def stop(self):
        self.speed = 0
        print(f"The car {self.color} {self.name} is stop")

    def turn(self, direction):
        print(f"The car {self.color} {self.name} is turn to the {direction}")

    def show_speed(self):
        print(f"The car {self.color} {self.name} is running with speed {self.speed} km/h ")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Warning! Your speed is over 60 km/h", end=" ")
        print(f"The car {self.color} {self.name} is running with speed {self.speed} km/h ")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Warning! Your speed is over 40 km/h", end=" ")
        print(f"The car {self.color} {self.name} is running with speed {self.speed} km/h ")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.is_police:
            print("This is a police car")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


t_1 = TownCar(70, "red", "Chevrolet", False)
t_1.go()
t_1.turn("left")
t_1.show_speed()
t_1.stop()
t_1.show_speed()
print(t_1.name)
print(t_1.color)
print(t_1.speed)
print(t_1.is_police)

w_1 = WorkCar(80, "dark blue", "Daewoo Nexia", False)
w_1.go()
w_1.turn("left")
w_1.show_speed()
w_1.stop()
w_1.show_speed()
print(w_1.name)
print(w_1.color)
print(w_1.speed)
print(w_1.is_police)

p_1 = PoliceCar(100, "white", "Ford", True)
p_1.go()
p_1.turn("left")
p_1.show_speed()
p_1.stop()
p_1.show_speed()
print(p_1.name)
print(p_1.color)
print(p_1.speed)
print(p_1.is_police)
