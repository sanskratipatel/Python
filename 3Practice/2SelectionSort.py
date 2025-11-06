nums = [5,6,3,1,3,5,7,2] 



for i in range(0 , len(nums)): 
    min_index = i
    for j in range(i+1, len(nums)) : 
        if nums[j] > nums[min_index]: 
            min_index = j
    nums[i] ,nums[min_index] = nums[min_index] , nums[i] 
print(nums)