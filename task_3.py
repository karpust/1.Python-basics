"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

month = int(input("Enter the month number: "))
dict_seasons = {"Winter": (12, 1, 2), "Spring": (3, 4, 5), "Summer": (6, 7, 8), "Autumn": (9, 10, 11)}
for k, v in dict_seasons.items():
    if month in v:
        print(k)

# month = int(input("Enter the month number: "))
# seasons = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# for i in range(len(seasons)):
#     if seasons[i] == month:
#         if i < 3:
#             print("Winter")
#         elif 2 < i < 6:
#             print("Spring")
#         elif 5 < i < 9:
#             print("Summer")
#         else:
#             print("Autumn")
