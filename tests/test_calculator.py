import pytest
from src.calculator import Calculator

class TestCalculator:
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (2.5, 3.5, 6)
    ])
    def test_add(self, a, b, expected):
        """Prueba la función de suma con diferentes casos"""
        assert Calculator.add(a, b) == expected

    def test_subtract(self):
        """Prueba la función de resta"""
        assert Calculator.subtract(5, 3) == 2

    def test_multiply(self):
        """Prueba la función de multiplicación"""
        assert Calculator.multiply(3, 4) == 12

    def test_divide_normal_case(self):
        """Prueba la división normal"""
        assert Calculator.divide(10, 2) == 5

    def test_divide_by_zero(self):
        """Prueba la división por cero"""
        with pytest.raises(ValueError) as exc_info:
            Calculator.divide(10, 0)
        assert "No se puede dividir por cero" in str(exc_info.value)