import MySQLdb
conn=MySQLdb.connect(user="root",passwd="root",db="employees")
c=conn.cursor()

with open("employee.txt", "r") as f:
     for line in f.readlines():
          line.strip()
          eid,name,designation,exp = line.split(',')
          c.execute("insert into employee_info (eid,name,designation,exp) values (%s,%s,%s,%s)",(eid,name,designation,exp))
          conn.commit()
conn.close()
     
