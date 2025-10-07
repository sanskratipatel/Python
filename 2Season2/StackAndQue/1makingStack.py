class Stack: 
    def __init__(self) : 
        self.items = [] 

    def isEmpty(self):
        return len(self.items) == 0 
    def push(self ,item) : 
        self.items.append(item) 
    def pop(self) : 
        if len(self.items) == 0 : 
            print("Cannot Pop Already Empty " )
        x = self.items.pop() 
        return x 
    def top(self) : 
        if len(self.items) ==0 :
            print("Cannot Pop Already Empty") 
        return self.items[-1] 
    def size(self) : 
        return len(self.items) 


s =Stack() 
print(s.size()) 
s.push(1)
s.push(2)
s.push(3)
s.push(4) 
s.push(5) 

print("stack pop",s.pop())  
print("stack top ",s.top()) 
print("stack is empty" ,s.isEmpty())