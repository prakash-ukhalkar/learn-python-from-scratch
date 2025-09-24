"""
================================================================================
🐍 Learn Python Programming from Scratch
================================================================================
Course: Python Fundamentals - Basic Operators
File: basic_operators.py
Topic: Working with Basic Operators in Python
================================================================================
"""

# Basic Operators in Python
# Operators are special symbols that perform operations on variables and values.
# They are used to perform arithmetic, comparison, assignment, and logical operations.
# Here are some common types of operators in Python:

"""
This script demonstrates basic operators in Python:
1. Arithmetic Operators
2. Comparison Operators
3. Assignment Operators
4. Logical Operators
"""


# -----------------------------
# 1. Arithmetic Operators
# -----------------------------

a = 15
b = 4

print("Arithmetic Operators:")
print(f"{a} + {b} =", a + b)       # Addition
print(f"{a} - {b} =", a - b)       # Subtraction
print(f"{a} * {b} =", a * b)       # Multiplication
print(f"{a} / {b} =", a / b)       # Division (float)
print(f"{a} // {b} =", a // b)     # Floor Division
print(f"{a} % {b} =", a % b)       # Modulus
print(f"{a} ** {b} =", a ** b)     # Exponentiation
print("-" * 40)

# -----------------------------
# 2. Comparison Operators
# -----------------------------

x = 10
y = 20

print("Comparison Operators:")
print(f"{x} == {y}:", x == y)      # Equal
print(f"{x} != {y}:", x != y)      # Not equal
print(f"{x} > {y}:", x > y)        # Greater than
print(f"{x} < {y}:", x < y)        # Less than
print(f"{x} >= {y}:", x >= y)      # Greater than or equal to
print(f"{x} <= {y}:", x <= y)      # Less than or equal to
print("-" * 40)

# -----------------------------
# 3. Assignment Operators
# -----------------------------

num = 5
print("Assignment Operators:")
print("Initial value:", num)

num += 3    # num = num + 3
print("After += 3:", num)

num -= 2    # num = num - 2
print("After -= 2:", num)

num *= 4    # num = num * 4
print("After *= 4:", num)

num /= 3    # num = num / 3
print("After /= 3:", num)

num %= 5    # num = num % 5
print("After %= 5:", num)

num **= 2   # num = num ** 2
print("After **= 2:", num)
print("-" * 40)

# -----------------------------
# 4. Logical Operators
# -----------------------------

print("Logical Operators:")
is_sunny = True
is_weekend = False

print("is_sunny and is_weekend:", is_sunny and is_weekend)
print("is_sunny or is_weekend:", is_sunny or is_weekend)
print("not is_sunny:", not is_sunny)
print("-" * 40)

"""
================================================================================
Author: Prakash Ukhalkar
GitHub: https://github.com/prakash-ukhalkar
Course: Learn Python Programming from Scratch
================================================================================
Built with ❤️ for the Python learning community
================================================================================
"""