def add(a, b):
    return a + b

def test_add():
    result = add(1, 2)
    assert result == 3, f"Error: {1} + {2} expected 3, but got {result}"

    result = add(1, -1)
    assert result == 0, f"Error: {1} + {-1} expected 0, but got {result}"
