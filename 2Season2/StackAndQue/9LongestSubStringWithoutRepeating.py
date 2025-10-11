str = 'CABZABCD' 
# Longest Substring without repeating 

maxi = 0 

for i in range(0 , len(str)): 
   my_set = set()
   for j in range(i , len(str)): 
      if str[j] in my_set:
         break 
      maxi = max(maxi, j-i+1) 
      my_set.add(str[j]) 

print(maxi)