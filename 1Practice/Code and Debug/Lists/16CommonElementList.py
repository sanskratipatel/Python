list1 = [12,23,34,5,6,453,23,13,3,2]  
list2 = [1,2,3,4,5,6] 
result = []

for i in range(len(list1)-1):
    if list1[i] in list2:
        if list1[i] not in result:
            result.append(list1[i]) 

print(result) 