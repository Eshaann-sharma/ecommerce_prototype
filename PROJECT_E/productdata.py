import mysql.connector
import random as r

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Thunderbolt224",
  database="arcedia"
)

sql = mydb.cursor()

def qtygen():
    randomvalue=r.randrange(10,100)
    return randomvalue

products=[
    #Keyboard
    (1000,"SteelSeries Apex Pro Mechanical Gaming Keyboard",1499, "SteelSeries", "kb1.gif", qtygen(), "Keyboard"),
    (1001,"Razer Huntsman Mini White Cliky Optical",1499, "Razer", "kb2.gif", qtygen(), "Keyboard"),
    #Mouse
    (1005,"Razer Basilisk",1499, "Razer", "m1.gif", qtygen(), "Mouse"),
    (1006,"Logitech G502",1499, "Logitech", "m2.gif", qtygen(), "Mouse"),
    (1007,"AW610M Gaming Mouse",1499, "Alienware", "m3.gif", qtygen(), "Mouse"),
    #Headset
    (1009,"Logitech Pro X Wired Gaming Headset",1499, "Logitech", "hd1.gif", qtygen(), "Headphone"),
    (1010,"Logitech G733 Wireless Gaming Headset",1499, "Logitech", "hd2.gif", qtygen(), "Headphone"),
    (1012,"Logitech G335 Wired Lightweight",1499, "Logitech", "hd4.gif", qtygen(), "Headphone"),
    #Graphic Card
    (1014,"MSI GeForce RTX Ti 12GB",1499, "Nvidia", "gc1.gif", qtygen(), "GraphicCard"),
    (1015,"Asus GDDR5 GTX 750",1499, "Asus", "gc2.gif", qtygen(), "GraphicCard"),
    (1016,"MSI GeForce GTX 1070 Ti 8GB",1499, "Nvidia", "gc3.gif", qtygen(), "GraphicCard"),
    #Games
    (1019,"Super Mario Odyssey",1499, "Nintendo", "gn1.gif", qtygen(), "Game"),
    (1020,"Minecraft",1499, "Nintendo", "gn2.gif", qtygen(), "Game"),
    (1021,"Carnival Games",1499, "Nintendo", "gn3.gif", qtygen(), "Game"),
    (1022,"Mario and Sonic: Olympic Games",1499, "Nintendo", "gn4.gif", qtygen(), "Game"),
    #Softwares
    (1024,"Photos Recovery",1499, "Unknown", "s1.gif", qtygen(), "Software"),
    (1025,"McAfee: Total Protection (1 Year)",1499, "McAfee", "s2.gif", qtygen(), "Software"),
    (1026,"Duplicate File Fixer",1499, "Unknown", "s3.gif", qtygen(), "Software"),
    #Desk
    (1029,"Eureka Ergonomic Z60 Gaming Desk",1499, "NULL", "t1.gif", qtygen(), "Desk"),
    (1030,"GTRACING Gaming Desk",1499, "NULL", "t2.gif", qtygen(), "Desk"),
    #Chair
    (1034,"Razer Gaming Chair",39999, "Razer", "c1.gif", qtygen(), "Chair"),
    (1035,"Drogo Gaming Chair",1499, "Drogo", "c2.gif", qtygen(), "Chair"),
    (1036,"Haraga Gaming Chair",1499, "Unknown", "c3.gif", qtygen(), "Chair"),
    #Misc
    (1040,"Full Gaming Set ",99999, "Logitech", "g1.gif", 5, "Full"),
    (1041,"Full Gaming Set", 99999, "Logitech", "g2.gif", 5, "Full")
]

sql.execute("create table product (pid int primary key, pname varchar(64) not null, price int not null, seller varchar(32), img varchar(255) not null, qty int, cat varchar(32));")

qry=("insert into product(pid,pname,price,seller,img,qty,cat) values (%s,%s,%s,%s,%s,%s,%s)")

sql.executemany(qry,products)

mydb.commit()

sql.execute("select * from product;")

data=sql.fetchall()

for i in data:
    print(i)
##sql.execute("show tables;")
##
##for i in sql:
##    print(i)

print("EOP")
