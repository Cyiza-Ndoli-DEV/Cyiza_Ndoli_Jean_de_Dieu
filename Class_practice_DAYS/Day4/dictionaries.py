#dictionaries
#creating and using dictionaries
#Dictionaries methods and operations

"""_summary_

Dictionaries in python are collections of keys and values
-Unordered
-Mutable and 
-Indexed by keys

"""

#Example 1: Create a dictionary
#create a dictionary for a student persuing software engineering
#The key must be your name, age, course, technology interest, course and year 

student_dict={
    'name': 'Cyiza Chegue','age': '79','technology':' ML and DA','year': '3'}
print(student_dict['name'])

#Modifying the age and technology

student_dict['age'] = 88
student_dict['technology']= 'Data Science'

print(student_dict)


#adding an email
student_dict['email']='cyndoli34@gmail.com'

print(student_dict)

student_dict.items()

#Removing a key and a value

del student_dict['age']
print(student_dict)

#popping a specific element the name

student_dict.pop('name')

print(student_dict)


#   MORE WAYS TO CREATE A DICTIONARY
#using the dict() function builds a dictionary from a sequence or list of key-value pairs

dict([('cyiza','056784674'),
    ('lionel','87645345326'),
    ('sankara', 8977468754)])

print(dict)

#Exercise 3
#Use the get method to get a value

print(student_dict.get('email'))

#Exercise 3 #Use the update method to change value in age

student_dict.update({'age':"110"})
print(student_dict)

print(student_dict)


#Exercise 4
# Use the if to check if the key 'age' is present in the dictionary

if'age' in student_dict:
    print("Age is present",student_dict['age'])
    
else:
    print("Age isnt present")
    
    #OTHER METHODS
    # keys()
    # values()
    # items()
    
    print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

"""summary

keys() returns a view of objects that displays a list of all keys
values() returns a view of objects that displays a list of all values
items() returns a view of objects that displays a list of dictionary keys and
values tuple pairs

 """
 
 # Exercise : Use the update method to change the course and add a new 
 # key "WhatsApp_Number" to the dictionary
 
student_dict.update({
    'course': 'BSC',
    'WhatsApp_Number': '0770646498'
})
print(student_dict)
        
    


