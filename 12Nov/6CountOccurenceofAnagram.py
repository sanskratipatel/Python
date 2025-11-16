str1 = "aabaabaaabb" 
str2 = "aaba" 
key = len(str2)  
i = 0 
j = 0 

my_map = {}
for i in range(0 , len(str2)) :
    if str2[i] not in my_map:
        my_map[str2[i]] = 1 
    else:
        my_map[str2[i]] = my_map[str2[i]] +1 

count = len(my_map) 
ans = 0 
print(count)
while(j< len(str1)) : 
    if str1[j] in my_map:
        my_map[str1[j]] =  my_map[str1[j]] -1 
        if  my_map[str1[j]] == 0 : 
            count =count-1 
    if (j-i+1 != key) : 
        j = j+1 
    elif (j-i+1 == key): 
        if count == 0 : 
            ans = ans +1 
        if str1[i] in my_map:
            if my_map[str1[i]] == 0 : 
                count = count +1 
            my_map[str1[i]] =   my_map[str1[i]]  +1
        i = i+1 
        j = j+1 

print(ans)