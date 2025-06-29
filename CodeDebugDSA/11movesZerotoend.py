num = [ 1,0,2,3,0,5,4,0,4,0,0,3]  
n = len(num)
num2 = []
for i in range(0 ,len(num)):
    if num[i] != 0: 
        num2.append(num[i]) 
print(num2)

for i in range(0 , len(num2)) : 
    num[i] = num2[i]

for k in range(len(num2) ,n): 
    num[k] =0 
print(num)