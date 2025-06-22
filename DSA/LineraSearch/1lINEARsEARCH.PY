NUM= [1,2,3,4,5,6,7,89 ] 
found = False 

inum = 994 
for i in range(0 , len(NUM)): 
    if NUM[i] == inum: 
        print("Found at index ", i , NUM[i])   
        found =True
        break


if found == False : 
    print("Nope")
