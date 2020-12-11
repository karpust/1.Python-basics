"""2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""
list_of_data = []
while True:
    element = input("Enter element value: ")
    if element:
        list_of_data.append(element)
    else:
        break

for i in range(0, len(list_of_data)-1, 2):
    list_of_data[i], list_of_data[i+1] = list_of_data[i+1], list_of_data[i]
print(list_of_data)
