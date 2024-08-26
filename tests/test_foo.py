import sys
import os
import pytest
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.lib import Foo

def test_footest():
    f = Foo()
    assert (f.footest() == True)