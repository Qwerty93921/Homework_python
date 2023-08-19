# find() - может вызываться с 1,2,3 параметрами
# find() - ищет индекс строки которую надо найти

q = "HELLO WORLD"
q = q.lower()
# Перезаписывание значения буквы q

print(q)
# hello world

t = q.find("e")
print(t)
# 1
# 1 - это ИНДЕКС буквы "е"

y = q.find("wor")
print(y)
# 6 индекс


u = q.find("c")
print(u)
# -1
# - 1 означает что буквы НЕТ

i = q.find("o")
print(i)
# 4 индекс
# Выдает индекс который БЛИЖЕ к началу(к индексу 0)


o = q.rfind("o")
print(o)
# 7 индекс
# RFIND - ищет НАЧИНАЯ СПРАВА

p = q.find("o", 6)
print(p)
# 7
# СТАРТ начала поиска


f = q.index("o")
print(f)
# 4 - индекс

# INDEX почти как FIND, НО если в INDEX искать букву КОТОРОЙ НЕТ, тогда он выдаст ОШИБКУ
# В то время как FIND, выдаст "-1"

# g = q.index("z")
# print(g)

# ValueError: substring not found


