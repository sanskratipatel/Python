nums = [1,2,3,4,5,6] 
target = 11

for i in range(0 ,len(nums)-1) : 
    for j in range(i+1, len(nums)): 
        if (nums[i] + nums[j]) == target :
            print(f"Answer is {i}-> {nums[i]} and {j} ->{nums[j]} index  = {target}")