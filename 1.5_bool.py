# Любое логическое выражение в пайтане возвращает True ( или 1 ) или False ( или 0 )
'''
number = 60
print(number % 2 == 0)
print(100 + int(number % 2 == 0))

# Пример чётности числа через такое выражение с умножением
print('не' * int(number % 2 != 0) + 'чётное')
print(f'{'не' * int(number % 2 != 0)}четное')
'''
from decimal import Decimal

'''
# Получение False без логических выражений (предача пустых значений):
print(bool(''))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(tuple()))
print(bool(set()))
print(bool(None))
# Всё остальное - True
print(bool('1'))
print(bool('0'))
print(bool([[], []]))
print(bool({None}))
print(bool(tuple('0', )))
print(bool(set('1')))
print(bool(not None))
'''

# Используем в if в цикл войдет, только если будет 1 True
result_1 = (1, 2, 3)
result_2 = tuple()

if result_1:
    print('Всё ок 1')
if result_2:
    print('Всё ок 2')

number = 61

if number % 2:
    print('Нечетное')
elif not number % 2:
    print('Чётное')

num_1 = -8
num_2 = 0

if num_1:
    print(100 / num_1)
if num_2:
    print(100 / num_2)

# C плавающей точкой

num_3 = 0.1 + 0.1 + 0.1 - 0.3
num_4 = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')

if num_3:
    print(f'Not null {num_3 = }')
else:
    print(f'Null?{ num_3 = }')

if num_4:
    print(f'Not null {num_4 = }')
else:
    print(f'Null?{num_4 = }')
