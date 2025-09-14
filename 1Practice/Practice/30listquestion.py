mylist1 = [1,2,3,4,5,5,67,6,8,8] 
mylist2 = [3,45,6,7,4,32,4,5] 
result=[]
for i in range(0 , len(mylist1)):
    if mylist1[i] in mylist2 : 
        if mylist1[i] not in result : 
            result.append(mylist1[i])

print(result)