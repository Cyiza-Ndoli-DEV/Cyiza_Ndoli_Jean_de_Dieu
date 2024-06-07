
def calculate_movie_ticket_price(age):
    if age < 13:
        return 1000  # Children under 13 get a discounted price of shs 1000
    elif age >= 13 and age <= 18:
        return 500  # Teenagers between 13 and 18 get a discounted price of shs 500
    elif age > 18:
        return 2000  # Adults 18 and above pay full price of shs 2000
    else:
        return 5000  # Senior citizens pay full price of shs 5000

# Example usage:
age = int(input("Please enter your age: "))
price = calculate_movie_ticket_price(age)
print(f"The price of the movie ticket for someone who is {age} years old is shs {price}.")

# num = int(input("Enter a number: "))

# reversed_num = 0
# original_num = num

# while num > 0:
#     digit = num % 10
#     reversed_num = (reversed_num * 10) + digit
#     num = num // 10

# print(f"The original number is: {original_num}")
# print(f"The reversed number is: {reversed_num}")