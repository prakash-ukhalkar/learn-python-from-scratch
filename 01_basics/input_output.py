"""
================================================================================
🐍 Learn Python Programming from Scratch
================================================================================
Course: Python Fundamentals - Basic Input and Output
File: input_output.py
Topic: Working with Input and Output in Python
================================================================================
"""

# Basic Input and Output in Python
# You can use the print() function to display output to the console.
# You can use the input() function to take input from the user.
# The input() function always returns a string, so you may need to convert it to the desired type.
# For example, to convert a string input to an integer, you can use int().

# Taking input from the user
name = input("Enter your name: ")    # input() returns a string
age = input("Enter your age: ")

print("Hello,", name)
print("You are", age, "years old.")

# Converting age to int for arithmetic operation
print("Next year, you will be", int(age) + 1, "years old.")  

"""
================================================================================
Author: Prakash Ukhalkar
GitHub: https://github.com/prakash-ukhalkar
Course: Learn Python Programming from Scratch
================================================================================
Built with ❤️ for the Python learning community
================================================================================
"""