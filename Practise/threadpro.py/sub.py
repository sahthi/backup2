import subprocess
import MySQLdb,sys,re,time

def get_time():
    return time.ctime()


def get_ut():
     op=subprocess.Popen(["uptime"],stdout=subprocess.PIPE)
     out,err=op.communicate()
     if err:
          print "error in command execution"
          sys.exit(100)

     mat = re.search(r"up\s(.+?),.+load\saverage:\s(.+?),", out)
     utime=mat.group(1)
     fm_avg=mat.group(2)

     return utime,fm_avg

def insert_to_db():
     curr_date=get_time()
     utime,fm_avg=get_ut()
     conn=MySQLdb.connect(user="root",passwd="root",db="students")
     c=conn.cursor()
     c.execute('insert into system_info(utime,fma) values(%s,%s)',(utime,fm_avg))
     conn.commit()
     conn.close()

if __name__ == "__main__":
     insert_to_db()



