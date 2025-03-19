# Problem Statements: Tuple
# 1. Employee Records Management
# Given a tuple of employee records, where each record is a tuple with (employee_id, name, age, department),
# write a program to find all employees in a specific department and print their details as a list of tuples.
# Sample Input:
employees = ((1, 'Alice', 30, 'HR'),(2, 'Bob', 25, 'Engineering'),(3, 'Charlie', 28, 'Engineering'),(4, 'Diana', 32, 'Marketing')) 
department_to_find = 'Engineering'
filtered = []
# Sample Output:
# [(2, 'Bob', 25, 'Engineering'), (3, 'Charlie', 28, 'Engineering')] 

for i in employees:
    if i[3] == department_to_find:
        filtered.append(i)

print(filtered)

# 2. Store Inventory System
# Create a tuple to store inventory items, where each item is a tuple with (item_id, name, quantity, price). Write a
# program to update the quantity of a given item and print the updated inventory as a tuple.
# Sample Input:
inventory = ( 
    (101, 'Apples', 50, 0.5), 
    (102, 'Bananas', 30, 0.2), 
    (103, 'Cherries', 20, 1.5) 
) 
item_id_to_update = 102 
new_quantity = 45

filtered_inventory = []
# Sample Output:
# ( 
#     (101, 'Apples', 50, 0.5),  
#     (102, 'Bananas', 45, 0.2),  
#     (103, 'Cherries', 20, 1.5) 
# ) 

for i in inventory:
    if i[0] == item_id_to_update:
        new = i[0] ,i[1] , new_quantity , i[3]
        filtered_inventory.append(new)
    else :
        filtered_inventory.append(i)
print(filtered_inventory)

# 3. Student Grades Analysis
# Given a tuple of student records, where each record is a tuple with (student_id, name, grades) and grades is a
# list of integers, write a program to calculate the average grade for each student and print a list of tuples with
# (student_id, name, average_grade).
# Sample Input:
students = ( 
    (1, 'Alice', [90, 85, 88]), 
    (2, 'Bob', [78, 82, 84]), 
    (3, 'Charlie', [92, 91, 89]) 
) 
# Sample Output:
# [(1, 'Alice', 87.67), (2, 'Bob', 81.33), (3, 'Charlie', 90.67)]

avg_marks = []

for i in students:
    students_id = i[0]
    name = i[1]
    grades = i[2]

    avg_grade = i[0] , i[1] , round(sum(grades) / len(grades),2)

    avg_marks.append(avg_grade)
print(avg_marks)


# 4. Library Catalog
# Create a tuple representing a library catalog, where each book is a tuple with (book_id, title, author, genre).
# Write a program to search for books by a specific author and print the list of matching books.
# Sample Input:
catalog = ( 
    (1001, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction'), 
    (1002, '1984', 'George Orwell', 'Dystopian'), 
    (1003, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction'), 
    (1004, 'Animal Farm', 'George Orwell', 'Satire') 
) 
author_to_find = 'George Orwell'
filtered_catalog = []
# Sample Output:
# [ 
#     (1002, '1984', 'George Orwell', 'Dystopian'),  
#     (1004, 'Animal Farm', 'George Orwell', 'Satire') 
# ]

for i in catalog:
    if i[2] == author_to_find:
        filtered_catalog.append(i)
print(filtered_catalog)

# 5. Movie Database
# Given a tuple of movies, where each movie is a tuple with (movie_id, title, director, rating), write a program to
# find the highest-rated movie and print its details.
# Sample Input:
movies = ( 
    (201, 'Inception', 'Christopher Nolan', 8.8), 
    (202, 'The Godfather', 'Francis Ford Coppola', 9.2), 
    (203, 'Pulp Fiction', 'Quentin Tarantino', 8.9) 
) 
highestrated_movies = movies[0]
# Sample Output:
# (202, 'The Godfather', 'Francis Ford Coppola', 9.2)

for i in movies:
    if i[3] > highestrated_movies[3]:
        highestrated_movies = i

print(highestrated_movies)

# 6. Flight Schedule Management
# Create a tuple to store flight schedules, where each flight is a tuple with (flight_id, origin, destination,
# departure_time). Write a program to find all flights between two cities and print the list of matching flights.
# Sample Input:
flights = ( 
    (301, 'New York', 'Los Angeles', '08:00'), 
    (302, 'Chicago', 'New York', '09:00'), 
    (303, 'New York', 'Chicago', '10:00'), 
    (304, 'Los Angeles', 'Chicago', '11:00') 
) 
origin_city = 'New York' 
destination_city = 'Chicago'

filtered_flights = []
# Sample Output:
# [(303, 'New York', 'Chicago', '10:00')]

for i in flights:
    if i[1] == origin_city and i[2] == destination_city:
        filtered_flights.append(i)
print(filtered_flights)

# 7. Shopping Cart System
# Given a tuple of items in a shopping cart, where each item is a tuple with (item_id, name, price, quantity), write
# a program to calculate the total cost of the cart and print it.
# Sample Input:
cart = ( 
    (401, 'Laptop', 999.99, 1), 
    (402, 'Mouse', 49.99, 2), 
    (403, 'Keyboard', 79.99, 1) 
) 
# Sample Output:
# 1179.96

filtered_cart = []

for i in cart:
    prices = i[2]
    quantity = i[3]
    total_prices = prices * quantity

    filtered_cart.append(total_prices)
print(sum(filtered_cart))

# 8. Weather Data Analysis
# Create a tuple representing weather data for a week, where each day's data is a tuple with (day, temperature,
# humidity). Write a program to find the day with the highest temperature and print its details.
# Sample Input:
weather = ( 
    ('Monday', 75, 65), 
    ('Tuesday', 86, 70), 
    ('Wednesday', 78, 68), 
    ('Thursday', 85, 72), 
    ('Friday', 82, 67) 
)
# Sample Output:
# ('Thursday', 85, 72)

highest_temp = weather[0]

for i in weather:
    if i[1] > highest_temp[1]:
        highest_temp = i
print(highest_temp)

# 9. Restaurant Menu Management
# Given a tuple of menu items, where each item is a tuple with (item_id, name, price, category), write a program
# to update the price of a specific item and print the updated menu as a tuple.
# Sample Input:
menu = ( 
    (501, 'Burger', 5.99, 'Main Course'), 
    (502, 'Fries', 2.99, 'Side Dish'), 
    (503, 'Soda', 1.49, 'Beverage') 
) 
item_id_to_update = 502 
new_price = 3.49

updated_menu = []
# Sample Output:
# ( 
#     (501, 'Burger', 5.99, 'Main Course'),  
#     (502, 'Fries', 3.49, 'Side Dish'),  
#     (503, 'Soda', 1.49, 'Beverage') 
# )

for i in menu:
    if i[0] == item_id_to_update:
        new_menu = i[0] , i[1] , new_price , i[3]
        updated_menu.append(new_menu)
    else:
        updated_menu.append(i)
print(updated_menu)

# 10. Sports Team Roster
# Create a tuple representing a sports team roster, where each player is a tuple with (player_id, name, position,
# goals_scored). Write a program to find the top scorer and print their details.
# Sample Input:
team = ( 
    (601, 'John', 'Forward', 10), 
    (602, 'Mike', 'Midfielder', 7), 
    (603, 'Dave', 'Defender', 3) 
) 
topscorer = team[0]
# Sample Output:
# (601, 'John', 'Forward', 10)

for i in team:
    if i[3] > topscorer[3]:
        topscorer = i
print(topscorer)

# 11. Bank Account Transactions
# Given a tuple of transactions, where each transaction is a tuple with (transaction_id, account_id, amount,
# transaction_type), write a program to calculate the balance for a specific account and print it.
# Sample Input:
transactions = ( 
    (701, 1001, 200.0, 'deposit'), 
    (702, 1002, 150.0, 'withdrawal'), 
    (703, 1001, 300.0, 'deposit'), 
    (704, 1001, 100.0, 'withdrawal') 
) 
account_id_to_check = 1001

balance = 0

# Sample Output:
# 400.0

for i in transactions:
    if i[1] == account_id_to_check:
        if i[3] == 'deposit':
            balance += i[2]
        elif i[3] == 'withdrawal':
            balance -= i[2]
print(balance)

# 12. Online Course Enrollment
# Create a tuple to store course enrollment, where each enrollment is a tuple with (course_id, student_id,
# enrollment_date). Write a program to find all students enrolled in a specific course and print their details.
# Sample Input:
enrollments = ( 
    (801, 2001, '2024-01-15'), 
    (802, 2002, '2024-01-16'), 
    (801, 2003, '2024-01-17'), 
    (803, 2001, '2024-01-18') 
) 
course_id_to_find = 801
filtered_enrollments = []
# Sample Output:
# [(801, 2001, '2024-01-15'), (801, 2003, '2024-01-17')]

for i in enrollments:
    if i[0] == course_id_to_find:
        filtered_enrollments.append(i)

print(filtered_enrollments)

# Problem Statement: Company Hierarchy and Salary Analysis (Master Problem)
# You are given a tuple representing a company's hierarchy and employee information. Each employee is
# represented by a tuple with the following structure:
# (employee_id, name, position, manager_id, salary, projects) 
# employee_id: Unique identifier for the employee (integer).
# name: Name of the employee (string).
# position: Job position of the employee (string).
# manager_id: Employee ID of the employee's manager (integer). If the employee is the CEO, the
# manager_id will be None.
# salary: Annual salary of the employee (float).
# projects: A list of project names the employee is currently working on (list of strings).

# Tasks:
# 1. Find the total number of employees in the company.
# 2. Find the total salary expenditure of the company.
# 3. Find the employee with the highest salary and print their details.
# 4. Find all employees who are working on a specific project and print their details.
# 5. Create a list of tuples representing the hierarchy of the company, where each tuple is in the format
# (manager_name, employee_name).
# 6. Create a list of tuples where each tuple contains a project name and a list of names of employees
# working on that project.
# Sample Input:
employees = ( 
    (1, 'Alice', 'CEO', None, 250000.0, ['Project X', 'Project Y']), 
    (2, 'Bob', 'CTO', 1, 200000.0, ['Project X']), 
    (3, 'Charlie', 'CFO', 1, 190000.0, ['Project Y']), 
    (4, 'Diana', 'Engineer', 2, 120000.0, ['Project X', 'Project Z']), 
    (5, 'Eve', 'Engineer', 2, 110000.0, ['Project Z']), 
    (6, 'Frank', 'Accountant', 3, 80000.0, ['Project Y']) 
) 
project_to_find = 'Project X'

# Expected Output:
# 1. Total number of employees
print('Total number of employees :' , employees.__len__())
# 6 
 
# 2. Total salary expenditure
total_salary = 0
for i in employees:
    total_salary += i[4]
print(total_salary)
# 950000.0 

# 3. Employee with the highest salary 
highest_salary = employees[0]
for i in employees:
    if i[4] > highest_salary[4]:
        highest_salary = i
print(highest_salary)


# (1, 'Alice', 'CEO', None, 250000.0, ['Project X', 'Project Y']) 

# 4. Employees working on 'Project X' 
employees_work_on = [i for i in employees if project_to_find in i[5]]
print(employees_work_on)
# [(1, 'Alice', 'CEO', None, 250000.0, ['Project X', 'Project Y']), 
#  (2, 'Bob', 'CTO', 1, 200000.0, ['Project X']), 
#  (4, 'Diana', 'Engineer', 2, 120000.0, ['Project X', 'Project Z'])] 
 
# 5. Company hierarchy 
# [('Alice', 'Bob'), 
#  ('Alice', 'Charlie'), 
#  ('Bob', 'Diana'), 
#  ('Bob', 'Eve'), 
#  ('Charlie', 'Frank')] 
 
# 6. List of projects with employees 
# [ 
#     ('Project X', ['Alice', 'Bob', 'Diana']), 
#     ('Project Y', ['Alice', 'Charlie', 'Frank']), 
#     ('Project Z', ['Diana', 'Eve']) 
# ]