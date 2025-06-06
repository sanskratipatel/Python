my_list = [1,2,3,4,5,6,7,8,9]  
# factor = 0
for i in range(0,len(my_list)):  
    factor = 0
    for j in range(1 , my_list[i]):   
        print(j)
        if (my_list[i] % j )== 0:  
          factor = factor + 1 
   
    if factor ==2:
       print (my_list[i])