import pytest 
from pytoxtest.main import add

def test_add():
    result = add(1,2)
    assert result == 3

def test_add2():
    assert(add(1.1,2) == 3.1)

def test_add3():
    with pytest.raises(Exception):
       add(1+ "")
