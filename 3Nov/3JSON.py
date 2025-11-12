# Serialerzer and Encode :- Convert Python to JSON 
# Deserializer :- Convert JSON to Python 
import json 

# person = {"name": "Json", "age": 112, "work": "Nothing" , "is_alive":True , "titles" : ["Engineer" , "Doctor"]} 
# personJson = json.dumps(person, indent=4,sort_keys=True ) 
# print(personJson) 
# with open('./3person.json','w') as files:
#     json.dump(person,files,indent=4) 

# # Decoding  :- Convert Json to Python 

# person1 = json.loads(personJson) 
# print(person1) 

# with open("3person.json","r") as files : 
#     person2 = json.load(files) 


class User: 
    def __init__(self,name,age): 
        self.name = name 
        self.age = age 

user = User("Max" , 23) 

def encoding(o): 
    if isinstance(o,User) :
        return {"name":o.name,'age':o.age,o.__class__.__name__:True} 
    else:
        raise TypeError("Object of type User is not json serializer")
userJson = json.dumps(user,default=encoding )
print(userJson)
        