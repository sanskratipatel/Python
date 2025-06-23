def sum1(i,n,sum =0):  
    if i>n : 
        print(sum) 
        return 
    sum = sum+i   
    sum1(i+1,n,sum)

sum1(1,5)