#Conditinal statements in Python include if , elif , and else blocks.
# Example code for conditional statements
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Test
print(check_number(5))   # Output: Positive
print(check_number(-3))  # Output: Negative
print(check_number(0))   # Output: Zero
   
#Looping allows repeated execution of code blocks, useful for tasks like iterating over lists, dictionaries, or ranges. Here are examples using for and while loops.
# Example code for looping
# Using for loop
numbers = [1, 2, 3, 4, 5]
sum_result = 0
for num in numbers:
    sum_result += num

# Using while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Test
print("Sum of numbers:", sum_result)  # Output: Sum of numbers: 15


# Dictionaries store key-value pairs and allow efficient data retrieval using keys.
# Example code for dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing dictionary elements
def get_person_info(key):
    return person.get(key, "Key not found")

# Test
print(get_person_info("name"))    # Output: Alice
print(get_person_info("country")) # Output: Key not found


#Sets are unordered collections of unique elements. They support set operations like union, intersection, and difference.
# Example code for sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Set operations
union_result = set_a | set_b        # Union
intersection_result = set_a & set_b # Intersection
difference_result = set_a - set_b   # Difference

# Test
print("Union:", union_result)              # Output: {1, 2, 3, 4, 5, 6}
print("Intersection:", intersection_result) # Output: {3, 4}
print("Difference:", difference_result)     # Output: {1, 2}



#Slicing allows selecting a part of a list, string, or other sequence types using the syntax [start:end:step].
# Example code for sequence slicing
numbers = [10, 20, 30, 40, 50, 60]

# Slicing examples
first_half = numbers[:3]   # First three elements
second_half = numbers[3:]  # Elements from index 3 onward
even_indexed = numbers[::2] # Every second element

# Test
print("First half:", first_half)         # Output: [10, 20, 30]
print("Second half:", second_half)       # Output: [40, 50, 60]
print("Even indexed elements:", even_indexed) # Output: [10, 30, 50]
