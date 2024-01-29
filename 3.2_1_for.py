lst = ['a', 'b', 'c', 'd']
# Попытка изменить спcмок по значению ПРОВАЛЬНАЯ
# for item in lst:
#     if item == 'c':
#         item = 'C'
# print(lst)

# Попытка изменить спиcок по значению КОРРЕКТНАЯ
for i in range(len(lst)):
    if lst[i] == 'c':
        lst[i] = 'C'
print(lst)
