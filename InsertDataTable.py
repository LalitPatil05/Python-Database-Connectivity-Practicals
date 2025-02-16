# Description :-

# Demonstration of how to insert the data into the table using the insert query
# in which we can perform query on the user application side and
# this reflected into the database side
# in which we can use the SQL insert query

'''
Steps to insert the data into table

1. Established the Connection
   con_obj = mysql.connector.connect(host, username, password, database)

2. Create the Cursor Object
    crsr_obj = con_obj.cursor()

3. Execute the Query
    crsr_obj.execute(SQLQuery)
    insert into table_name values(value1, value2, ......, valuen)

4. Commit the changes
    - con_obj.commit()

'''

# Implementation Code :-

import mysql.connector as db

# 1. Get the Connection
con_obj = db.connect(host="localhost", username="root", password="admin", database="componey")
print("Connection Established Successfully...!!")

# 2. Create the Cursor Object
crsr_obj = con_obj.cursor()
print("Cursor Object Created Successfully....!!")

# 3. Execute the Query
crsr_obj.execute("insert into employee values(5, 'Chetan', 50000)")
print("Query Executed Successfully...!!")

# 4. Commit the Changes
con_obj.commit()