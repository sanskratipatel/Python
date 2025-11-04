a = [1,2,3,4,5,6]  
b = lambda x: x%2 ==0 
c = filter(b,a) 
print(list(c)) 

li = [a[i] for i in range(0 , len(a)) if a[i] %2 ==0] 
print(li)