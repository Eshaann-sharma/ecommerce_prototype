import mysql.connector

#random UID will be done once we have the program ready to go to preven creating duplicate values during testing

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abcd1234",
  database="arcedia"
)

users=[
    (1000,"User01","1234","abc@gmail.com","Fullname1"),
    (2000,"User02","1234","abcd@gmail.com","Fullname2"),
    (3000,"User03","1234","abce@gmail.com","Fullname3"),
    (4000,"User04","1234","abcf@gmail.com","Fullname4"),
    (5000,"User05","1234","abcg@gmail.com","Fullname5")
]

qry="insert into user (uid, uname, pwd, eml, fullname) values (%s,%s,%s,%s,%s);"

sql=mydb.cursor()

sql.execute("create table user (uid int not null, uname varchar(30) unique, pwd varchar(64), eml varchar(255) unique, fullname varchar(64));")

for i in range(len(users)):
    sql.execute(qry,users[i])
    mydb.commit()


sql.execute("select * from user;")

data=sql.fetchall()

for i in data:
    print(i)
##sql.execute("show tables;")
##
##for i in sql:
##    print(i)


print("EOP")
