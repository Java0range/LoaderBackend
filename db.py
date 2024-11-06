import sqlite3
import random


def create_key():
    lst = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    s = ""
    for i, item in enumerate(random.choices(lst, k=10)):
        if i == 4 or i == 8:
            s += "-"
        s += item
    return s


def create_keys(count):
    conn = sqlite3.connect("keys.db")
    c = conn.cursor()
    keys = []
    for i in range(count):
        key = create_key()
        while True:
            if check_key(key):
                key = create_key()
            else:
                break
        keys.append(key)
        c.execute(f"INSERT INTO keys(key) VALUES('{key}')")
    conn.commit()
    conn.close()
    return keys


def check_key(key):
    conn = sqlite3.connect("keys.db")
    c = conn.cursor()
    lst = c.execute(f"SELECT key FROM keys WHERE key = '{key}'").fetchall()
    conn.close()
    if lst:
        return True
    else:
        return False


def clear_db():
    conn = sqlite3.connect("keys.db")
    c = conn.cursor()
    c.execute("DELETE from keys")
    conn.commit()
    conn.close()