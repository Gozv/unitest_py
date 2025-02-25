import pytest
from src.string_manipulator import StringManipulator

class TestStringManipulator:
    @pytest.fixture
    def manipulator(self):
        return StringManipulator()

    def test_reverse_string(self, manipulator):
        """Prueba la inversión de cadena normal"""
        assert manipulator.reverse_string("hello") == "olleh"
        assert manipulator.reverse_string("12345") == "54321"

    def test_reverse_string_invalid_input(self, manipulator):
        """Prueba con entrada inválida"""
        with pytest.raises(TypeError):
            manipulator.reverse_string(123)

    @pytest.mark.parametrize("input_str,expected", [
        ("radar", True),
        ("Anita lava la tina", True),
        ("hello", False),
        ("A", True),
        ("", True)
    ])
    def test_is_palindrome(self, input_str, expected, manipulator):
        """Prueba múltiples casos para palíndromos"""
        assert manipulator.is_palindrome(input_str) == expected