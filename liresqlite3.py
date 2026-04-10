import sqlite3

# ouvrir la base
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# lister les tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# lire une table (exemple : BetsFaits)
cursor.execute("SELECT * FROM bets_faits;")
for row in cursor.fetchall():
    print(row)

conn.close()