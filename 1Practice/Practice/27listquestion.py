my_list = [1,2,2,4,5,7,6,4,5,6,7,8,9,5,4 , "Abhi" , "Abhi"] 
result = [] 

for i in range(0 , len(my_list)):
    if my_list[i] not in result:
        result.append(my_list[i]) 

print(result)