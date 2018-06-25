import MySQLdb,re,sys,time,telnetlib

def tel_connect():
   
     tn=telnetlib.Telnet("linuxzoo.net")
     tn.read_until("login:"+"\n")
     tn.write("root")
     tn.read_until("password:"+"\n")
     tn.write("secure")
     tn.read_until("#")
      
     return tn

def get_date():

     tn = tel_connect()
     tn.write("date"+"\n")
     return  tn.read_until("#")

def get_ut():

     tn=tel_connect()
     tn.write("uptime"+"\n")
     u_out = tn.read_until("#")
     mat=re.search(r"up\s(.+?),.+load\s average:\s(.+?)",u_out)
     utime = mat.group(1)
     fm_avg=mat.group(2)
    
     return utime,fm_avg

def insert_to_db():
     cur_date=get_date()
     for line in cur_date.split("\r\n"):
           mat=re.search(r"\w{3}\s+\d{1,2}\s+\w{3}\s+\d{2}:\d{2}:\d{2}\s+\w+ \s+\d{4}")
           if mat:
                 cur_date=mat.group()
                 break
     utime,fm_avg=get_ut()
     conn=MySQLdb.connect(user="root",password="root",db="students")
     c = conn.cursor()
     c.execute('insert into system_info (cdate, utime, fma) values(%s, %s, %s)', (curr_date, utime, fm_avg))
     conn.commit()
     conn.close()

if __name__ == "__main__":
	insert_to_db()

    


 
    
    
   
      
