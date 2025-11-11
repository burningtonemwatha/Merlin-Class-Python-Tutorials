#password = ""
#while password != "letmein":
#    password = input("Enter the password: ")

#print("Access granted!")

#pyhton methods for looping actions
# Enumirates(): useful when we want both index and value

names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Index: {index}, Name: {name}")

for x in range(5):
    for y in range(3):
        print(f"{x} : {y}")


# comprehensions: List comprehension : loop one liners

# Traditional loop
squares = []
for x in range(5):
    squares.append(x * x)
print("Squares using loop:", squares)


# Using list comprehension
squares_comp = [i * i for i in range(5)]
print("Squares using list comprehension:", squares_comp)

# Functions - Reusable block of code designed to perform a specific task
# A fuction will receive input(parameters) -> it processes the input in accordamce to logic in code block -> gives back desired output (Single value)
# define a fucntio in python we use def() keyword followed by function name and parentheses
# Pass - a function that does nothing (Absence of code block)
# Return - used to send back a value from the function to the caller
# None - specifies no return was specified
# To be executed functions have to be called

def greet():
    print(f"Hello!")
    greeting = "Welcome to the Python world."
    return greeting

message = greet()
print(message)


# Using parameters in functions - max of 6
def add(a, b):
    borrow = greet()
    sum = a + b
    return f'{borrow} {sum}'

result = add(5, 10)
print("Sum:", result)

# a function with default parametres
def multiply(a=3, b=2):
    return a * b

result = multiply()
print("Product with default parameters:", result)

result = multiply(4, 5)
print("Product with given parameters:", result)

# Special type of python functionalities in functions
# One liner functions - Lambda functions
# Used for small functionalities that can be written in a single line of code

square = lambda x: x * x
print("Square using lambda function:", square(6))

# multiple values return 
def math_operations(a, b):
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b if b != 0 else None
    return sum, difference, product, quotient

out = math_operations(10, 2)
print("Math Operations (sum, difference, product, quotient):", out)

"""
Why use Functions?
1. Reusability :: Write once, use everywhere
2. Modularity :: Break complex problems into smaller, manageable functions
3. Readability :: Clear function names and docstrings enhance code understanding
4. Maintainability :: Easier to update and fix bugs in isolated functions
5. Testing :: Functions can be tested independently for correctness
6. Abstraction :: Hide complex logic behind simple function interfaces
7. Collaboration :: Functions allow multiple developers to work on different parts of a codebase simultaneously
8. Performance :: Functions can be optimized individually for better performance

Pro Tips:
1. Use descriptive names for functions and parameters to enhance readability.
2. Document functions with docstrings to explain their purpose and usage.
3. Keep functions focused on a single task to promote reusability and maintainability.
4. Avoid side effects by minimizing changes to global state within functions.
"""

def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    import math
    area = math.pi * radius * radius
    return area

area = calculate_area(5)
print("Area of circle with radius 5:", area)

