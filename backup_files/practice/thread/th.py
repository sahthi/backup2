import threading
import time 
class mythread(threading.Thread):
       def __init__(self,i):	
              threading.Thread.__init__(self)
              self.h=i
       def run(self):
              print"value send:",self.h
thread1=mythread(1)
thread1.start()
thread2=mythread(2)
thread2.start()
       
