num1 = [1,0,2,3,0,4,5,0,6,4] 
temp = []
for i in range(0 , len(num1)-1): 
    if num1[i] == 0 : 
        num1[len(num1)-1] = num1[i] 
        remove = num1.pop(i)
print(num1)