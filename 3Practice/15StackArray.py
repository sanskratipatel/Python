class Stack: 
    def __init__(self) : 
        self.items = [] 

    def is_empty(self) : 
        return len(self.items) == 0 
    
    def push (self,item) : 
        self.items.append(item) 
    
    def pop(self): 
        if len(self.items) == 0 :
            return "Stack is Empty" 
        return self.items.pop() 
    
    def top(self):
        if len(self.items) == 0 : 
            return "Stack is Empty" 
        return self.items[-1] 
    def size(self) :
        return len(self.items)  
    
    