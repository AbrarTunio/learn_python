import sqlite3

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS newTable")
cur.execute("CREATE TABLE newTable (email TEXT, Count INTEGER)")

fname = input("Enter file name: ")
if (len(fname) < 1):
    fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
    if not line.startswith("From: "): continue
    peices = line.split() #do not use split(" ") # WARNING: \n
    email = peices[1]
    cur.execute("SELECT Count FROM newTable WHERE email = ?" , (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO newTable (email,Count) VALUES (?,1)",(email,))
    else:
        cur.execute("UPDATE newTable SET count = count + 1 WHERE email = ?",
        (email,))
    conn.commit()

sqlstr = "SELECT email, Count FROM newTable ORDER BY Count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()
