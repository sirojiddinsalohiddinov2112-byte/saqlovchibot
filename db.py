import sqlite3
from datetime import datetime

conn = sqlite3.connect("backup.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    sender_id INTEGER,
    text TEXT,
    time TEXT
)
""")

conn.commit()

def save_message(user_id, sender_id, text):
    cur.execute("""
    INSERT INTO messages (user_id, sender_id, text, time)
    VALUES (?, ?, ?, ?)
    """, (user_id, sender_id, text, datetime.now().isoformat()))
    conn.commit()
