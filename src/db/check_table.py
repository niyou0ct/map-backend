import sqlite3

dbname = 'TEST.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('SELECT * FROM persons')

print(cur.fetchall())

cur.close()
conn.close()