str1 ="pwwkew" 

my_map = {}
i = 0 
longest = 0 
for j in range(0 , len(str1)) : 
    if str1[j] not in my_map:
        my_map[str1[j]] = 1 
    else: 
        my_map[str1[j]] = my_map[str1[j]] +1 
    while(my_map[str1[j]]>1) :
        my_map[str1[i]]=  my_map[str1[i]]-1 
        if my_map[str1[i]] == 0 : 
            del my_map[str1[i]]
        i = i +1
    longest = max(longest,j-i+1) 
print(longest)
 