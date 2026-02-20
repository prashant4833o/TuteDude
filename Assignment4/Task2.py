
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
    print("Data written to the file successfully.")

# Appending additional data to the file
additional_data = input("Enter some additional data to append to the file: ")
with open(FileName, "a") as f:  
    f.write(additional_data + "\n")
    print("Additional data appended to the file successfully.")

# Reading and displaying the final content of the file
with open(FileName, "r") as f:
    content = f.read()
    print(f"Final content of the {FileName}:")
    print(content)
    