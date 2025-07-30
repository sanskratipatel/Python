nums = [1,2,3,4,5,6,78,87] 

k = int(input("Enter k = "))  
if k >=len(nums):
    j = k % len(nums)
    print("Value of j",j)
    for i in range(0 , j): 
        e = nums.pop() 
        nums.insert(0 ,e)
else :  
    print("Here")
    for i in range(0 , k): 
        e = nums.pop() 
        nums.insert(0 ,e)
print(nums)
z = int(input("Enter the z ="))
num1 = [1,2,3,4,5,6,7,8] 
n = len(num1)
num1[:] = num1[n-z:] + num1[0 : (n-k)] 

print(num1)