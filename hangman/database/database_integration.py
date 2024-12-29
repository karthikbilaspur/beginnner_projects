import sqlite3

class DatabaseIntegration:
    def __init__(self):
        self.conn = sqlite3.connect("user_data.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """)
        self.conn.commit()

    def insert_user(self, username, password):
        self.cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        self.conn.commit()

# Example usage
database_integration = DatabaseIntegration()
database_integration.create_table()
database_integration.insert_user("john", "password123")