# Task 1: Basic Unpacking

# Given a tuple "student_info = ("Alice", 21, "Biology")", unpack it into variables "name", "age", and "major", and print each of them.

student_info = ("Alice", 21, "Biology")
name , age , major = student_info
print(student_info)
print(name , age , major)

# Task 2: Ignoring Values

# Given a tuple "colors = ("red", "green", "blue", "yellow")", unpack it so that only the first and last colors are assigned to variables ("first_color" and "last_color") and print these two variables.

colors = ("red", "green", "blue", "yellow")
first_color , _ , _ , last_color =  colors

print(first_color , last_color)

# Task 3: Packing with Arbitrary Values

# Create a tuple named "prices" containing several price values: "(19.99, 9.99, 4.99)". Unpack these values into separate variables and calculate the total price by summing them.

prices = (19.99, 9.99, 4.99)
first , second , third = prices

print(first + second + third)

# Task 4: Unpacking with "*"

# Given a tuple "numbers = (10, 20, 30, 40, 50, 60)", unpack it so that the first number is assigned to a variable "start", the last number to "end", and the remaining middle values to a list "middle_values". Print all three variables.

numbers = (10, 20, 30, 40, 50, 60)
start , *middle_value , end = numbers

print(start , middle_value , end , sep=' , ')

# Task 5: Nested Tuple Unpacking

# Suppose you have a tuple "employee_record = ("John Doe", (35, "Engineer"), "San Francisco")". Unpack it into variables "name", "details", and "location". Then unpack "details" further into "age" and "position". Print all variables.

employee_record = ("John Doe", (35, "Engineer"), "San Francisco")
name , (age , position) , location = employee_record
print(name , age , position , location , sep=' , ')

# Task 6: Swapping Variables Using Tuple Unpacking

# Create two variables "x = 5" and "y = 10". Use tuple packing and unpacking to swap their values without using a temporary variable. Print the swapped values.

x = 5  
y = 10
tuple = y,x

print(tuple , '\n')

# Task 7: Tuple Unpacking in a Loop

# Given a list of tuples with pairs of numbers, "pairs = [(1, 2), (3, 4), (5, 6)]", use a "for" loop with unpacking to iterate through each tuple and print the sum of each pair.

pairs = [(1, 2), (3, 4), (5, 6)]
for i,j in pairs:
    print(i+j)

# Task 8: Unpacking in Place

# Given a list of numbers "values = [4, 1, 9, -3, 5]", find the minimum and maximum values using "min()" and "max()", and unpack the results into "min_val" and "max_val". Print these values.

values = [4, 1, 9, -3, 5]
min_val = min(values)
max_val = max(values)

print(min_val , max_val)
# Task 9: Grouping and Unpacking for Unknown-Length Data

# You have a list "data = [100, 200, 300, 400, 500]". Unpack it so that:
# "first" contains the first item.
# "last" contains the last item.
# "middle" contains all items in between as a list.
# Print all three variables.
data = [100, 200, 300, 400, 500]
first , *middle , last = data

print(first , middle , last , sep=' , ')

# Task 10: Creating Multiple Tuples and Unpacking Simultaneously

# Create two tuples, "a = (1, 2, 3)" and "b = (4, 5, 6)". Use tuple unpacking to swap their contents and print the new values of "a" and "b".

a = (1, 2, 3)
b = (4, 5, 6)

a , b = b , a
print(a , b)
# Additional Task: Unpacking in a Nested Structure

# Given a list of tuples "nested_data = [(1, 2), (3, 4), (5, 6)]", unpack the list in a way that you create two separate lists: one for the first elements and one for the second elements. Print both lists.

nested_data = [(1, 2), (3, 4), (5, 6)]

for i in nested_data:
    first_ele = i[0]
    second_ele = i[1]
    print(first_ele , second_ele)