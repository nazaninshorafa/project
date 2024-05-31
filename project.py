import mysql.connector 

mydb = mysql.connector.connect(
    host = "local host" , 
    user = " root " , 
    password = " pass "
)

mycursor = mydb.cursor1()