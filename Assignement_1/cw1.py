#the following are some of the basic concepts in python 
#this is how we comment

# below is some usage of variables

person = "CYIZA NDOLI"
a= 45
best_food = "Sweet Potatoes"


#simple usage of the variables by just printing them
print(f"{person} is aged  {a} and likes  {best_food}")

#the ouput will be the following :
#CYIZA NDOLI is aged  45 and likes  Sweet Potatoes

#accepting user input

#accepting strings
name = input("Enter your name please: ")

#accepting integers
age = int(input("Enter your age too: "))

print(f"{name} is {age}  years old")
#or use casting so as to be able to concatenate the strings

print(name + " is " + str(age) +  " years old")

# the output will be 
# cyiza is 99  years old

if age >= 120:
    print("You are really old")

elif age<0:
    print("Bro you are dead or not born")
   
else:
    print("Enjoy your life "+ name + ", please You're young")    
        
