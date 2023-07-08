q = "HELLO WORLD"
q = q.lower()
# Перезаписывание значения буквы q

print(q)
# hello world


w = q.count("o")
print(w)
# 2
# count считает количество элементов в строке

# В count можно писать 1,2,3 АРГУМЕНТА. Первое что надо искать, второе - START, третье - END


e = q.count("o", 6) # ищет "o" начиная с 6 позиции
print(e)
# 1

r = q.count("l", 1, 3) # в промежутке "el" ищет букву "l"
print(r)
# 1

