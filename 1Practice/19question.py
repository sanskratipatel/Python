# Two Sum Problem  target value 

nums = [1,2,1,15,6,71,5,3,2,7] 
target = 13 


for i in range(0 , len(nums)): 
    for j in range(i+1,len(nums)): 
        if nums[i] + nums[j] == target:
            print(f"index are {i} num {nums[i]} ,{j} num {nums[j]} for target {target}") 
            break
