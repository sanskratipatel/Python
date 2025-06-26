# Merge Two sorted list No duplicate  
num1 = [1,2,3,4,5,6,7,8] 
num2 = [1,2,4,5,6,6,7] 
n = len(num1) 
m = len(num2)
i = 0 
j =0 
ans = []
while i<n and j< m:
    if num1[i] <= num2[j] : 
        if len(ans) ==0 or ans[-1] != num1[i] : 
            ans.append(num1[i]) 
        i = i+1 
    else: 
        if len(ans) ==0 or ans[-1] != num2[j]:
                ans.append(num2[j]) 
        j = j+1

              
if i <n: 
    while i<n :
         if ans[-1] != num1[i]: 
             ans.append(num1[i]) 
             i = i+1

if j<m :
    while j<m: 
         if ans[-1] != num2[j]: 
             ans.append(num2[j]) 
             j = j+1 

print(ans)

        
