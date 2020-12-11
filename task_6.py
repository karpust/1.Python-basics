"""6. * Реализовать структуру данных «Товары». Она должна представлять собой
список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором
каждый ключ — характеристика товара, например название, а значение — список
значений-характеристик, например список названий товаров.
Пример:
{“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]}"""

n = 1
input_lst = []

while True:
    name = input("Enter product name: ")
    if name:
        input_dict = {"name": name,
                      "price": int(input("Enter price of product: ")),
                      "number": int(input("Enter number of products: ")),
                      "unit": input("Enter unit of products: ")}
        input_lst.append((n, input_dict))
        n += 1
    else:
        break

# print(input_lst)

category_number = len(list(input_lst[0][1]))  # ['name', 'price', 'number', 'unit']
goods_number = len(input_lst)
output_dict = dict()

for i in range(category_number):
    val_lst = []
    key = list(input_lst[0][1])[i]
    for k in range(goods_number):
        val = list(input_lst[k][1].values())[i]
        val_lst.append(val)
    output_dict[key] = val_lst

print(output_dict)


