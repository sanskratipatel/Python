list1 = [1,2,3,24232,446,7,5,5,4,3,5,56,676,43] 
myresult =[] 

for i in range(0 ,len(list1)):
    if list1[i] not in myresult:
        myresult.append(list1[i]) 

highestoccuerencelement = 0 
highestoccuerence = 0 

for i in range(0,len(myresult)):
    count =list1.count(myresult[i]) 
    print(f"{myresult[i]} and its occuerence {count}") 
    if highestoccuerence < count : 
        highestoccuerencelement = myresult[i]   
        highestoccuerence = count

print(highestoccuerencelement , "Element of highest occuserence")  
print(highestoccuerence, "higher count of that element ") 