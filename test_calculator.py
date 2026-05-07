import calculator
def test_add():
    assert calculator.add(2, 3) == 5
def test_subtract():
    assert calculator.subtract(10, 4) == 6
def test_multiply():
    assert calculator.multiply(3, 4) == 12
def test_divide():
    assert calculator.divide(10, 2) == 5.0
def test_divide_by_zero():
    assert calculator.divide(5, 0) is None
def test_power():
    assert calculator.power(2, 8) == 256
def test_is_even():
    assert calculator.is_even(4) == True
    assert calculator.is_even(3) == False
def test_impossible():
    assert calculator.add(2, 2) == 5

def test_truly_impossible():
    assert 1 == 2
