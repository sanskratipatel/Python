my_list = [23,1,"Code" ,54,32,23,6,54,2,4,1] 
my_set = set(my_list)  
# {32, 1, 2, 4, 6, 'Code', 54, 23}
list1=list(my_set)
print(list1) 
# [32, 1, 2, 4, 'Code', 6, 54, 23] 
result = [] 
for i in range(0,len(my_list)-1):
    if my_list[i] not in result:
        result.append(my_list[i])

print(result)