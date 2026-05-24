import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "spendwise.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "database", "schema.sql")
SEED_PATH = os.path.join(BASE_DIR, "database", "seed_data.sql")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def initialize_database(seed=False):
    with open(SCHEMA_PATH, "r") as f:
        schema = f.read()
    conn = get_connection()
    conn.executescript(schema)
    if seed:
        with open(SEED_PATH, "r") as f:
            seed_data = f.read()
        conn.executescript(seed_data)
    conn.commit()
    conn.close()


def fetch_all(query, params=()):
    conn = get_connection()
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return rows


def fetch_one(query, params=()):
    conn = get_connection()
    row = conn.execute(query, params).fetchone()
    conn.close()
    return row


def execute(query, params=()):
    conn = get_connection()
    cursor = conn.execute(query, params)
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id
