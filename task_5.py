"""5. Реализовать структуру «Рейтинг», представляющую собой
не возрастающий набор натуральных чисел. У пользователя необходимо
запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""

rat_list = [7, 5, 3, 3, 2]
new_pos = int(input("Enter new position: "))
if new_pos in rat_list:
    rat_list.insert(rat_list.count(new_pos) + rat_list.index(new_pos), new_pos)
else:
    for i in range(len(rat_list)-1):
        if new_pos > rat_list[i]:
            rat_list.insert(i, new_pos)
            break
        elif new_pos < rat_list[len(rat_list)-1]:
            rat_list.append(new_pos)
            break
print(rat_list)
