# Maximum SubArray Sum 

num1 = [-2,1,-3,4,2,-1,-2,4] 
maxi = float("-inf") 


for i in range(0 , len(num1)):
    total = 0 
    for j in range(i , len(num1)):
        total = total + num1[j] 
        if total > maxi : 
            maxi = total 
print(maxi)
