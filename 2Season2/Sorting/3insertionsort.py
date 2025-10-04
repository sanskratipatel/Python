nums = [2,3,4,5,2,4,5,3,2] 

for i in range(1 , len(nums)):
    key = nums[i] 
    j = i -1 
    while(j >= 0 and nums[j] > key) :  
           nums[j+1] = nums[j] 
           j = j-1
    nums[j+1] = key
