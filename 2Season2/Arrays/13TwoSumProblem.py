nums = [6,5,3,2,3,5,3,2,4,312,9] 
target = 10 
found = False
for i in range(0 ,len(nums)-1):  
    for j in range(i+1, len(nums)) : 
        if nums[i] + nums[j] == target: 
            found = True
            print(f"index {i} and {j} have {nums[i]} and {nums[j]} whose equal to target {target}") 
    if found == True: 
        break
