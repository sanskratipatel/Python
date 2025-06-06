my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(my_list)):
    factor = 0  # Reset factor count for each number
    for j in range(1, my_list[i]):  # Include the number itself
        if my_list[i] % j == 0:
            factor += 1
    if factor <  2:  # Prime numbers have exactly 2 factors
        print(my_list[i])
