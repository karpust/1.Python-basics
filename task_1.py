"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами."""
from sys import argv

while True:
    try:
        name_scr, rate, hours, prize = argv
    except ValueError:
        if len(argv) < 4:
            print(f"The number of passed values less then expected (4), were given:{argv}")
            break
        else:
            print(f"The number of passed values more then expected (4), were given:{argv}")
            while len(argv) > 4:
                argv.pop()
    a = [int(argv[i]) for i in range(len(argv)) if i > 0]
    r, h, p = a
    print(r * h + p)
    break

