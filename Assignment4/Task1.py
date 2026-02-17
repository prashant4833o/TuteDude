
#!Task 1: Read a File and Handle Errors 
#~Problem Statement:  Write a Python program that:
#*1.   Opens and reads a text file named sample.txt.
#*2.   Prints its content line by line.
#*3.   Handles errors gracefully if the file does not exist.
"""Program to read a file and handle errors."""
import os
FileName="sample.txt"
if os.path.exists(FileName):
    f=open(FileName,"r")
    lines = f.readlines()
    for i in range(len(lines)):
        print(f"line {i}:   {lines[i]}")
else:
    print("File does not exist.")

    


