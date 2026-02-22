
#!Task 1: Create a Dictionary of Student Marks
#code:-
student_marks = {
    "gemini": 83,
    "clode": 85,
    "siri": 78,
    "jarvis": 95,
    "edith": 97}
name = input("Enter the name of the student: ")
if name in student_marks:
    marks = student_marks[name]
    print(name,"marks:", marks)
else:
    print("Student",name,"not found in the dictionary.")      