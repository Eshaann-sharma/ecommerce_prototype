import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Thunderbolt224",
  database="arcedia"
)

cur = mydb.cursor()

cur.execute("CREATE TABLE purchase_log (orderid INT AUTO_INCREMENT PRIMARY KEY,pid INT, pname VARCHAR(255), uname VARCHAR(32) NOT NULL,uid INT);")