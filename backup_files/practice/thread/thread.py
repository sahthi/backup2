import threading
def print_cube(num):
     print("cube:{}".format(num*num*num))
def print_square(num):
     print("square:{}".format(num*num))
if __name__=="__main__":
     t1=threading.thread(target=print_square,args=(10,))
     t2=threading.thread(target=print_cube,args=(5,))
     t1.start()
     t2.start()
     t1.join()
     t2.join()
     print("done")
     


