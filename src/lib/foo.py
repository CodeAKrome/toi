from .bar import Bar

class Foo:
    def __init__(self):
        self.k = 1
        self.bar = Bar
        
    def footest(self):
        print("foo")
        self.bar.bartest()
        return True
