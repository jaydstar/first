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

#mycursor.execute("CREATE TABLE encrytp (token VARCHAR(255), msg VARCHAR(255))")

key = Fernet.generate_key()
print(key)

f = Fernet(key)
token = f.encrypt(b"hello")
print (token)


sql = "INSERT INTO encrytp (token, msg) VALUES (%s, %s)"
val = (key, token)
mycursor.execute(sql, val)

mydb.commit()





