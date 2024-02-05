# Список - изменяемый, поэтому будут меняться и ссылки на него
# a = [1, 2, 3]
# b = a
# print(a)
# print(b)
# a.append(4)
# print(a)
# print(b)
# b.append(5)
# print(a)
# print(b)
# print(a == b)

# Теперь сделаем полную копию copy
# a = [1, 2, 3]
# b = a.copy()
# print(a)
# print(b)
# a.append(4)
# print(a)
# print(b)
# b.append(5)
# print(a)
# print(b)
# print(a == b)

# Пребор списка через for
a = [4, True, 'fb', 3.14, False, '@sutulaya']
for items in a:
    print(items)