"""
Tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)
        assert 10 == calculator.add(5, 5)
        assert 23 == calculator.add(10, 3)

    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)
        assert 3 == calculator.subtract(26, 23)
        assert 4 == calculator.subtract(12, 8)

    def test_multiply(self):
        assert 4 == calculator.multiply(2, 2)
        assert 21 == calculator.multiply(7, 14)
        assert 6 == calculator.multiply(3, 2)

    def test_divide(self):
        assert 4 == calculator.divide(16, 4)
        assert 3 == calculator.divide(9, 3)
        assert 20 == calculator.divide(60, 3)
