import pytest
from src.db_handler import DatabaseHandler

class TestDatabaseHandler:
    @pytest.fixture
    def db_handler(self):
        return DatabaseHandler()
    
    def test_user_insertion(self, db_handler):
        with db_handler.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name) VALUES ('test')")
            conn.commit()
        
        users = db_handler.get_users()
        assert len(users) == 1
        assert users[0][1] == 'test'
    
    @pytest.mark.asyncio
    async def test_async_insert(self, db_handler):
        await db_handler.async_insert_user('async_test')
        users = db_handler.get_users()
        assert any(user[1] == 'async_test' for user in users)