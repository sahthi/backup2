from threading import*
def hello():
    print "helloworld"
t=Timer(10,hello)
t.start()
