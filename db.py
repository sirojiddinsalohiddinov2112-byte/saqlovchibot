import sqlite3

conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    telegram_id INTEGER PRIMARY KEY,
    phone TEXT,
    trial_end TEXT,
    premium_end TEXT
)
""")

conn.commit()

def add_user(user_id):
    from datetime import datetime, timedelta
    trial = datetime.now() + timedelta(days=2)

    cur.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?)",
                (user_id, None, str(trial), None))
    conn.commit()

def get_user(user_id):
    cur.execute("SELECT * FROM users WHERE telegram_id=?", (user_id,))
    return cur.fetchone()

def set_premium(user_id):
    from datetime import datetime, timedelta
    premium = datetime.now() + timedelta(days=30)

    cur.execute("UPDATE users SET premium_end=? WHERE telegram_id=?",
                (str(premium), user_id))
    conn.commit()
