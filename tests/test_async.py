import pytest
from src.string_manipulator import StringManipulator

class TestAsyncOperations:
    @pytest.mark.asyncio
    async def test_async_palindrome_check(self):
        manipulator = StringManipulator()
        assert await manipulator.is_palindrome_async('radar') is True
    
    @pytest.mark.asyncio
    async def test_async_reverse_string(self):
        manipulator = StringManipulator()
        result = await manipulator.reverse_string_async('hello')
        assert result == 'olleh'