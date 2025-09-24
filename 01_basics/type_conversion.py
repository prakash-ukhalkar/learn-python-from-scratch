"""
================================================================================
🐍 Learn Python Programming from Scratch
================================================================================
Course: Python Fundamentals - Type Conversion
File: type_conversion.py
Topic: Working with Variables in Python
================================================================================
"""

# Converting between different data types
# You can convert between different data types using built-in functions like int(), float(), str(), etc.
# This is often necessary when you want to perform operations that require specific data types.
# For example, converting a string input to an integer for arithmetic operations.

# Here are some examples of type conversion:

age = input("Enter your age: ")      # input() returns string
print("Type of age before conversion:", type(age))

age_int = int(age)                   # Convert to integer
print("Type of age after conversion:", type(age_int))

height_str = "5.9"
height_float = float(height_str)    # Convert string to float
print("Height:", height_float)


"""
================================================================================
Author: Prakash Ukhalkar
GitHub: https://github.com/prakash-ukhalkar
Course: Learn Python Programming from Scratch
================================================================================
Built with ❤️ for the Python learning community
================================================================================
"""