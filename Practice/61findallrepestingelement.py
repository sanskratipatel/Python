list1 = [1,2,3,1,3,3,54,4,5,6,7,8,9]  
dict1 = {} 
for i in range(0 , len(list1)):
    if list1[i] in dict1: 
        dict1[list1[i]] +=1
    else : 
        dict1[list1[i]]  =1 

print(dict1)

