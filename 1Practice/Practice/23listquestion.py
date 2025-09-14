num = int(input("Enter the number = ")) 
mylst = []
total = 0
for i in range(0 , num): 
    n1 = int(input("Enter the number ==")) 
    mylst.append(n1) 
    total = total+n1
print(mylst)  
print(total)
listw = [12,4,5,6]
mylst.extend(listw) 
print(mylst) 

