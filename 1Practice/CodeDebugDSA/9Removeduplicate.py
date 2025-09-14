num = [1,2,1,1,1,1,1,3,4,5,56,3,2,34,2] 
map_dict = {}
for i in range(0 ,len(num)) : 
    if num[i] not in map_dict: 
        map_dict[num[i]] = 1 

NUM2 = []
for key in map_dict:
    NUM2.append(key) 

print(NUM2) 
print("Length = ",len(NUM2))