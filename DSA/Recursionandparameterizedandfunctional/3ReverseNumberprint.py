def func(i,n) : 
    if i>n:
        return
    func(i+1 ,n) 
    print(i)  
    
func(1,6) 

# 6
# 5
# 4
# 3
# 2
# 1