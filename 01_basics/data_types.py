"""
================================================================================
🐍 Learn Python Programming from Scratch
================================================================================
Course: Python Fundamentals - Data Types
File: data_types.py
Topic: Working with Data Types in Python
================================================================================
"""

# Python has several built-in data types
# that are used to store different kinds of data.
# By default, Python is dynamically typed,
# which means you don't need to declare the type of a variable when you create it.
# Python automatically assigns the appropriate data type based on the value you provide.
# You can check the type of a variable using the built-in type() function.
# Common data types include:
# - int: Integer numbers (e.g., 1, 2, 3)
# - float: Floating-point numbers (e.g., 1.5, 2.0)
# - str: Strings (e.g., "Hello", 'Python')
# - bool: Boolean values (True or False)
# - list: Ordered, mutable collections (e.g., [1, 2, 3])
# - tuple: Ordered, immutable collections (e.g., (1, 2, 3))
# - dict: Key-value pairs (e.g., {'name': 'Alice', 'age
# - set: Unordered collections of unique elements (e.g., {1, 2, 3})
# - NoneType: Represents the absence of a value (None)
# You can also create custom data types using classes.
# Python provides various functions and methods to work with these data types.
# You can convert between different data types using type casting functions like int(), float(), str(), etc.
# Understanding data types is crucial for effective programming in Python.

# Here are some of the most common data types in Python:

# Numeric types
integer_num = 10         # int
float_num = 10.5         # float
complex_num = 2 + 3j     # complex number 

# Text type
string_var = "Hello, Python!"

# Boolean type
is_active = False

print(type(integer_num))   # <class 'int'>
print(type(float_num))     # <class 'float'>
print(type(complex_num))   # <class 'complex'>
print(type(string_var))    # <class 'str'>
print(type(is_active))     # <class 'bool'>

"""
================================================================================
Author: Prakash Ukhalkar
GitHub: https://github.com/prakash-ukhalkar
Course: Learn Python Programming from Scratch
================================================================================
Built with ❤️ for the Python learning community
================================================================================
"""