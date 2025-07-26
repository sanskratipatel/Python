list1 = [1232,3,4,2,43,56,43,67,4,423,564,4,3] 
largest = list1[0] 

for i in range(0 , len(list1)):
    if list1[i] > largest : 
        largest = list1[i]  
print(largest)