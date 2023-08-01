# cs-project-public
import pymysql
from tabulate import tabulate

#CREATING A DATABASE

db = pymysql.connect(host="localhost",user="root",password="root")
cursor=db.cursor()
cursor.execute("drop database Car_Showroom")
cursor.execute("CREATE DATABASE Car_Showroom")

#CREATING TABLES

db=pymysql.connect(host='localhost',user="root",password="root",db="Car_Showroom")
cursor=db.cursor()

# EMPLOYEE DETAILS
cursor.execute("CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, position VARCHAR(255), department VARCHAR(255), salary INT)")
employees_data = [
    ('Priti Sharma', 28, 'Manager', 'Sales', 5000),
    ('Sunil Shah', 32, 'Supervisor', 'Marketing', 4500),
    ('Henry Cavil', 25, 'Developer', 'IT', 4000),
    ('Sonya Khurana', 29, 'Analyst', 'Finance', 4200),
    ('Nita Verma', 31, 'Engineer', 'Engineering', 4800),
    ('Kavita Kansal', 27, 'Coordinator', 'Operations', 3800),
    ('Shreya Koli', 33, 'Consultant', 'Consulting', 5200),
    ('Disha Verma', 30, 'Designer', 'Creative', 4400),
    ('Ishpreet Singh', 26, 'Associate', 'Legal', 3900),
    ('Manya Jha', 34, 'Executive', 'Management', 5500)
]
cursor.executemany("INSERT INTO employees (name, age, position, department, salary) VALUES (%s, %s, %s, %s, %s)", employees_data)
db.commit()

# PROFIT OF LAST 12 MONTHS
cursor.execute("CREATE TABLE profit (month varchar(220), amount varchar(220), revenue varchar(220), expenses varchar(220))")
profit_data = [
    ('may2022', '50000', '60000', '10000'),
    ('june2022', '75000', '90000', '15000'),
    ('july2022', '60000', '70000', '10000'),
    ('august2022', '85000', '95000', '10000'),
    ('september2022', '55000', '65000', '10000'),
    ('october2022', '80000', '90000', '10000'),
    ('november2022', '70000', '80000', '10000'),
    ('december2022', '95000', '100000', '5000'),
    ('january2023', '65000', '75000', '10000'),
    ('february2023', '90000', '95000', '5000')
]
cursor.executemany("INSERT INTO profit (month, amount, revenue, expenses) VALUES (%s, %s, %s, %s)", profit_data)
db.commit()

# AVAILABLE CARS
cursor.execute("CREATE TABLE nexa_cars (id INT AUTO_INCREMENT PRIMARY KEY, model VARCHAR(255), price varchar(255), color VARCHAR(255), quantity INT, discount DECIMAL(5, 2))")
nexa_cars_data = [
    ('Baleno', '800000', 'Red', 10, 5.00),
    ('Ciaz', '900000', 'Blue', 5, 3.50),
    ('Swift', '700000', 'Silver', 8, 4.00),
    ('Ertiga', '940000', 'White', 3, 3.00),
    ('Ignis', '600000', 'Grey', 12, 6.00),
    ('S-Cross', '980000', 'Black', 6, 3.00),
    ('XL6', '990000', 'Maroon', 2, 2.50),
    ('Brezza', '950000', 'Orange', 7, 4.50),
    ('S-Presso', '550000', 'Green', 9, 5.50),
    ('Celerio', '650000', 'Yellow', 10, 5.00)
]
cursor.executemany("INSERT INTO nexa_cars (model, price, color, quantity, discount) VALUES (%s, %s, %s, %s, %s)", nexa_cars_data)
db.commit()

# Create table for upcoming events for staff
cursor.execute("CREATE TABLE events (id INT AUTO_INCREMENT PRIMARY KEY, event_name VARCHAR(255), date DATE, location VARCHAR(255), attendees INT, duration INT)")
events_data = [
    ('Team Building', '2023-07-10', 'Conference Room A', 50, 4),
    ('Training Workshop', '2023-07-15', 'Training Center', 30, 2),
    ('Conference', '2023-07-20', 'Convention Center', 100, 3),
    ('Product Launch', '2023-07-25', 'Exhibition Hall', 80, 2),
    ('Seminar', '2023-07-30', 'Auditorium', 200, 4),
    ('Networking Event', '2023-08-05', 'Hotel Banquet Hall', 150, 3),
    ('Trade Show', '2023-08-10', 'Trade Show Grounds', 300, 2),
    ('Workshop', '2023-08-15', 'Training Center', 40, 2),
    ('Charity Event', '2023-08-20', 'Community Center', 60, 3),
    ('Company Retreat', '2023-08-25', 'Resort', 80, 4)
]
cursor.executemany("INSERT INTO events (event_name, date, location, attendees, duration) VALUES (%s, %s, %s, %s, %s)", events_data)
db.commit()

# Create table for car accessories and parts available to sell
cursor.execute("CREATE TABLE accessories (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT, stock_quantity INT, supplier VARCHAR(255))")
accessories_data = [
    ('Seat Covers', 5000, 20, 'ABC Accessories Supplier'),
    ('Floor Mats', 1500, 30, 'XYZ Auto Parts'),
    ('Car Charger', 1000, 25, 'Car Electronics Inc.'),
    ('Roof Rack', 2000, 15, 'Adventure Gear Ltd.'),
    ('Car Perfume', 500, 50, 'Fragrance World'),
    ('Car Cover', 3000, 10, 'Vehicle Protection Systems'),
    ('Phone Holder', 800, 40, 'Tech Accessories Inc.'),
    ('Wheel Locks', 1500, 20, 'Security Solutions Ltd.'),
    ('Air Freshener', 200, 60, 'Fresh Scents Co.'),
    ('Car Cleaning Kit', 2500, 12, 'Auto Care Products')
]
cursor.executemany("INSERT INTO accessories (name, price, stock_quantity, supplier) VALUES (%s, %s, %s, %s)", accessories_data)
db.commit()

# Create table for reviews
cursor.execute("CREATE TABLE review (id INT AUTO_INCREMENT PRIMARY KEY, customer_name VARCHAR(255), rating DECIMAL(3, 2))")
reviews_data = [
    ('Hema Joshi', 4.5),
    ('Babita kumari', 3.8),
    ('Shaibal Mukharjee', 4.2),
    ('Shubman Gill', 4.0),
    ('Nicole wallace', 4.7),
    ('Prem Garg', 3.5),
    ('Chetan Jain', 4.9),
    ('Kiara Malhotra', 4.3),
    ('Shyam Aggrawal', 3.9),
    ('Ravi Jindal', 4.1)
]

cursor.executemany("INSERT INTO review (customer_name, rating) VALUES (%s, %s)", reviews_data)
db.commit()

# Function to display a table
def display_table(table, headers):
    print(tabulate(table, headers=headers, tablefmt='grid'))
    print()

# Function to update table data
def update_table(table_name, column_name, new_value, condition_column, condition_value):
    db = pymysql.connect(host='localhost', user='root', password='root', db='Car_Showroom')
    cursor = db.cursor()

    # Inserting the query
    query = f"UPDATE {table_name} SET {column_name} = %s WHERE {condition_column} = %s"

    try:
        # Execute the query with the provided values
        cursor.execute(query, (new_value, condition_value))
        db.commit()
        print("Table updated successfully.")
        print()
    except:
        db.rollback()
        print("An error occurred while updating the table.")
        print()

# Function to get user input for updating table data
def get_update_input():
    print("Enter the details for updating the table:")
    table_name = input("Table Name: ")
    column_name = input("Column Name: ")
    new_value = input("New Value: ")
    condition_column = input("Condition Column: ")
    condition_value = input("Condition Value: ")
    print()

    update_table(table_name, column_name, new_value, condition_column, condition_value)


# Function to handle user input and perform actions
def manager(option):
    while True:
        print("1. Employees Table")
        print("2. Profit Table")
        print("3. Update Tables")
        print("4. Change the user")
        option = input("Enter an option: ")
        if option == '1':
            db = pymysql.connect(host='localhost', user='root', password='root', db='Car_Showroom')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM employees")
            employees_table = cursor.fetchall()
            display_table(employees_table, ['ID', 'Name', 'Age', 'Position', 'Department', 'Salary'])
            a=input("do you want to update the table? y for yes, n for no")
            if a == 'n' or a == 'N':
                return
            elif a == 'y' or a == 'Y':
                records = int(input("Enter the number of records to insert: "))
                for i in range(records):
                    print(f"\nEnter details for record {i+1}:")
                    c1 = input("Enter value for name: ")
                    c2 = int(input("Enter value for age : "))
                    c3 = input("Enter value for position: ")
                    c4 = input("Enter value for department : ")
                    c5 = int(input("Enter value for salary : "))
                    query = f"INSERT INTO employees(name ,age ,position,department, salary) VALUES (%s, %s,%s, %s,%s)"
                    cursor.execute(query, (c1,c2,c3,c4,c5))
                    db.commit()
                    print("values inserted")
                
        elif option == '2':
            db = pymysql.connect(host='localhost', user='root', password='root', db='Car_Showroom')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM profit")
            profit_table = cursor.fetchall()
            display_table(profit_table, ['Year', 'Amount', 'Revenue', 'Expenses'])
            a=input("do you want to update the table? y for yes, n for no")
            if a == 'n' or a == 'N':
                return
            elif a == 'y' or a == 'Y':
                records = int(input("Enter the number of records to insert: "))
                for i in range(records):
                    print(f"\nEnter details for record {i+1}:")
                    c1 = input("Enter value for month: ")
                    c2 = input("Enter value for amount : ")
                    c3 = input("Enter value for revenue: ")
                    c4 = input("Enter value for expenses : ")
                    query = f"INSERT INTO profit(month,amount,revenue,expenses) VALUES (%s, %s,%s, %s)"
                    cursor.execute(query, (c1,c2,c3,c4))
                    db.commit()
                    print("values inserted")
           
        elif option == '3':
            get_update_input()
        else:
            return
    
def staff(option):
    while True:
        print("1. Nexa Cars Table")
        print("2. Events Table")
        print("3. Accessories Table")
        print("4. Update Tables")
        print("5. Change the user")
        option = input("Enter an option: ")
        if option == '1':
            db = pymysql.connect(host='localhost', user='root', password='root', db='Car_Showroom')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM nexa_cars")
            cars_table = cursor.fetchall()
            display_table(cars_table, ['ID', 'Model', 'Price', 'Color', 'Quantity', 'Discount'])
            a=input("do you want to update the table? y for yes, n for no")
            if a == 'n' or a == 'N':
                return
            elif a == 'y' or a == 'Y':
                records = int(input("Enter the number of records to insert: "))
                for i in range(records):
                    print(f"\nEnter details for record {i+1}:")
                    c1 = input("Enter value for model ")
                    c2 = input("Enter value for price: ")
                    c3 = input("Enter value for color : ")
                    c4 = int(input("Enter value for quantity : "))
                    c5 = float(input("Enter value for discount : "))
                    query = f"INSERT INTO nexa_cars(model,price,color,quantity,discount) VALUES (%s, %s,%s, %s,%s)"
                    cursor.execute(query, (c1,c2,c3,c4,c5))
                    db.commit()
                    print("values inserted")
            
        elif option == '2':
            db = pymysql.connect(host='localhost', user='root', password='root', db='Car_Showroom')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM events")
            events_table = cursor.fetchall()
            display_table(events_table, ['ID', 'Event Name', 'Date', 'Location', 'Attendees', 'Duration'])
            a=input("do you want to update the table? y for yes, n for no")
            if a == 'n' or 'N':
                return
            elif a == 'y' or a == 'Y':
                records = int(input("Enter the number of records to insert: "))
                for i in range(records):
                    print(f"\nEnter details for record {i+1}:")
                    c1 = input("Enter value for event name ")
                    c2 = input("Enter value for date: ")
                    c3 = input("Enter value for venue : ")
                    c4 = int(input("Enter value for attendees : "))
                    c5 = float(input("Enter value for duration : "))
                    query = f"INSERT INTO events(event_name,date,location,attendees,duration) VALUES (%s, %s,%s, %s,%s)"
                    cursor.execute(query, (c1,c2,c3,c4,c5))
                    db.commit()
                    print("values inserted")
    
        elif option == '3':
            db = pymysql.connect(host='localhost', user='root', password='root', db='Car_Showroom')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM accessories")
            accessories_table = cursor.fetchall()
            display_table(accessories_table, ['ID', 'Name', 'Price', 'Stock Quantity', 'Supplier'])
            a=input("do you want to update the table? y for yes, n for no")
            if a == 'n' or a == 'N':
                return
            elif a == 'y' or a == 'Y':
                records = int(input("Enter the number of records to insert: "))
                for i in range(records):
                    print(f"\nEnter details for record {i+1}:")
                    c1 = input("Enter value for name ")
                    c2 = input("Enter value for price: ")
                    c3 = input("Enter value for stock quantity : ")
                    c4 = int(input("Enter value for supplier : "))
                    query = f"INSERT INTO employees(name,price,stock_quantity,supplier) VALUES (%s, %s,%s, %s)"
                    cursor.execute(query, (c1,c2,c3,c4))
                    db.commit()
                    print("values inserted")

        elif option == '4':
            get_update_input()
        else:
            return
        
def customer(option):
    while True:
        print("1. Nexa Cars Table")
        print("2. Accessories Table")
        print("3. Customer_Review Table")
        print("4. Change the user")
        option = input("Enter an option: ")
        if option == '1':
            db = pymysql.connect(host='localhost', user='root', password='root', db='Car_Showroom')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM nexa_cars")
            cars_table = cursor.fetchall()
            display_table(cars_table, ['ID', 'Model', 'Price', 'Color', 'Quantity', 'Discount'])
        elif option == '2':
            db = pymysql.connect(host='localhost', user='root', password='root', db='Car_Showroom')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM accessories")
            accessories_table = cursor.fetchall()
            display_table(accessories_table, ['ID', 'Name', 'Price', 'Stock Quantity', 'Supplier'])
        elif option == '3':
            db = pymysql.connect(host='localhost', user='root', password='root', db='Car_Showroom')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM review")
            reviews_table = cursor.fetchall()
            display_table(reviews_table, ['customer_name', 'rating'])
            a = input(" do you want to leave a review")
            if a == 'n' or a == 'N':
                return
            elif a == 'y' or a == 'Y':
                for i in range(1):
                    c1 = input("Enter your name ")
                    c2 = float(input("Enter the rating: "))
                    query = f"INSERT INTO review(customer_name,rating) VALUES (%s, %s)"
                    cursor.execute(query, (c1,c2))
                    db.commit()
                    print("Thanks for your response")

        else:
            return
        
        
print("HELLO!!! Welcome to our project about Car Showroom Management.There are many different tables that contain different informations about the showroom.There are three viewing options,Manager,Staff,Customer.")
print("Made By: \n1.Kavya Bansal(Group Leader) \n2.Pakhi Jain \n3.bhavishya")
while True:
    print("Which usermode do you want to choose?")
    z= int(input("1.Manager \n2.Staff \n3.Customer \n4.Quit \n=>"))
    if z == 1:
        option = input("Enter the password.")
        if option == "noah" or option == "Noah" or option == "NOAH":
            print("welcome")
            manager(option)
        else:
            print("Invalid Password")
    elif z == 2:
        option = int(input("Enter your ID"))
        if option in range(1,16):
            print("Access Granted")
            cursor.execute("Select Name from employees where ID =%d"%(option))
            d=cursor.fetchall()
            print("Welcome Mr./Ms.%s"%(d[0]))
            staff(option)
        else:
            print("ID not found")
    elif z ==3:
        print("Welcome to our Nexa showroom")
        option = input("To view available item, Press any key")
        customer(option)
    else:
        print("Thanks for visiting our program")
        break    

# Close the database connection
db.close()
