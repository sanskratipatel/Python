import os 

if(not os.path.exists("data")):
    os.mkdir("data") 
for i in range(0, 10):
    os.mkdir(f"data/Days{i+1}")  
   
