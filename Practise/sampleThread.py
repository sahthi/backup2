import Threading
import time
exitflag=0
class myThread(threading.Thread):
      def __init__(self,threadId,name,counter):
           threading.Thread.__init__(self)
           self.threadId=threadId
           self.name=name
           self.counter=counter
      def run(self):
           print "starting:" +self.name
           print_time(self.name,5,self.counter)
           print"exiting:" +self.name
      def print_time(name,counter,delay):
           while counter:
                if exitflag:
                      threadname.exit()
                time.sleep(delay)
                print "%s:%s" %(threadName,time.ctime(time.time())
                counter -= 1
thread1=myThread(1,"Thread-1",1)
thread2=myThread(2,"Thread-2",2)
thread1.start()
thread2.start()
print "exiting main thread"

   

 

