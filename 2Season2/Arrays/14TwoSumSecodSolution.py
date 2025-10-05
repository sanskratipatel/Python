nums = [1,2,3,4,5,6,7,8] 

my_dict = {} 
target = 10
for i in range(0 , len(nums)) :  
    value  = target - nums[i]  
    if value in my_dict : 
        print (value)
        print(i , my_dict[value] )
        break
    if nums[i] not in my_dict: 
        my_dict[nums[i]] = i 
print(my_dict)