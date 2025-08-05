#  Maximum Consecutive ones 

nums = [1,1,23,1,1,4,3,5,3,1,2,1,1,2,1,1,1,1] 

count = 0 
max_count =0 
for i in range(0 ,len(nums)):
    if nums[i] ==1 : 
        count = count+1 
    else : 
        if count > max_count: 
            max_count = count
        count = 0
print(max_count)