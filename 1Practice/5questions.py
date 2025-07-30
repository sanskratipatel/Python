nums = [1,2,3,4,5,6,7,88,7,6,54,4,3,2,2,4,5,6,8,5,3,2] 

dict1 = {} 

for i in range(0 , len(nums)):
    if nums[i] in dict1 :  
        dict1[nums[i]] +=1 
    else: 
        dict1[nums[i]] =1

print(dict1)
    