list1 = [22,43,53,5,22,34,23,54,3,2,23,23,343] 
set1 = set(list1) 
list2 = list(set1) 
print(list2) 
list3 = []
for i in range(0 , len(list1)) : 
    if list1[i] not in list3:
        list3.append(list1[i]) 

print(list3) 

