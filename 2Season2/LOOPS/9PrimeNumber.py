mini = 2 
maxi = 10

is_Prime = False
for i in range(2, ((maxi)//2)+1): 

    if maxi % i ==0 :  
        is_Prime = True
        print("Not prime = ", i)
        break

if is_Prime ==False:
    print("Prime")