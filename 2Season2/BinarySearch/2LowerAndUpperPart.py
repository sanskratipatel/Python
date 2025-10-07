nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13] 
# Lower bound means found lower index for target or if target not exists then its greated element lower index 

lowerbound = len(nums) +1 
low = 0 
high = len(nums) +1 
target = 12
while(low <=high) : 
    mid = (low + high) //2 

    if nums[mid] >= target: 
        lowerbound = mid 
        high = mid -1 
    else : 
        low = mid +1 
print(lowerbound) 


# higher bound = means found higher index for target or if target not exists then its greated element higher index 

highbound = len(nums) +1 
lowh = 0 
highh = len(nums) +1 
target1 = 12 

while(lowh <= highh) : 
    mid = (lowh+highh)//2 

    if nums[mid] <= target: 
        highbound = mid
        lowh = mid +1 
    else : 
        highh = mid -1 
print(highbound)