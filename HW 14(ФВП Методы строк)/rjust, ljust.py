q = "HELLO WORLD"
q = q.lower()
# Перезаписывание значения буквы q

print(q)
# hello world


# RJUST и LJUST требуют ШИРИНУ в скобки и дополняют строку чтобы дошло до 5 ИНДЕКСА, и строка ПРИЖИМАЕТСЯ к ПРАВОМУ КРАЮ
# ПЕРВОЕ число это до какого индекса в сумме получится, ВТОРОЕ число это ЗАПОЛНИТЕЛЬ "3"
# В НАПОЛНИТЕЛЬ можно добавить ТОЛЬКО 1 СИМВОЛ, или будет ОШИБКА


v = "111"
v = v.rjust(5)
print(v)
#   111

n = "111"
n = n.rjust(5, "3")
print(n)
# 33111

m = "111"
m = m.ljust(6, "-")
print(m)
# 111---
# ИЗНАЧАЛЬНОЕ содержимое ушло ВЛЕВО
