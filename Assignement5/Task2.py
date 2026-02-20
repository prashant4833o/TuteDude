
#!Task 2: Demonstrate List Slicing 

#*Problem Statement: Write a Python program that:
#~1.   Creates a list of numbers from 1 to 10.
#~2.   Extracts the first five elements from the list.
#~3.   Reverses these extracted elements.
#~4.   Prints both the extracted list and the reversed list

"""Program to demonstrate list slicing and reversing."""
# Creating a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Extracting the first five elements from the list
extracted_list = numbers[:5]

# Reversing the extracted elements
reversed_list = extracted_list[::-1]

# Printing both the extracted list and the reversed list
print("Original List:", numbers)
print("Extracted List:", extracted_list)
print("Reversed List:", reversed_list)


