num = [1,2,3,4,6,7,8]  

num.insert(0,10)
element = 5 
place =4 
for i in range (0 ,len(num)) : 
    if i == place: 
        num.insert(place,element) 
print(num)