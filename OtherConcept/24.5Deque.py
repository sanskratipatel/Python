from collections import deque 

d = deque() 
d.append(1) 
d.append(2) 
d.appendleft(4)  
print(d) 

d.popleft() 
print(d) 
d.clear() 
print(d) 