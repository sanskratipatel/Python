num = [-11,-3,-34,-342]  
print("Using max = ",max(num))
max1 =num[0]  
min = num[0]
for i in range(1,len(num)): 
     if num[i] > max1:
          max1 = num[i]  
     if num[i] <min: 
        min =  num[i] 
print(max1) 
print(min)