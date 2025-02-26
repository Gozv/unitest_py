import sqlite3
import aiosqlite
from contextlib import contextmanager

class DatabaseHandler:
    def __init__(self, db_path=':memory:'):
        self.db_path = db_path
    
    @contextmanager
    def connect(self):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
            conn.commit()
            yield conn
        finally:
            conn.close()
    
    async def async_insert_user(self, name):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute('INSERT INTO users (name) VALUES (?)', (name,))
            await db.commit()
    
    def get_users(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()