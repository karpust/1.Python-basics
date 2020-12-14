"""2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой."""


def collect_data(f_name, l_name, birth_year, city, email, phone):
    return f"First name: {f_name}, last name: {l_name}, year of birth: " \
           f"{birth_year}, current city: {city}, email: {email}, phone number: {phone} "


print(collect_data(f_name="Nathan", l_name="Villazon",
                   birth_year="1986", city="Moscow",
                   email="1111@22mail.ru", phone="8111333555"))

