from .foo import bar as b
from ..foo1 import bar as b1

class Foo(object):

    def __init__(self):
        """This is a test
        """
        super().__init__()

    def alpha(self):
        for _, i in enumerate(['a', 'b'], start=1):
          print(f"#{i}")


def test_a(b='test'):
    a = [1, 2, 3]
    return None

# test
test_a()
f = Foo()
f.alpha()
