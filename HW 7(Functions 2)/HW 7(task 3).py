def multiply_numbers_table(number, multiplier = 1):
    if number > 9:
        return
    
    result = number * multiplier
    print(f"{number} * {multiplier} = {result}")

    if multiplier < 10:
        multiply_numbers_table(number, multiplier + 1)
    else:
        multiply_numbers_table(number + 1)

multiply_numbers_table(2)
