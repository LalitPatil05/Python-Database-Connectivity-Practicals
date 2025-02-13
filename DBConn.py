import mysql.connector

con = mysql.connector.connect(host ='localhost' , password='admin', user='root')

if con.is_connected():
    print("Python Database Connectivity Successful..!!")
    print("Connection is Successfull..!!")
    print("Connection ID : ",con)
