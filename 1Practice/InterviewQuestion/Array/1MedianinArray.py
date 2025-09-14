num = [1,2,4,5,3] 



for i in range(len(num)-2, -1,-1) : 
    for j in range(0,i):
        if num[j] > num[j+1] : 
            num[j] ,num[j+1] = num[j+1], num[j] 
n = len(num)
median = 0
print(n) 
if n %2 == 0:  
    n1 =(n//2)-1
    n2 =(n //2)
    median = (num[n1] + num[n2])
median = num[n//2] 

print(median)