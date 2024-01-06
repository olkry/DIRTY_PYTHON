string = 'Грязный питон \t- очушуенный питонзер'
alphavit = 'Коньогонь'
number = '6789'

# print(string.index('з'))  # Узнать индекс символа, 1ое вхождение - 1 результат
# print(string.index('з', 4))  # Узнать индекс символа после определенного индекса, 1 результат
# print(string.find('з'))  # Узнать индекс символа, 1ое вхождение - 1 результат, если нет выдаст -1
# print(string.index('питон'))  # Узнать индекс символа, 1ое вхождение - 1 результат
# print(string.split(' '))  # режет строку в список по символу, сам символ удаляется
# print(string.replace('пи', 'Пай'))  # Заменяет символы на другие символы
# print(string.replace('пи', 'Пай', 1))  # Заменяет символы на другие символы, ограничиваясь количеством замен
# print(number.isdigit(), string.isdigit(), alphavit.isdigit())  # Проверка на символы, цифры
# print(number.isalpha(), string.isalpha(), alphavit.isalpha())  # Проверка на символы, буквы без знаков
# print(string[0].isupper(), number[0].isupper(), alphavit[0].isupper())  # Проверка, что 1я буква - большая
# print(number.istitle(), string.istitle(), alphavit.istitle())  # Проверка, что 1я буква - большая без знаков
# print(string.startswith('К'), alphavit.startswith('К'), number.startswith('К'))  # Начинается с
# print(string.endswith('р'), alphavit.endswith('р'), number.endswith('р'))  # Заканчивается на
print(string.count('питон'), string.count('н'))  # Сколько раз встречаются символы
print(string.lower(), string.upper())  # перевод текста в нижний и верхний регистр
print(string[7:15].strip())  # Отчищает начало и конец строки от неппечатаемых символов

