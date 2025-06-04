my_list = [] 
for i in range(5): 
    value = int(input("Enter value at index {i} = "))  
    my_list.append(value) 

result =[] 
for i in range(len(my_list)-1,-1,-1) :
    result.append(my_list[i]) 

print(result)


