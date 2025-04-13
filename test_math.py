import math_functions

def test_add():
    assert math_functions.add(1, 2) == 3
    assert math_functions.add(-1, 1) == 0
    print("Add test passed!")

def test_multiply():
    assert math_functions.multiply(2, 3) == 6
    assert math_functions.multiply(0, 5) == 0
    print("Multiply test passed!")

def test_is_even():
    assert math_functions.is_even(2) == True
    assert math_functions.is_even(3) == False
    print("Is_even test passed!")

if __name__ == "__main__":
    test_add()
    test_multiply()
    test_is_even()
    print("All tests passed!")
