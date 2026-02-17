
#!Task 2: Write and Append Data to a File
 
#~Problem Statement: Write a Python program that:
#*1.   Takes user input and writes it to a file named output.txt.
#*2.   Appends additional data to the same file.
#*3.   Reads and displays the final content of the file.
"""Program to write and append data to a file."""
FileName="output.txt"
# Taking user input and writing to the file
user_input = input("Enter some text to write to the file: ")
with open(FileName, "w") as f:
    f.write(user_input + "\n")

# Appending additional data to the file
additional_data = input("Enter some additional data to append to the file: ")
with open(FileName, "a") as f:  
    f.write(additional_data + "\n")

# Reading and displaying the final content of the file
with open(FileName, "r") as f:
    content = f.read()
    print("Final content of the file:")
    print(content)
    