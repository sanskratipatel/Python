nums = [1,2,3,4,5,6,7,8,9] 

target = 12 
found = False
for i in range(0 , len(nums)-1) : 
    for j in range(i+1, len(nums)) :  
        if nums[i] + nums[j] == target :
            found = True  
            print(i , j) 
        
    if found == True : 
        break

 

mydict = {} 


for i in range(0 , len(nums)) : 
    r = target - nums[i]  
    if r in mydict: 
        print(mydict[r] , i) 
        break
    mydict[nums[i]] = i  
