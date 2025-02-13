# Description :-

# Connect the Python Application into the Database
# Using the MySql Database Server
# Established the Connection Using the mysql.connector
# to Establish the Connectivity between python and mysql by using the connect method
# using connectivity we can perform the various operations into database through the application side

'''

Steps to Establish the Connection between Database and Python Application

1. Get the Connection
    - mysql.connector.connect(host, username, password)

'''

# Implementation Code :-

import mysql.connector as mycon

conobj = mycon.connect(host="localhost", user="root", password="admin")

print("Connection Established Successfully...!!")
print("Connection Id is : ",conobj)