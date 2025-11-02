class Person: 
    def __init__(self, name, gender):
        self.name = name 
        self.gender = gender 

p1 =Person('A','MALE')
p2 =Person('B','MALE')
p3= Person('C','FEMALE') 

l = [p1,p2,p3] 
for i in l: 
    print(i.name , i.gender)  

# We can put objects in list  

# We can also put then in Dict also 

d1 = {'p1':p1,'p2':p2 , 'p3':p3} 

for key in d1:
    print(key) 
    # print(d1[key]) 
    print(d1[key].name , d1[key].gender)