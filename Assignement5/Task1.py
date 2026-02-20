
#!Task 1: Create a Dictionary of Student Marks

#*Problem Statement: Write a Python program that:
#~1.   Creates a dictionary where student names are keys and their marks are values.
#~2.   Asks the user to input a student's name.
#~3.   Retrieves and displays the corresponding marks.
#~4.   If the student’s name is not found, display an appropriate message

"""Program to create a dictionary of student marks and retrieve marks based on user input."""
# Creating a dictionary of student marks
student_marks = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Charlie": 95,
    "David": 88
}

# Asking the user to input a student's name
name = input("Enter the name of the student: ")

# Retrieving and displaying the marks
if name in student_marks:
    marks = student_marks[name]
    print(f"Marks for {name}: {marks}")
else:
    print(f"Student {name} not found in the dictionary.")      
#*Note: The program will display an appropriate message if the student’s name is not found in the dictionary.