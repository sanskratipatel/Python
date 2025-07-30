nums = [6,59,4,3,2,1] 
ase = True
descending  =True
for i in range(0 , len(nums)) :
    if nums[i] >nums [i+1] : 
        ase = False
        break  
    if nums[i] < nums[i + 1]:
        descending = False
if ase: 
    print("sorted in asending ")  
elif descending:
    print("Sorted in desc")
else:
    print("Not sroted")