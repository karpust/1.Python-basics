# """1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран."""
#
# student_name = input("Hello! What is your name?")
# number_of_pets = int(input("How many pets do you have?"))
# if number_of_pets:
#     type_of_pets = input("What kind of pets do you have?")
#     print("%s have %d pets: %s" % (student_name, number_of_pets, type_of_pets))
# else:
#     # print(student_name + " have " + "no pets")
#     print(f"{student_name} have no pets.")


# """2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк."""
#
# typed_time = int(input("Enter time in seconds: "))
# hours, rest = divmod(typed_time, 3600)
# minutes, seconds = divmod(rest, 60)
# print("%02d:%02d:%02d" % (hours, minutes, seconds))


# """3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""
#
# n = input("Enter number n: ")
# print(int(n)+int(n+n)+int(n+n+n))


# """4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции."""
#
# big_number = input("Enter positive integer: ")
# digits = []
# for el in big_number:
#     digits.append(int(el))
# ind = len(digits)-1
# while len(digits) > 1:
#     if digits[ind] >= digits[ind-1]:
#         digits.pop(ind-1)
#     else:
#         digits.pop(ind)
#     ind -= 1
# print(digits[0])


# """5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""
#
# income = int(input("Enter income company: "))
# costs = int(input("Enter costs company: "))
# profit = income - costs
# if income > costs:
#     employees = int(input("Enter number of company employees: "))
#     print(f"Your company's profit is: {profit} руб.\n"
#           f"Your company's profitability is: {round(profit/income*100)} %\n"
#           f"Your company's income per 1 employee is: {income//employees} руб.")
# elif income < costs:
#     print("Your company is working at a loss.")
# else:
#     print("Your company does not generate income.")


# """6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составит
# не менее b километров. Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
#
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км."""
#
# a = int(input("Enter result at first day: "))
# b = int(input("Enter result at last day: "))
# day = 1
# inc = a * 0.1
# while a < b:
#     a += inc
#     day += 1
# print(f"At {day} day the gay achieved the result - not less than {b} km")
