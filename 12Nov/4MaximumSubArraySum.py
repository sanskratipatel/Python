nums = [1,2,3,4,0,1,2,3,1,0,2] 

k = 3 
sum = 0 
maxi = 0 
j=0 
i = 0 
while(j < len(nums)): 
    sum = sum +nums[j]
    if (j-i + 1 <k ) : 
        j = j+1 
    elif (j-i+1 == k) : 
        maxi = max(maxi,sum)
        sum = sum - nums[i] 
        j = j+1
        i = i+1 

print(maxi) 
print(sum)