# Demonstration of How to Update the Record in table into our application side
# in which we can use the update queru for sql to update the record into table
# we can pass the query at the user application and changes made to database side
# finally all updates are done then in the end commit the all the changes.

'''

Steps for Retrieve the Data into Our Application

1. Establish the Connection
    - con_obj = mysql.connector.connect(host,username,password,database)

2. Create the Cursor() Object
    - crsr_obj = con_obj.cursor()

3. Execute the Query
    - pass the sql query in execute method.
    eg. crsr_update.execute("update emp set name=%s where id=%s")
    
4. Commit the Changes
    - con_obj.commit()

'''

# Implementation Code :-

import mysql.connector as db

# 1. Get the Connection
con_obj = db.connect(host="localhost", username="root", password="admin", database="componey")

# 2. Create Cursor Object
crsr_obj = con_obj.cursor()

# 3. Execute the Query
crsr_obj.execute("update employee set name='Dhiraj' where id=5")
print("Query Executed Successfully...!!")

# 4. Commit the Changes
con_obj.commit()
print("Commit all Changes Successfully...!!")