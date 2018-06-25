import MySQLdb
db=MySQLdb.connect(user="root",passwd="root",db="employees")
cur=db.cursor()
cur.execute("select * from examples")
for row in cur.fetchall():
        print row[0]," ",row[1]

