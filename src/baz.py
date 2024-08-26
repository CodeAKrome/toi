from lib import Foo
import lib.log

def terry(obj):
    print("type:", type(obj))
    print("contents:", dir(obj))
    print("obj.__dict__:", obj.__dict__)
    
#terry(Foo)

f = Foo()
f.footest()
