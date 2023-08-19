q = "HELLO WORLD"
q = q.lower()
# Перезаписывание значения буквы q

print(q)
# hello world

h = q.replace("o", "???")
print(h)
# hell??? w???rld


# REPLACE - может иметь 1,2,3 аргумента

j = q.replace("l", "") # Заменяем "l" на пустоту
print(j)
# heo word

k = q.replace(" ", "") # Заменяем ПРОБЕЛЫ на пустоту
print(k)
# helloworld

l = q.replace("l", "", 2) # Убираем "l" 2 РАЗА
print(l)
# heo world

