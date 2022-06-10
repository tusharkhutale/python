#from dbm import _Database
import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",passwd="root",database="python_schema")
cur = conn.cursor()
cur.execute("create table students(rollno int primary key, name varchar(30), percentage float, branch varchar(10))")
conn.close()