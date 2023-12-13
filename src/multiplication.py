def multiply(a, b):
    return a * b

def test_multiply():
    result = multiply(2, 3)
    assert result == 6, f"Error: {2} * {3} expected 6, but got {result}"

    result = multiply(-1, 4)
    assert result == -4, f"Error: {-1} * {4} expected -4, but got {result}"
