nums = [1,2,3,4,5,6,75,4,3,2] 

maxi = nums[0] 

for i in range(0,len(nums)):
    if nums[i] >maxi:
        maxi = nums[i] 

print(maxi)