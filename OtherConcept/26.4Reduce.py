from functools import reduce
lis = [1,2,3,4,5] 
p = lambda x,y : x*y 
s = reduce(p ,lis) 
print(s) 
