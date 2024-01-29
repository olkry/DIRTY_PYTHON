number = 354341568879143465743
summa = 0

while number > 0:
    summa += number % 10
    number //= 10

print(summa)
