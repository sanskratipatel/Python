list1 = [1,2,3,4,5]  
count = len(list1)  
print(count)
# result=[] 
sum = 0
for i in range(count):  
    sum = sum + list1[i]
    # result.append(list1[i]) 

average = sum//count 
print("Average ==",average)