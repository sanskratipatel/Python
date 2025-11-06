nums = [7,5,3,1,4,8,2] 

maxi_profit = 0 

for i in range(0 , len(nums)) : 
    for j in range(i+1, len(nums)):
        if nums[j] > nums[i] : 
            p = nums[j] - nums[i] 
            if p > maxi_profit :
                maxi_profit = p 
print(maxi_profit)