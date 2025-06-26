num1 = [1,2,3,4,5,6]
num2 = [1,2,3,4,5,6,7,7,8] 
ans = []
n = len(num1) 
m = len(num2) 
i = num1[0] 
j = num2[0] 

while i<n and j < m : 
    if num1[i] <= num2[j] : 
       ans.append(num1[i]) 
       i = i+1
    else: 
        ans.append(num2[j]) 
        j=j+1

if i<n : 
    while i< n: 
      ans.append(num1[i]) 
      i = i+1
if j<m:
   while j<m: 
      ans.append(num2[j]) 
      j=j+1

print(ans)