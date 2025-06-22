def func(i,n):
    if i >n:
        return
    print(i) 
    func(i+1,n)
    
func(0,6) 
# 0
# 1
# 2
# 3
# 4
# 5
# 6