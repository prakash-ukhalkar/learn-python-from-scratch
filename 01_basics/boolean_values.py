"""
================================================================================
🐍 Learn Python Programming from Scratch
================================================================================
Course: Python Fundamentals - Boolean Operations
File: boolean_operations.py
Topic: Working with Boolean Operations in Python
================================================================================
"""


# Demonstrating Boolean values in Python
# Boolean values can be either True or False
# They are often used in conditional statements and logical operations

# Here are some examples:

is_true = True
is_false = False

print("is_true:", is_true)
print("is_false:", is_false)

# Truthy and Falsy values
print(bool(0))          # False
print(bool(""))         # False
print(bool([]))         # False
print(bool("Hello"))    # True
print(bool(123))        # True

# Logical operations
# Combining Boolean values
# AND, OR, NOT operations
# Example usage of logical operators

a = True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

"""
================================================================================
Author: Prakash Ukhalkar
GitHub: https://github.com/prakash-ukhalkar
Course: Learn Python Programming from Scratch
================================================================================
Built with ❤️ for the Python learning community
================================================================================
"""