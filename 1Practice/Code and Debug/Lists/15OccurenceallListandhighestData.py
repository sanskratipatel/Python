my_list = [1,2,3,4,5,6,4,3,2,7,4,3,23,4,6,4,3,3,3,3,3]  
highest_occ = 0 
highest_occ_element = 0 
result =[]
for i in range(len(my_list)-1): 
     if my_list[i] not in result:
         result.append(my_list[i])

for i in range(len(result)-1): 
    value=my_list.count(my_list[i])  
    print(f"{my_list[i]} occurs {value} times") 
    if value>highest_occ:
        highest_occ = value
        highest_occ_element = my_list[i]  

print("highest occurence = ", highest_occ) 
print("Highest Occurence = ",highest_occ_element)