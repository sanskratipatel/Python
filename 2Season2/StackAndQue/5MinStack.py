class StackMin: 
    def __init__(self): 
        self.items = [] 

    def push(self, val): 
        mini = val
        if len(self.items) == 0 : 
            self.items.append([val,mini]) 
        else : 
            if self.items[-1][1] < val :
                mini = self.items[-1][1] 
            self.items.append([val , mini])  
    
    def getminimum (self) : 
        if len(self.items) == 0: 
            return 0 
        return self.items[-1][1] 
    
    def top (self) : 
        return self.items[-1][0] 
    
    def size (self) : 
        return len(self.items)

    def pop(self): 
        return self.items.pop()       
s = StackMin() 
s.push(2)
s.push(6) 
s.push(7) 
s.push(5) 
s.push(1) 
print(s.getminimum() ) 
print(s.top())