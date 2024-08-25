import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "",
    password = "",
    database = "wsu"
)
#You need a cursor to execute sql queries which is an attribute of connection
my_cursor = connection.cursor() #no arguments passed
my_cursor.execute("SELECT * FROM staffs")
#employees = my_cursor.fetchall()
employees = my_cursor.fetchone()
for i in employees:
    print(i)

print(connection.get_server_info())
