import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='root',
    port=8889,
    database='testdatabase'
)

mycursor = db.cursor()

