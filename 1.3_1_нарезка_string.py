

string = 'слово' + ' ещё одно слово'
print(string)

string_slice_1 = string[6:9]  # Вырезать конкретную часть текста
string_slice_2 = string[0:9]  # Вырезать от самого начала до конкретного символа
string_slice_3 = string[6:]  # Вырезать от конкретного символа до самого конца
string_slice_4 = string[:-6]  # Срез от начала, до 6 символов с конца
string_slice_5 = string[:-6:2]  # Срез от начала, до 6 символов с конца, каждого 2го символа
string_slice_6 = string[::-1]  # Полный разворот слов, срез всего, с шагом с конца [-1:1:-1]
string_slice_7 = string[6:9] + string[:6] + string[9:] # Перетасовка строки
string_slice_8 = 'slovo ' * 10  # продублировать символы 10 раз

print(string_slice_1)
print(string_slice_2)
print(string_slice_3)
print(string_slice_4)
print(string_slice_5)
print(string_slice_6)
print(string_slice_7)
print(string_slice_8)
