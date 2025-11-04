a = [1,2,3,4,6,6] 
v = lambda x:x*2
b = map(v,a) 
print(list(b)) 
li = [a[i]*2 for i in range(0, len(a))] 
print(li) 

