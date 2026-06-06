import sqlite3

conn = sqlite3.connect("stress_history.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM predictions")

rows = cursor.fetchall()

print("Total Records:", len(rows))

for row in rows:
    print(row)

conn.close()