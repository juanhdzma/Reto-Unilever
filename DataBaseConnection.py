import mysql.connector

def startConnection():
    mydb = mysql.connector.connect(
        host="sabanahack.c99opdt5oa43.us-east-1.rds.amazonaws.com",
        user="admin",
        password="admin1234",
        port=3306,
        database="SabanaHack"
    )
    return mydb

def selectQuery(query):
    mydb = startConnection()
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def selectVariableQuery(query, val):
    mydb = startConnection()
    mycursor = mydb.cursor()
    mycursor.execute(query, val)
    myresult = mycursor.fetchall()
    return myresult