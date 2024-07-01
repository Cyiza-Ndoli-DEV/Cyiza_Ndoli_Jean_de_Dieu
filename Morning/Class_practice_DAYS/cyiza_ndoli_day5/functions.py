# functions

#Example 1 

def multiply():
    a = 12
    b = 23
    c = a * b
    print(c)


# Example 3 Return multiple return values of my details
def get_name_and_position():
    name ='cyiza'
    position = 'I am a software tester software tester at ST OMUTUNDE CODING ACADEMY'
    return name,position

name,position = get_name_and_position()
print(name,position)

"""_summary_
def: keyword to define a function
parameters: optional
Docstrings: optional describes the funtion purpose
return: optional returns a value from a function
    
"""

# Lambda function 
# These are small anonymous functions defined using the lambda keyword
# They re restricted to a single expression 

# Syntax
# lambda parameter: expression


# Example 6 to add numbers using a lambda function
def add(a,b): return a+b
print(add(44,765))



# Use cases of lambda function for sorting
coordinates = [(1, 2), (2, 3), (3, 1), (5, 0)]
coordinates.sort(key=lambda coordinate: coordinate[0])
print(coordinates)


# map,filter,reduce
number_squares = [1,2,3,4,5]

squares = list(map(lambda x: x**2, number_squares))

print(squares)

# **kwargs


# Allows passing an arbitrary number of keyword arguments to a function
#  Handling kwargs in a function

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

my_function(first_name="cyiza", last_name="sankara")






