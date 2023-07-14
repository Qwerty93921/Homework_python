my_list = [1,2,3,4,5,6,7,8,9,10]

min_number = min(my_list)
max_number = max(my_list)

min_index = my_list.index(min_number)
max_index = my_list.index(max_number)

changed_list = my_list.copy()
changed_list[min_index] = max_number
changed_list[max_index] = min_number

print(changed_list)
