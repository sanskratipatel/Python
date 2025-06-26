num = [1,2,3,4,5,6] 
n = len(num)  
hash_map = {}
for i in range(0,n): 
    hash_map[num[i]] = hash_map.get(num[i] ,0) +1