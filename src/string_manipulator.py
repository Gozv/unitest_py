class StringManipulator:
    @staticmethod
    def reverse_string(s: str) -> str:
        if not isinstance(s, str):
            raise TypeError("La entrada debe ser una cadena")
        return s[::-1]

    @staticmethod
    def is_palindrome(s: str) -> bool:
        s = s.replace(" ", "").lower()
        return s == s[::-1]