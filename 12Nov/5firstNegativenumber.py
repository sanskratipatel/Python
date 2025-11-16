nums = [12,-1,-7,8,6,5,-6,6,3,-7,3,5,6] 
k =3
i = 0 
j = 0 
result = [] 
res = []
l = []
while(j < len(nums)) : 
    if nums[j] <0 :
        l.append(nums[j]) 
    if (j-i+1 < k):  
        j = j+1 
    elif (j-i+1 == k): 
        if (len(l) == 0) : 
            res.append(0) 
        else: 
            res.append(l[0]) 
        if len(l) != 0 and nums[i] == l[0]:
            l.pop(0) 
        i = i+1
        j = j+1

print(res)
for i in range(0 , len(nums) -k+1) :
    first = 0
    for j in range(i , i+k):
        if nums[j] < 0 : 
            first = nums[j]
            break 
        
    result.append(first) 
    
print(result)

