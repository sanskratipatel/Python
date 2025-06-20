set1 = {1,2,3,4,5,6,7} 
set2 = {3,4,5,6,87,5,3,2} 
set3 = set() 
for i in set1 : 
    if i not in set2: 
        set3.add(i) 
    
print(set3)