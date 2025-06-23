num = [1,2,3,4,5,6,3,223,5,6,7,54,2] 

freq_map = {} 
# for i in range(0,len(num)) : 
#     if num[i] in freq_map : 
#         freq_map[num[i]]  +=1 
#     else: 
#         freq_map[num[i]] =1 

# print(freq_map) 

# for key in freq_map: 
#     print(key ," :", freq_map[key]) 
i =0
while  i < len(num): 
    if num[i] in freq_map: 
        num.remove(num[i]) 
    else:
        freq_map[num[i]] =1
num1 =[]
for key in freq_map:
    num1.append(key) 
print(num1)