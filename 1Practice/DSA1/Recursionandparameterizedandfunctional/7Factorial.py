def func(i ,n ,fac =1): 
    if i >n :  
        print(fac)
        return  
    if i == 0 :
        fac = 1
        return
    else:
        fac = fac*i  
    func(i+1, n ,fac) 

func(0,5)