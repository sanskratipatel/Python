nums = [2,3,4,2,4,5,2,4,5] 

for i in range(0 , len(nums)):
    minindex = i
    for  j in range(i+1 , len(nums)):  
        if nums[j] > nums[minindex] : 
            minindex = j 
    nums[minindex], nums[i] = nums[i] ,nums[minindex] 


print(nums)