# Description :-

# demonstration of how view the actual how many tables are created into the databases
# they can view at our application side using cursor, and execute.
# the tables are viewing using the for loop

'''
Steps to Show tables at our Application Side

1. Established the Connection
    - con_obj = mysql.connector.connect(host, username, password, database)

2. Create a Cursor Object
    - crsr_obj = con_obj.cursor

3. Execute the Query
    - crsr_obj.execute(SQL Query)
    - use the for loop to show the tables
    for i in crsr_obj:
        print(i)

'''

# Implementation Code :-

import mysql.connector as db

# 1. Get the Connection
con_obj = db.connect(host="localhost", username="root", password="admin", database="componey")
print("Database Connection Successfully...!!")

# 2. Create Cursor Object
crsr_obj = con_obj.cursor()
print("Cursor Object Created Successfully...!!")

# 3. Execute the Query
crsr_obj.execute("show tables")
print("Query Executed Successfully...!!")

print("Tables into the Databases : ")

for i in crsr_obj:
    print(i)
