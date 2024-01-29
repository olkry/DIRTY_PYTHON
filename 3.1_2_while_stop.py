# При передачи в вайл значения True цикл будет бесконечный до команды break


count = 0
# Остановка при помощи счётчика, 10 раз. Неприемлимый способ
# while True:
#     print('Хеллоу')
#     count += 1
#     if count >= 10:
#         break

# Корректный способ:
# while count < 10:
#     print('Хеллоу')
#     count += 1

# прерывание только внутреннего цикла
# m = 0
# while m <= 10:
#     count = 0
#     while count < 10:
#         count += 1
#         if m == count and (m > 5 or count > 5):  # После значений 5 будет сбрасывать цикл на равных
#             print('Равны, сброс внутреннего цикла')
#             break
#         else:
#             print('Хеллоу', count, m)
#     m += 1

# прерывание с flag, вылет из всех циклов
# flag = 1
# m = 0
# while m <= 10 and flag:
#     count = True
#     while count < 10 and flag:
#         count += 1
#         if m == count and (m > 5 or count > 5):  # меняет флаг
#             print('Равны, сброс цикла')
#             flag = False
#         else:
#             print('Хеллоу', count, m)
#     m += 1


# Пример с continue начинает цикл сначала
# while count < 10:
#     count += 1
#     if count % 2: # тут если True(1) то входит в тело ветвления, пропускает все нечетные, добавить not и четные
#         continue
#     print('Хеллоу', count)


# Используем pass, это просто заглушка
# while count < 10:
#     count += 1
#     if count % 2:  # тут если True(1) то входит в тело ветвления, пропускает все нечетные, добавить not и четные
#         pass
#     print('Хеллоу', count)

# В случае, если цикл отработает полностью без брейков, можем прописать else
while count < 10:
    count += 1
    print(count)
    if count == 11:
        break
else:
    print('Цикл выжил')

