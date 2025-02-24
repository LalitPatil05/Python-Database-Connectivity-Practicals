# Description :-

# Demonstration of how to Retrieve the data on our user application
# by using the select query we can see the all the data of the table
# in the ython we can use the fetchall() method to access the all the data from the table
# by using the fetchall method we can access the all the records of the database
# we can give the reference of database in the select command to access the data.

'''

Steps for Retrieve the Data into Our Application

1. Establish the Connection
    - con_obj = mysql.connector.connect(host,username,password,database)

2. Create the Cursor() Object
    - crsr_obj = con_obj.cursor()

3. Execute the Query
    - result_obj = crsr_obj.execute("select * from database.table_name")
    - print(result_obj)

'''

# Implementation Code :-

import mysql.connector as db

# 1. Get the Connection
con_obj = db.connect(host="localhost", username="root", password="admin", database="componey")
print("Connection Established Successfully...!!")

# 2. Create the Cursor Object
crsr_obj = con_obj.cursor()
print("Cursor Object Created Successfully...!!")

# 3. Execute the Query
crsr_obj.execute("select * from employee")
result_obj = crsr_obj.fetchall()

print("Query Executed Successfully...!!")
print()

print("Records of Table are : ")
print(result_obj)

print("By Using For Loop Print the Data")
for data in result_obj:
    print(data)
