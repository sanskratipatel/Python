nums = [1,3,4,12,14,22,34,112]  
is_asc = True
is_desc = True

for i in range(1, len(nums)):
    if nums[i-1] < nums[i]:
        is_desc = False
    elif nums[i-1] > nums[i]:
        is_asc = False

if is_asc:
    print("Ascending")
elif is_desc:
    print("Descending")
else:
    print("Neither")

