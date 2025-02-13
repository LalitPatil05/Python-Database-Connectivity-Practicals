# Description :-

# Demonstration of Perform the Any Query into the our Application side
# they can reflected to the database side by using the cursor() method.
# demonstration of cursor() method
# the cursor method also contain a one that execute() method
# the execute() method in which we can type the query and it reflected on database side
'''
Steps to Perform the Query :-
    1. Establish the Connection
        - connect(host, username, password)
    2. Create the cursor object
        - db_cursor = mysql.connector.cursor()
    3. Execute the Query Using the execute() method
        - dbcursor.execute("SQL Query")
'''

# Implementation Code :-

import mysql.connector as mycon

# 1. Get the Connection
db_obj = mycon.connect(host="localhost", username="root", password="admin")
print("Connection Established Successfully...!!")

# 2. Create a Cursor Object
cursor_obj = db_obj.cursor()
print("Cursor Object Created Successfully...!!")

# 3. Execute the Query
cursor_obj.execute("create database Componey")
print("Query Executed Successfully...!!")
