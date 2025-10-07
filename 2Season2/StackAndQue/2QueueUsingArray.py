class Queue: 
    def __init__(self): 
        self.items = [] 

    def is_empty(self) :
        return len(self.items) ==0 
    
    def enqueue(self,item): 
        self.items.append(item)

    def dequeue(self):
        if len(self.items) ==0: 
            print("Queue is Empty") 
        x = self.items.pop(0) 
        return x 
    
    def front(self) :
        if len(self.items) ==0 : 
            print("Queue is Empty") 
        return self.items[0] 
    
    def rear(self) : 
        if len(self.items) ==0 :
            print("Queue is empty" ) 
        return self.items[-1] 
    
    def size(self) :
        return len(self.items ) 
    

q = Queue() 
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4) 

print("Front is = ",q.front())
print("Rear is ",q.rear()) 
print("Deque is ",q.dequeue()) 
print("Size is ",q.size()) 
print("Is empty = ",q.is_empty())