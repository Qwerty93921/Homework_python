my_list_1 = [1,2,3, "word", [4,9,1], 4,5,6, "word_2",99,81,19,152]
my_list_2 = [1,2,3,4,5,6,7,8,9,10]

my_list_1 = [i for i in my_list_1 if i not in my_list_2]  #VN: отличное решение!

print(my_list_1)
