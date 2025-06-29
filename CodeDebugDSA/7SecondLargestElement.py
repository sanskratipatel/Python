num = [1,23,43,53,463,342,3,6] 
largest =float("-inf") 
secondlargest = float("-inf") 

for i in range(0,len(num)): 
    if num[i] > largest:
        largest = num[i] 
    if  largest != num[i] and num[i] >secondlargest  : 
        secondlargest = num[i] 
print(largest) 
print(secondlargest)