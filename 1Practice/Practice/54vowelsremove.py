mystr = "dferddd" 
mystr2 = mystr.lower()
result = ""
for i in range(0 ,len(mystr2)) : 
    if mystr2[i] not in "aeiou" : 
        result = result+mystr2[i] 
print(result)