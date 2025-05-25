# How many number divide with 6 and 7 
count = 0
for i in range(1,201):
    if ((i %6 ==0) and (i%7 == 0)) : 
        print(i ,end = " ")  
        count = count+1

print("count = " , count)
        