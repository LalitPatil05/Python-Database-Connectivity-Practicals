# Description :-

# Demonstration of How to Insert the Multiple Values into the Table
# values are passed into the application side and this stored into the database
# In this we can store the multiple values at time to creating the list of datas
# in the list create a seprate tuple for every record for the table
# in which we can use the executemany(insert_query(%s,%s) , insert_list) method to insert the records
# insert_1uery in which we can store the insert query for the actual specifiers
# and the insert_list in which we can store the multiple records into the form of tuple and every tuple store in list

'''

Steps for Insert the Multiple Records into the Table at Time

1. Established the Connection
    - con_obj = mysql.connector.connect(host,username,password,database)

2. Create Cursor Object
    - crsr_obj = cursor()

3. Execute the Query
    - Create the first variable that in which we can store the command of sql 
    - eg. query = "insert into employee values(%s,%s,%s)"
    - Create the Second variable as a list in which we can store multiple records in the form of seprate tuple
    - eg. record_list = [(1,'a',100),(2,'b',200)(3,'c',300)]
    - again this two parameter are passed into the executemany() method
        eg. crsr_obj.executemany(query, record_list)

4. Commit the Changes
    - con_obj.commit()

'''

# Implementation Code :-

import mysql.connector as db

# 1. Get the Connection
con_obj = db.connect(host="localhost", username="root", password="admin", database="componey")
print("Database Connection Successfull...!!")

# 2. Create the Cursor Object
crsr_obj = con_obj.cursor()
print("Create Cursor Object Successfully...!!")

# 3. Execute the Query
query = "insert into employee values (%s,%s,%s)"
record_list = [(3,"Sumit",30000), (4,"Dipak",40000), (5,"Chetan",60000)]
crsr_obj.executemany(query, record_list)
print("Query Executed Successfully...!!")

# 4. Commit the Changes
con_obj.commit()
print("Commit All Changes Successfully...!!")