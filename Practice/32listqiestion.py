my_list = [1,2,3434,5,6,7,896,6,4,2] 

for i in range(0 , len(my_list)) : 
    factor = 0 
    for j in range(2 , my_list[i]+1) : 
        if my_list[i] % j ==0 : 
            factor = factor +1
    if factor < 2:
        print(my_list[i])
