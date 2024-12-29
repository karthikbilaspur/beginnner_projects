import sqlite3

class UserProfiles:
    def __init__(self):
        self.conn = sqlite3.connect("user_data.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_progress (
                username TEXT PRIMARY KEY,
                wins INTEGER,
                losses INTEGER,
                achievements TEXT
            )
        """)
        self.conn.commit()

    def update_progress(self, username, wins, losses, achievements):
        self.cursor.execute("""
            INSERT OR REPLACE INTO user_progress (username, wins, losses, achievements)
            VALUES (?, ?, ?, ?)
        """, (username, wins, losses, achievements))
        self.conn.commit()

    def get_progress(self, username):
        self.cursor.execute("SELECT * FROM user_progress WHERE username=?", (username,))
        return self.cursor.fetchone()

# Example usage
user_profiles = UserProfiles()
user_profiles.create_table()
user_profiles.update_progress("john", 10, 5, "Newbie")
progress = user_profiles.get_progress("john")