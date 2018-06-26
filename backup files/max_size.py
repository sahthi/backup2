class MaxSizeList(object):

    def __init__(self, max_length):
        self.max_length = max_length
        self.ls = []

    def push(self, st):
        if len(self.ls) == self.max_length:
            self.ls.pop(0)
        self.ls.append(st)

    def get_list(self):
        return self.ls
a = MaxSizeList(3)
a.push("hey")
a.push("hi")
a.push("skjdfh")
a.push("let's")
a.push("go")
a.push("dslkfjs")

print(a.get_list())
