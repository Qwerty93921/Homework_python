# Мы можем получить доступ ко всем элементам, но индекс элемента
# остается недоступным. Есть способ получить доступ как к индексу
# элемента, так и к самому элементу. Для этого используйте функцию
# range() в сочетании с функцией длины len():

fibonacci = [0,1,1,2,3,5,8,13,21]

for i in range(len(fibonacci)):
    print(i,fibonacci[i])

# 0 0
# 1 1
# 2 1
# 3 2
# 4 3
# 5 5
# 6 8
# 7 13
# 8 21
