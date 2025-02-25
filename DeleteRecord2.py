# Description :-

# Demonstration of How to delete the Record in table into our application side
# in which we can use the delete query for sql to delete the record into table
# we can pass the query at the user application and changes made to database side
# finally all changes are done then in the end commit the all the changes.

'''

Steps for Delete the Data into Our Application

1. Establish the Connection
    - con_obj = mysql.connector.connect(host,username,password,database)

2. Create the Cursor() Object
    - crsr_obj = con_obj.cursor()

3. Execute the Query
    - first step we can pass the query at a one variable by actual/proper specifiers
    -e.g. query = "delete from table_name where id=%s"
    - in the second step give the value in tuple
    - eg. value = (,5)
    - then this two parameters are pass to the execute function for executing
        - crsr_obj.execute(query, value)
    
4. Commit the Changes
    - con_obj.commit()

'''

# Implementation Code :-

import mysql.connector as db

# 1. Get the Connection
con_obj = db.connect(host="localhost", username="root", password="admin", database="componey")
print("Connection Established Successfully...!!")

# 2. Create Cursor Object
crsr_obj = con_obj.cursor()
print("Object Created Successfully...!!")

# 3. Execute the Query
query = "delete from employee where id=%s"
value = ('5',)
crsr_obj.execute(query,value)
print("Query Executed Successfully...!!")

# 4. Commit the Changes
con_obj.commit()
print("Commit all Changes Successfully...!!")