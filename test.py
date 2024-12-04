import mysql.connector

conn = mysql.connector.connect(
    USER="nameer",PASSWORD="12345678",HOST='localhost', DB='author_wiki'
)

cur = conn.cursor(dictionary=True)
cur.execute('select * from author where id = 5')
print(cur.fetchone())