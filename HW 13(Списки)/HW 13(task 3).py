my_list = [1,2,3,4,5,6,7,8,9,10]

min_number = min(my_list)
max_number = max(my_list)

changed_list = my_list.copy()
changed_list[0] = max_number
changed_list[9] = min_number

print(changed_list)
