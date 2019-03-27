from sqlite3 import *

konekcija = connect("skola.db")

kursor = konekcija.cursor()

sql = "CREATE TABLE evidencija ("
sql += "ID INTEGER PRIMARY KEY AUTOINCREMENT,"
sql += "IME TEXT,"
sql += "PREZIME TEXT,"
sql += "DATUM DATE)"

kursor.execute(sql)
konekcija.close()