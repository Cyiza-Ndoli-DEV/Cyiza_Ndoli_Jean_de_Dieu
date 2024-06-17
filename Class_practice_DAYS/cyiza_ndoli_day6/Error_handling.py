

# Error handling in python
# Exception handling with try,except,else and finally
# custom exceptions


"""
Notes:

Error handling in Python helps handle unexpected situations and errors

1. Try: contains code that might throw an exception
NB: If an exception occurs the rest of the code in th try block is skipped

2. Except: Catches and handles exceptions
NB: You can specify different handlers to different exceptions types

3. Else: Executes if no exception is thrown
NB:If no exceptions are raised in the try block, it runs

4. Finally: Executes regardless of whether an exception is raised or not
NB: Used for cleaning up actions

"""

# Eg 1: HAndle exceptions with division by zero
try:
    number = int(input('Enter a number to divide by zero:  '))
    result = number/0
    
    
except ValueError:
    print("Something went wrong: Enter a valid number!!")
    
except ZeroDivisionError:
    print("You can't divide by zero!!")
       
else:
    print("Nothing went wrong")
    print(f"RESULT:  {result}")
    
    
    # Exercise1: Write a function that converts a string to an integer and handle both valueError
    # If the string cannot be converted to an integer and the typeError if the 
    # Use multiple except 
    
    
def string_to_int():
    while True:
        user_input = input("Enter an integer: ")
        try:
            return int(user_input)
        except ValueError:
            print(f"Error: '{user_input}' cannot be converted to an integer. Please try again.")

# Test the function
string_to_int()

        
        
#  Customized exceptions in python   
#  Eg2: Exception raised for an error in the input, if funds are insufficient
 
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {amount} with only {balance} available."
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# Custom error handling
try:
    balance = 20000
    amount_to_withdraw = 1000000
    new_balance = withdraw(balance, amount_to_withdraw)
except InsufficientFundsError as e:
    print(f"Error: {e.message}")
else:
    print(f"Your new balance is: {new_balance}")
finally:
    print("Thank you for banking with us!!")

        
      
#Note
"""Summary description

Defining a custon exception

Class Custom Error(CustonException):
# custom exception for specific error cases

def __init__(self,message)
self.message = message
super().__init__(self.message)

etc

""" 

# Example2: Create a custom exception InvalidAgeError and write a function that raises 
# this exception if the given age is negative, Handle this custom exception when calling the function

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Invalid age: {age}. Age cannot be negative."
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    return f"Age is valid: {age}"

# Custom error handling
try:
    age = int(input("Enter you age:  "))  # Example of an invalid age
    result = check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e.message}")
else:
    print(result)
finally:
    print("Age validation complete.")
