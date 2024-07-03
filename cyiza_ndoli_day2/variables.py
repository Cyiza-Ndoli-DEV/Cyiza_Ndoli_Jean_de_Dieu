import math
import cmath

#integers

a=2
b=5

print(b//a) #integer division ans:2
print(b**a) #25

#float 
c= 5.88
d= 6.9876
print(c/d) #0.8414906405632836
print(d*c)
#complex
e = -8-3j
f = 4-2j
# can also use complex keyword to create complex numbers
z = complex(a, b)
print(z) #(2+5j)

# operations
print(e + f) #(-4-5j)
print(e - f) #(-12-1j)
print(e.real) #return the real part   -8.0
print(f.imag) # return the imaginary part   -2.0
print(f)  #(4-2j)
print(abs(f)) #return the magnitude   4.47213595499958
print(e.conjugate()) #negates the imaginary part   (-8+3j)

# functions
print(math.sin(c)) #provides functions to work with the math numbers  -0.39235022399145386
print(math.log(c)) #find the log of integer declared using c  1.7715567619105355
print(math.pi) #pi is a constant  3.141592653589793
# cmath
print(cmath.sin(8-3j)) #provides functions to work with the complex numbers  (9.960524419739546+1.4576011406286027j)
