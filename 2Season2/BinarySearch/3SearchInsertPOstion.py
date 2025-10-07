nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13] 
 
target = 15
found = False
for i in range(0 , len(nums)) : 
    if target < nums[i] : 
        found = True
        print(i)
    elif target > nums[len(nums)-1]:
        found = True
        print(len(nums))
    else:
        for j in range(i+1,  len(nums)) : 
            if nums[j] > target and nums[i] <target:
                found = True
                print(j)
                break 
 
    if found == True: 
        break 


lowerbound = len(nums) 
high = len(nums) + 1 
low = 0 
if target < nums[0] : 
        found = True
        print(0)
elif target > nums[len(nums)-1]:
        found = True
        print(len(nums))
else:
    while(low <=high) : 
        mid = (low + high) //2 
        if nums[mid] >= target: 
            lowerbound = mid 
            high = mid -1 
        else: 
            low = mid + 1 
# print(lowerbound)