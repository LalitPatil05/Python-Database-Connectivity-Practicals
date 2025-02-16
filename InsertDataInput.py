# Description :-

# Demonstration of How to insert the Data into the table
# by the giving the User input insert query in Sql command

'''
Steps to Insert the Data into table :

1. Get the Connection
    - con_obj = mysql.connector.connect(host,username,password,database)

2. Create Cursor Object
    - crsr_obj = con_obj.cursor()

3. Execute the Query
    - First of all take the input from user
    - this values are put into the query
    - execute the query
    - crsr_obj.execute("insert into employee values(%s,%s,%s)",(value1,value2,value3))

'''

# Implementation Code :-

import mysql.connector as db

# 1. Get the Connection
con_obj = db.connect(host="localhost", username="root", password="admin", database="componey")
print("Database Connection Successfully...!!")

# 2. Create the Cursor() Object
crsr_obj = con_obj.cursor()
print("Create Cursor Object Successfully...!!")

# 3. Execute the Query
id = input("Enter the Employee id : ")
name = input("Enter the Employee Name : ")
salary = input("Enter the Employee Salary : ")
crsr_obj.execute("insert into employee values(%s,%s,%s)",(id,name,salary))
print("Query Executed Successfully...!!")

# 4. Commit the Changes
con_obj.commit()
print("Commit the Data and Save it Successfully...!!")
