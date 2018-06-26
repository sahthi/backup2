import MySQLdb, subprocess, re, sys, time, telnetlib

def tel_connect():
	tn = telnetlib.Telnet("linuxzoo.net")
	tn.read_until("login: ")
	tn.write("root"+"\n")
	tn.read_until("Password: ")
	tn.write("secure"+"\n")
	tn.read_until("# ")

	return tn

def get_date():
	tn = tel_connect()
	tn.write("date"+"\n")
	return tn.read_until("# ")


def get_ut_fa():
	tn = tel_connect()
	tn.write("uptime"+"\n")
	u_out = tn.read_until("# ")
	mat = re.search(r"up\s(.+?),.+load\saverage:\s(.+?),", u_out)
	utime = mat.group(1)
	fma = mat.group(2)

	return utime, fma

def insert_to_db():
	cdate = get_date()
	for line in cdate.split("\r\n"):
		mat = re.search(r"\w{3}\s+\d{1,2}\s+\w{3}\s+\d{2}:\d{2}:\d{2}\s+\w+\s\d{4}", line)
		if mat:
			cdate = mat.group()
			break
		
	utime, fma = get_ut_fa()
	conn = MySQLdb.connect(user="root", passwd="root", db="students")
	c = conn.cursor()
	c.execute('insert into system_info (cdate, utime, fma) values(%s, %s, %s)', (cdate, utime, fma))
	conn.commit()
	conn.close()

tel_connect()
print get_date()


if __name__ == "__main__":
     insert_to_db()

