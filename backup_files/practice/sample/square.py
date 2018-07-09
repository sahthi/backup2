class shape(object):
    def __init__(self):
         pass
    def area(self):
         return 0
class square(shape):
    def __init__(self,l):
        self.length=l
    def area(self):
        return self.length*self.length
s=square(3)
print s.area()

