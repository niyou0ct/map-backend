import sqlite3

dbname = 'TEST.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
cur.execute('INSERT INTO persons(name) values("Taro")')
cur.execute('INSERT INTO persons(name) values("Hanako")')
cur.execute('INSERT INTO persons(name) values("Hiroki")')

conn.commit()

cur.close()
conn.close()