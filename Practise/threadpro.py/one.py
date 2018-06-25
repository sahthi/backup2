import threading
import time

def f1():
    print threading.currentThread().getname(), 'Starting'
    print threading.currentThread()
    time.sleep(1)
    print threading.currentThread().getName(), 'Exiting'

def f2():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

def f3():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(3)
    print threading.currentThread().getName(), 'Exiting'

t1 = threading.Thread(target=f1) # use default name
t2 = threading.Thread(name='f2', target=f2)
t3 = threading.Thread(name='f3', target=f3)

t1.start()
t2.start()
t3.start()
