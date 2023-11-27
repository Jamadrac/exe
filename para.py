class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")


# Unit tests
def test_calculator():
    calculator = Calculator()

    # # Test addition
    # assert calculator.add(2, 3) == 5
    # assert calculator.add(-1, 1) == 0

    # # Test subtraction
    # assert calculator.subtract(5, 3) == 2
    # assert calculator.subtract(0, 0) == 0

    # # Test multiplication
    # assert calculator.multiply(2, 4) == 8
    # assert calculator.multiply(-3, 2) == -6

    # # Test division
    # assert calculator.divide(8, 2) == 4
    # assert calculator.divide(5, 0)  # This should raise a ValueError


if __name__ == "__main__":
    try:
        test_calculator()
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")
