li = [-12,-34,-23,-45,-3,-4,-323,-12,-3,-53,-2] 
# max = 0 
max = li[0]
for i in range(0,len(li)): 
    if max < li[i]: 
        max = li[i] 

print("Max value = ", max)