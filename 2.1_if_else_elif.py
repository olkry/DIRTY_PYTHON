# Проверка в цикле(бесконечном) на число, и что оно в диапазоне от 1 до 9:

while True:
    number = input('Введите число: ')

    if number.isdigit() and 0 < int(number) < 10:  # Первой идет проверка на число, второй уже на условие
        print(f'Вы ввели число {number} в диапазоне от 1 до 10')
    else:
        print(f'{number} не соответствует условиям!')


# count =0
# while count < 4:
#     number = input('Введите число: ')
#
#     if number.isdigit() and 0 < int(number) < 10:
#         print(f'Вы ввели число {number} в диапазоне от 1 до 10')
#     else:
#         print(f'{number} не соответствует условиям!')
#
#     count += 1


