my_list = [1,2,3,4,5,6,7,8,9] 
for i in range(0 , len(my_list)):
    if my_list[i] % 2 ==0: 
        print(my_list[i],end=" ") 
     
print("Second ===========")
for i in range(0,len(my_list)): 
    # if (i==0): 
    #      print(my_list[i],end=" ")
    if (i%2==0):
        print(my_list[i],end=" ")