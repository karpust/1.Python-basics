"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках
реализовать параметры, уникальные для каждого типа оргтехники."""


class Warehouse():
    pass


class OfficeEquip():
    def __init__(self, man_firm, model):
        self.man_firm = man_firm
        self.model = model

    def __str__(self):
        return f"{self.man_firm}, model-{self.model}"


class Printer(OfficeEquip):
    def __init__(self, man_firm, model, speed_print, resolution):
        super().__init__(man_firm, model)
        self.__type = "printer"
        self.speed_print = speed_print
        self.resolution = resolution

    def __str__(self):
        return f"{self.__type}-" + super().__str__()


class Scanner(OfficeEquip):
    def __init__(self, man_firm, model, speed_scan, out_format_scan, sensor_type):
        super().__init__(man_firm, model)
        self.__type = "scanner"
        self.speed_scan = speed_scan
        self.out_format_scan = out_format_scan
        self.sensor_type = sensor_type

    def __str__(self):
        return f"{self.__type}-" + super().__str__()


class Xerox(OfficeEquip):
    def __init__(self, man_firm, model, speed_copy, in_paper_format):
        super().__init__(man_firm, model)
        self.__type = "xerox"
        self.speed_copy = speed_copy
        self.in_paper_format = in_paper_format

    def __str__(self):
        return f"{self.__type}-" + super().__str__()


# p_1 = Printer("Samsung", "0103", 20, 1200)
# p_2 = Printer("Digital", "0g0213", 10, 600)
# s_1 = Scanner("Xiaomi", "2017", 50, "pdf", "CCD")
# s_2 = Scanner("Pioneer", "5d500", 11, "pdf", "CCD")
# x_1 = Xerox("Asus", "0509", 10, "A0")
# x_2 = Xerox("Siemens", "0420c", 30, "A3")
# print(p_1, p_2, s_1, s_2, x_1, x_2, sep="\n")

