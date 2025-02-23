import sqlite3

connection = sqlite3.connect("itstep_sl3", 5)
cur = connection.cursor()
cur.execute("SELECT rowid name FROM first_table;")
connection.commit()
print(connection)
print(cur)
connection.close()