import mysql.connector

def startConnection():
    mydb = mysql.connector.connect(
        host="",
        user="",
        password="",
        port=3306,
        database=""
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
