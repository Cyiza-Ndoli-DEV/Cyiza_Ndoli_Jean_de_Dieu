

       
 #THE __str__()
                
        #The __str__() function controls what should be returned when the class object is represented as a string.

        #f the __str__() function is not set, the string representation of the object is returned:
        
        
class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #str 
    def __str__(self):
        return f"NAME: {self.name}, AGE: ({self.age})"    
        
        # repr()
    def __repr__(self):
        return f"NAME: {self.name},\n AGE: ({self.age})"
    
        
        
        
p1 = Person("SOUZZIE", 77)
    
    
print(str(p1))

# official
print(repr(p1))