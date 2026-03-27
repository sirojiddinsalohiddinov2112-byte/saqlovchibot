import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect("db.sqlite3", check_same_thread=False)
cur = conn.cursor()

# ================= TABLE =================
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    telegram_id INTEGER PRIMARY KEY,
    phone TEXT,
    trial_end TEXT,
    premium_end TEXT
)
""")

conn.commit()

# ================= ADD USER =================
def add_user(user_id):
    trial = datetime.now() + timedelta(days=2)

    cur.execute("""
    INSERT OR IGNORE INTO users (telegram_id, phone, trial_end, premium_end)
    VALUES (?, ?, ?, ?)
    """, (user_id, None, trial.isoformat(), None))

    conn.commit()

# ================= GET USER =================
def get_user(user_id):
    cur.execute("SELECT * FROM users WHERE telegram_id=?", (user_id,))
    return cur.fetchone()

# ================= SET PREMIUM =================
def set_premium(user_id):
    premium = datetime.now() + timedelta(days=30)

    cur.execute("""
    UPDATE users SET premium_end=? WHERE telegram_id=?
    """, (premium.isoformat(), user_id))

    conn.commit()

# ================= CHECK PREMIUM =================
def is_premium(user_id):
    user = get_user(user_id)
    if not user:
        return False

    premium_end = user[3]
    if premium_end is None:
        return False

    return datetime.fromisoformat(premium_end) > datetime.now()
