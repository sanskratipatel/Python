marks = {"A":2,
         "B": 6 , 
         "C" :7,
         "D": 8} 
sums = 0 
for i in marks.values():
    sums = sums+i 

print(sums)  


print(sum(list(marks.values())))