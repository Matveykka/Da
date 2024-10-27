# logic.py

import sqlite3
from config import DATABASE

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                description TEXT
            )
        ''')
        self.connection.commit()

    def close(self):
        self.connection.close()

        if __name__ == '__main__':
            manager = DB_Manager(DATABASE)
            manager.create_tables()