# Process :- An Instance of a program (e.g. a python interpreter)  
# A process can have multiple thread Inside 
# It is a heavy weight process  
# There is one GIL  for one process 
# It takes more memory and it takes more memory  
# It is tough inter process communication 

# Thread :- It is light weight process 
# It is small of process 
# It is limited by GIL 
# GIL stopped us for multiprocessing so we did not stuck in deadlock 
# It could have race condidtion when two or more thread are running 


# Avoid GIL 
# Use Multiprocessing 
# Use a different ,free threaded python implementation (JPython , IronPython) 
# Use third-Party Libraries (c/c+) -> numpy ,scipy 



# MULTIPROCESSING 
from multiprocessing import Process 
import os  
import time

def square_numbers(): 
    for i in range(100):
        i = i 
        time.sleep(0.1)
processes = [] 
num_p = os.cpu_count() 

# Create Process 
for i in range(num_p) : 
    p = Process(target=square_numbers) 
    processes.append(p) 

# Start
for p in processes:
    p.start() 


# Join
for i in processes:
    p.join() 

print("End main")