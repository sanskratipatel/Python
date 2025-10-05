nums = [-1,3,-2,4,3,-1,3,6,-5,2] 
maxi_value = float("-inf") 
total = 0
for i in range(0 , len(nums)) :
    total = total+ nums[i] 
    if maxi_value < total: 
        maxi_value = total 
    if total < 0 : 
        total = 0 
print(maxi_value)