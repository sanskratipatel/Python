num = [7,6,5,4,3,2]
found =True
for i in range(0 ,len(num)-1):
    if num[i] > num[i+1] : 
        found = False 
        break
  
if (found == True) : 
     print("Sorted ")  

else: 
    print("not sorted")