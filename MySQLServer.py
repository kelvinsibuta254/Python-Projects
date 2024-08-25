import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "byg6zmXp@#$%",
    #database = "PhD"
)
my_cursor = connection.cursor()

my_cursor.execute("CREATE DATABASE sibuta_book_store;")
my_cursor.execute("USE sibuta_book_store;")

#result = my_cursor.fetchall() #fetching data from cursor and storing it in result object
# result = my_cursor.fetchone()

# for i in result:
#     print(i)

#print(connection.get_server_info())