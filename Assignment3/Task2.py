
#!Task 2: Using the Math Module for Calculations
 
#~Problem Statement: Write a Python program that:
#*1.   Asks the user for a number as input.
#*2.   Uses the math module to calculate the:
#*   --Square root of the number
#*   --Natural logarithm (log base e) of the number
#*   --Sine of the number (in radians)
#*3.   Displays the calculated results.
"""Program to perform calculations using the math module."""
import math
num=int(input("Enter a number: "))
print("Square root of",num,"is",math.sqrt(num))
print("Natural logarithm of",num,"is",math.log(num))
print("Sine of",num,"in radians is",math.sin(math.radians(num)))



