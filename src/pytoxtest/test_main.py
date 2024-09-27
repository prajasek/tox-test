import pytest 
from pytoxtest.main import add

def test_add():
    result = add(1,2)
    assert result == 3

def test_add2():
    assert(add(1.1,2) == 3.1)

@pytest.fixture
def values_fix():
    return [1,2,3]

@pytest.fixture
def test_values(values_fix):
    values_fix.append(4)
    assert [1,2,3,4] == values_fix
    return values_fix

def test_values1(test_values, values_fix):
    values_fix.append(5)
    assert [1,2,3,4, 5] == values_fix

    