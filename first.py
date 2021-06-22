import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port="3306",
  db='jdb',
  user="root",
  password="password"
)

#print(mydb)

mycursor = mydb.cursor()

#1mycursor.execute("CREATE DATABASE mydatabase")
#2mycursor.execute("SHOW DATABASES")
#2for x in mycursor:
#2 print(x)
#3mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Jake", "Highway 22")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")