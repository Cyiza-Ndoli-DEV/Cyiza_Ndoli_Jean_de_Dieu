# Arithmetic Operators
a = 10
b = 4
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Assignment Operators
print("\nAssignment Operators:")
x = 5
print("Initial value of x:", x)
x += 2  # Same as x = x + 2
print("x += 2:", x)
x -= 3  # Same as x = x - 3
print("x -= 3:", x)
x *= 4  # Same as x = x * 4
print("x *= 4:", x)
x /= 2  # Same as x = x / 2
print("x /= 2:", x)
x //= 3 # Same as x = x // 3
print("x //= 3:", x)
x %= 5  # Same as x = x % 5
print("x %= 5:", x)
x **= 2 # Same as x = x ** 2
print("x **= 2:", x)

# Comparison Operators
print("\nComparison Operators:")
print("a =", a, ", b =", b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print("a == b:", a == b)
print("a != b:", a != b)

# Logical Operators
print("\nLogical Operators:")
x = True
y = False
print("x =", x, ", y =", y)
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Bitwise Operators
print("\nBitwise Operators:")
a = 0b1010  # Binary 10
b = 0b1100  # Binary 12
print("a =", a, ", b =", b)
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 2:", a << 2)
print("b >> 2:", b >> 2)


#PYTHON CASES
# SNAKE 
# PASCAL 
# UPPER CASE
# kebab-case


#COMPREHENSIONS
"""
Provide a concise way to create lists and dictiionaries

Lists:          []square brackets //used to store multiple items in a single variable
Dictionaries:   {}curly brackets // store data values in keyvalue pairs
    
"""
    
#LISTS
#list of squares in a range of 10

list_of_squares = [x**2 for x in range(10)]
print(list_of_squares)    

#List of even squares in the range of 20

list = [X**2 for X in range(20) if (X**2)%2 ==0 ]
print(list)


#cubes
cubes = {x:x**3 for x in range(11)}
print(cubes)