# importing the threading module
import threading
 
def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))
 
def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))
 
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    print t1
    t2 = threading.Thread(target=print_cube, args=(10,))
    print t2 
    # starting thread 1
    t1.start()
    print t1
    # starting thread 2
    t2.start()
    print t2
    # wait until thread 1 is completely executed
    t1.join()
    print t1
    # wait until thread 2 is completely executed
    t2.join()
    print t2
    # both threads completely executed
    
    print("Done!")
