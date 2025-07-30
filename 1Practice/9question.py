nums = [-12,3,2342,2342 ,5332,3,23,643,21,4,75,4-4,2] 

largest = float("-inf") 
secondlargest = float("-inf") 

for i in range(0 , len(nums)) : 
    if nums[i] >largest:
        secondlargest = largest 
        largest = nums[i] 
    elif nums[i] > secondlargest and nums[i] <largest:
        secondlargest = nums[i] 
print(largest) 
print(secondlargest)