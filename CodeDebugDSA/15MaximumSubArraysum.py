nums = [1,2,-2,-5,4,3-6,4,5] 

maxi = float("-inf") 

for i in range(0 , len(nums)): 
    total = 0 
    for j in range(0 , len(nums)): 
        total = total+nums[j] 
        if total > maxi : 
            total , maxi = maxi ,total 
print(maxi)