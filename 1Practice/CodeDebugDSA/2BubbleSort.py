num = [2,4,2,5,65,4,3,23,5,4,24,45] 
n = len(num) 

for i in range(n-2 ,-1,-1) : 
    for j in range(0 , i-1) : 
        if num[j] > num[j+1]: 
            num[j+1] , num[j] = num[j] ,num[j+1]  


print(num)