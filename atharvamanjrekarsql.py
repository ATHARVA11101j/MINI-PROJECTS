
# Task 1: Database Connection and Configuration

import mysql.connector
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "assigment"
}

try:
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Connected to MySQL database successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
        
# Task 2:Creating and Managing Tables: Orders, Customer

import sqlite3

conn = sqlite3.connect('assigment')
cursor = conn.cursor()


cursor.execute('''
create table Customers (
    Customerid int primary key,
    Firstname text,
    Lastname text,
    Email text,
    Phone int
)
''')


cursor.execute('''
create table Orders (
Orderid int primary key, 
Customerid int,                
Orderdate date,            
Totalamount decimal(10, 2),      
Orderstatus varchar(50),          
foreign key (Customerid) references Customers(Customerid)
)
''')

conn.commit()

cursor.execute('''
insert into Customers (FirstName, LastName, Email, Phone)
values
('John', 'Doe', 'johndoe@example.com', '123-456-7890'),
('Jane', 'Smith', 'janesmith@example.com', '987-654-3210')
''')

cursor.execute('''
insert into Orders (Customerid, Orderdate, Totalamount, Orderstatus)
values
(1, '2025-03-06', 250.00, 'Pending'),
(2, '2025-03-05', 180.00, 'Shipped')
''')

conn.commit()


cursor.execute('''
select Orders.Orderid, Customers.Firstname, Customers.Lastname, Orders.OrderDate, Orders.Totalamount, Orders.Orderstatus
from Orders
join Customers ON Orders.Customerid = Customers.Customerid
''')

orders = cursor.fetchall()
for order in orders:
    print(order)

conn.close()


import sqlite3

conn = sqlite3.connect('business.db')
cursor = conn.cursor()


# Task 3: Data Manipulation and Queries
import sqlite3

conn = sqlite3.connect('business.db')
cursor = conn.cursor()

# Insert New Orders

def insert_new_order(customer_id, order_date, total_amount, order_status):
    cursor.execute('''
    insert into Orders (Customerid, Orderdate, Totalamount, Orderstatus)
    values (?, ?, ?, ?)
    ''', (customer_id, order_date, total_amount, order_status))
    
    conn.commit()

insert_new_order(1, '2025-03-07', 300.00, 'Pending')

# insert New Customers

def insert_new_customer(first_name, last_name, email, phone, address, city, country):
    cursor.execute('''
    insert into Customers (Firstname, Lastname, Email, Phone)
    values (?, ?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, email, phone, address, city, country))
    
    conn.commit()

insert_new_customer('Alice', 'Johnson', 'alicejohnson@example.com', '555-987-6543')

# Fetch Customer Orders

def fetch_customer_orders(customer_id):
    cursor.execute('''
    select Orders.Orderid, Orders.Orderdate, Orders.Totalamount, Orders.Orderstatus
    from Orders
    where Orders.Customerid = ?
    ''', (customer_id,))
    
    orders = cursor.fetchall()
    
    if orders:
        for order in orders:
            print(order)
    else:
        print("No orders found for this customer.")

fetch_customer_orders(1)

# Update an Order’s Status

def update_order_status(order_id, new_status):
    cursor.execute('''
    update Orders
    set OrderStatus = ?
    where OrderID = ?
    ''', (new_status, order_id))
    
    conn.commit()

update_order_status(1, 'Shipped')

conn.close()


# Task 4: Advanced Operations

# Retrieve All Orders for a Specific Date Range

def get_orders_by_date_range(start_date, end_date):
    cursor.execute('''
    select Orders.Orderid, Customers.Firstname, Customers.Lastname, Orders.Orderdate, Orders.Totalamount, Orders.Orderstatus
    from Orders
    join Customers ON Orders.Customerid = Customers.Customerid
    where Orders.Orderdate BETWEEN ? AND ?
    ''', (start_date, end_date))

    orders = cursor.fetchall()
    if orders:
        for order in orders:
            print(order)
    else:
        print("No orders found within the specified date range.")

get_orders_by_date_range('2025-03-01', '2025-03-10')

# Find the Total Sales for a Given Month

def get_total_sales_for_month(year, month):
    cursor.execute('''
    select SUM(Totalamount)
    from Orders
    where strftime('%Y', Orderdate) = ? AND strftime('%m', Orderdate) = ?
    ''', (year, month))

    total_sales = cursor.fetchone()[0]
    if total_sales:
        print(f"Total sales for {month}/{year}: ${total_sales:.2f}")
    else:
        print(f"No orders found for {month}/{year}.")


get_total_sales_for_month('2025', '03')

# Find the Most Expensive Order

def get_most_expensive_order():
    cursor.execute('''
    select Orders.Orderid, Customers.Firstname, Customers.Lastname, Orders.Orderdate, Orders.Totalamount, Orders.Orderstatus
    from Orders
    join Customers ON Orders.Customerid = Customers.Customerid
    order BY Orders.Totalamount DESC
    LIMIT 1
    ''')

    order = cursor.fetchone()
    if order:
        print(f"The most expensive order is: {order}")
    else:
        print("No orders found.")

get_most_expensive_order()

# Use Different Joins with Customers

def inner_join_orders_customers():
    cursor.execute('''
    select Orders.Orderid, Customers.Firstname, Customers.Lastname, Orders.Orderdate, Orders.Totalamount, Orders.Orderstatus
    from Orders
    inner join Customers ON Orders.Customerid = Customers.Customerid
    ''')

    orders = cursor.fetchall()
    if orders:
        for order in orders:
            print(order)
    else:
        print("No matching orders and customers found.")

inner_join_orders_customers()

def left_join_orders_customers():
    cursor.execute('''
    select Customers.Customerid, Customers.Firstname, Customers.Lastname, Orders.Orderid, Orders.Orderdate, Orders.Totalamount
    from Customers
    left join Orders ON Customers.Customerid = Orders.Customerid
    ''')

    orders = cursor.fetchall()
    if orders:
        for order in orders:
            print(order)
    else:
        print("No customers or orders found.")

left_join_orders_customers()

def right_join_orders_customers():
    cursor.execute('''
    select Orders.Orderid, Orders.Orderdate, Orders.Totalamount, Customers.Customerid, Customers.Firstname, Customers.Lastname
    from Orders
    left join Customers ON Orders.Customerid = Customers.Customerid
    ''')

    orders = cursor.fetchall()
    if orders:
        for order in orders:
            print(order)
    else:
        print("No orders or customers found.")

right_join_orders_customers()
