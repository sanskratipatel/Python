num = [1,2,3,4,5,4,32,6,4,3] 
freq_map = {} 

for i in range(0,len(num)): 
    if num[i] in freq_map: 
        freq_map[num[i]] += 1 
    else: 
        freq_map[num[i]] =1 


print(freq_map) 
num1 = []
map1 = {}
for key in freq_map: 
    if freq_map[key] >1 : 
       num1.append(key)   
       map1[key] = freq_map[key]
print(num1)