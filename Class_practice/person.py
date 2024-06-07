#this is about classes and objects

class Person:
    
 #THE __init__()
    
    #__init__() function is called automatically every time the class is being used to create a new object
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    #create an object method 
    def WhuAreU(self):
        print(" Your name is " + self.name + " and your age is " + str(self.age))    
        
p1 = Person("Cyiza",99)
p1.age = 889   #modifying the object properties
del p1.age     #use the del keyword to delete any properties
del p1         # used to delete the object p1
p1.WhuAreU()
        
print(p1.name)
print(p1.age)
print(p1)
        
 
#  Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class

# The self PARAMETER

#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
                # EXAMPLE BELOW

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()
 
 
 
#  THE PASS STATEMENT
 
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# Example
# class Person:
#   pass
 