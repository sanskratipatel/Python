marks = {}
subject_count = int (input("Enter how many subjects = ")) 
for i in range(0,subject_count): 
    subject_name= input("Enter Subject Name =") 
    subject_marks = int(input(f"Enter marks for {subject_name} = ")) 
    # marks[subject_name]= subject_marks 
    marks.update({subject_name :subject_marks}) 

print(marks)