# Description :-

# Demonstration of How to crate the table in database using the python.
# in which we can perform operation on application side and they can
# reflected to the database side using the mysql database connector

'''
Steps to Create table into Database :
    1. Establish the Connection
        mysql.connector.connect(host, username, password, database)
    2. Create the Cursor object
        - crsr_obj = mysql.connector.cursor()
    3. Execute the Query 
        - crsr_ob.execute(SQL Query)

'''

# Implementation Code :-

import mysql.connector as db

# 1. Get the Connection
con_obj = db.connect(host="localhost", username="root", password="admin", database="componey")
print("Database Connection Established...!!")

# 2 Create the Cursor Object
crsr_obj = con_obj.cursor()
print("Cursor Object Created Successfully...!!")

# 3. Execute the Query
crsr_obj.execute("create table employee(id int, name varchar(20), salary int)")
print("Query Executed Successfully...!!") 