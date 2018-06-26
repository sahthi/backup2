import MySQLdb

conn = MySQLdb.connect(user="root", passwd="root", db='employees')
c = conn.cursor()

with open("employees.txt", "r")as f:
	for line in f.readlines():
		line = line.strip()
		eid, name, designation, exp = line.split(',')
		c.execute('insert into employee_info(eid, name, designation, exp)values(%s, %s ,%s ,%s)', (eid, name, designation, exp))
		conn.commit()
		

conn.close()
