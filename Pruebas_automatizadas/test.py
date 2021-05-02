from algoritmos1 import fibonacci, palindromo, factorial

def test_fibonacci_cinco():
    assert fibonacci(5) == 5

def test_palindromo_anita():
    assert palindromo("Anita lava la tina")

def test_factorial_cinco():
    assert factorial(5) == 120
