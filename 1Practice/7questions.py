nums = [1,2,3,4,2,3,5,56,7,3,34,65,34,2] 

for i in range(0 , len(nums)):
    
    for j in range(i+1 , len(nums)) : 
        if nums[i] < nums[j]: 
            nums[i] , nums[j] = nums[j] ,nums[i] 

print(nums)
 