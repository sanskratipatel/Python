nums = [1,2,3,-2,-1,-4,2,4,5,-2] 

my_set = set()
for i in range(0 , len(nums)) : 
    for j in range(i+1,  len(nums)) : 
        for k in range(j+1,  len(nums)): 
            if nums[i] + nums[j] + nums[k] == 0:
                temp = [nums[i],nums[j],nums[k]] 
                temp.sort()  
                my_set.add(tuple(temp))



t = [list(i) for i in my_set] 
print(t)