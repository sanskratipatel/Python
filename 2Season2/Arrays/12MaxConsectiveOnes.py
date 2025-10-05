nums = [1,1,0,2,3,41,1,1,1,0,4,35,1,1,1,1,1] 

maxi = 0 
temp_max = 0 


for i in range(0 , len(nums)):
    
    if nums[i] == 1 : 
          temp_max = temp_max +1 
    else : 
        if maxi < temp_max: 
            maxi = temp_max
            temp_max = 0 

if maxi < temp_max :  
     maxi = temp_max 
print(maxi)