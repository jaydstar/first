import mysql.connector
from cryptography.fernet import Fernet


mydb = mysql.connector.connect(
  host="127.0.0.1",
  port="3306",
  db='mydatabase',
  user="root",
  password="password"
)


mycursor = mydb.cursor()
mycursor.execute("SELECT token FROM encrytp")
myresult = mycursor.fetchall()
key = myresult
print (myresult)


mycursor = mydb.cursor()
mycursor.execute("SELECT msg FROM encrytp")
myresult1 = mycursor.fetchall()
print (myresult1)

f = Fernet(key)
#token =f.decrypt(myresult1)
#print (token)