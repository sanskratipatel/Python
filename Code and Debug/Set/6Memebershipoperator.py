my_set = {1,2,3,4,5,6,9} 
num = int(input("Enter the number = ")) 
found = False  
for i in my_set: 
    if i == num :
        found = True  
        print("Yes")
        break
    
if found == False:
    print("No")  


if num in my_set:
    print("yES") 
else: 
    print("No") 