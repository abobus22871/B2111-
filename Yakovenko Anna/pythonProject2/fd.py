import sqlite3

connection = sqlite3.connect("itstep_sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
print(connection)
print(cur)
connection.close()