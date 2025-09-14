my_list1 = [1,2,3,4,5] 
my_list2 = [1,2,3,4,5] 

result = {} 

for i in range(0 , len(my_list1)): 
    result[my_list1[i]] = my_list2[i] 

print(result)