from app import even_or_odd

def test_even():
    assert even_or_odd(2) == "Even"

def test_odd():
    assert even_or_odd(3) == "Odd"

def test_zero():
    assert even_or_odd(0) == "Invalid Input"

def test_negative():
    assert even_or_odd(-1) == "Invalid Input"
