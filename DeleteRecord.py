# Demonstration of How to Delete the Record into the Database
# The Row are deleted by using the delete query in sql
# using mysql_connector we can perform query at application side and this reflect on database side
# it is alsp same as like a update query

'''

Steps for Delete the Record into the Database :-

1. Establish the Connection
    - con_obj = mysql.connector.connect(host,username,password,database)

2. Create the Cursor() Object
    - crsr_obj = con_obj.cursor()

3. Execute the Query
    - pass the sql query in execute method.
    eg. crsr_update.execute("delete from employee where id=5")
    
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

# 3. Execute the Query
crsr_obj.execute("delete from employee where id=5")
print("Query Executed Successfully...!!")

# 4. Commit the Changes
con_obj.commit()
print("Commit all Changes Successfully...!!")