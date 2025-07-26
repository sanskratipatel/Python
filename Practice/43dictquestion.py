marks = {} 
subject_count = int(input("Enter count = ")) 

for i in range(0 , subject_count):
    subject_name = input("Enter subject name = ") 
    subject_marks = int(input(f"Enter the marks for {subject_name} = ")) 
    marks[subject_name] = subject_marks
print(marks)