list1 = ["one","two",'three'] 
list2 =[1,2,3] 
result = {} 
for i in range(0,len(list1)):
    # result[list1[i]] = list2[i]  
    result.update({list1[i] : list2[i]})

print(result)