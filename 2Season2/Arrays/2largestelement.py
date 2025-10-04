nums = [122,3,23,4,342,234,5,4,234,2324]

largest = float("-inf") 
secondlargest = float("-inf") 

for i in range(0 ,len(nums)): 
    if nums[i] > largest :  
        secondlargest = largest
        largest = nums[i]
    elif nums[i] > secondlargest and nums[i] < largest: 
         secondlargest = nums[i] 
    
print(largest) 
print(secondlargest)
        