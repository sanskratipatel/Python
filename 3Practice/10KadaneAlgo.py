nums = [-2,1,-3,4,-1,2,1,-5,4] 

maxi = float("-inf")
total = 0 
for i in range(0 , len(nums)) :  
    total = total + nums[i] 
    if maxi < total : 
        maxi = total 
    if total < 0 : 
        total = 0  
print(maxi)
