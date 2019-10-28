import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='root',
    port=8889,
    database='testdatabase'
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ('jack', 20))
db.commit()