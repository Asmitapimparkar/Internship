import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="internship2"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Employ (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO Employ (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")