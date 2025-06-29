num = [2,34,6,45,3242,54] 
flag = True
for i in range(0, len(num)-1) : 
    if num[i] > num[i+1] : 
        print("not sort" )  
        flag = False
        break
      
if flag == True: 
    print("sort")


    