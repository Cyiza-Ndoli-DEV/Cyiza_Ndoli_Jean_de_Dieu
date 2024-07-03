# Create a list with 5 names
people = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Print the 2nd item
print(f"2nd item: {people[1]}")  # Access using index (0-based)

# Change the value of the first item
people[0] = "Emily"
print(f"Updated list: {people}")

# Add a sixth item
people.append("Fiona")
print(f"List with sixth item: {people}")

# Insert "Bathel" as the 3rd item (using index)
people.insert(2, "Bathel")
print(f"List with inserted item: {people}")

# Remove the 4th item
del people[3]  # Remove by index
print(f"List after removing 4th item: {people}")

# Print the last item using negative indexing
print(f"Last item: {people[-1]}")  # -1 refers to the last element

# Create a new list with 7 items and print using range of indexes
new_list = [1, "apple", "banana", "cherry", True, None, 3.14]
print(f"Items 3rd to 5th: {new_list[2:5]}")  # Slicing (start:end:step)

# Create a list of countries, copy it, and loop through the copy
countries = ["Iran", "Cuba", "Mali", "Chile", "Ethiopia"]
countries_copy = countries.copy()  # Make a copy
for country in countries_copy:
    print(country)

# Create a list of animal names, sort them, and filter with letter 'a'
animals = ["cat", "dog", "bird", "snake", "zebra"]
animals.sort()  # Sort in ascending order (default)
animals.sort(reverse=True)  # Sort in descending order
animals_with_a = [animal for animal in animals if 'a' in animal]
print(f"Animals with 'a': {animals_with_a}")

# Create lists of first and last names and join them
first_names = ["John", "Mary"]
last_names = ["Smith", "Jones"]
full_names = first_names + last_names
print(f"Full names: {full_names}")
