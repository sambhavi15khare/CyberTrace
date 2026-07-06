import os
import sqlite3


def connect_db():

    db_path = os.path.abspath("database/cybertrace.db")

    print("DATABASE PATH:", db_path)

    connection = sqlite3.connect(db_path)

    return connection


def create_table():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            level TEXT,

            event_type TEXT,

            file_path TEXT,

            file_hash TEXT,
            
            risk_score INTEGER,
            severity TEXT
        )
    """)

    connection.commit()

    connection.close()


def insert_log (
    timestamp,
    level,
    event_type,
    file_path,
    file_hash=None,
    risk_score=None,
    severity=None
):

    print("INSERTING:", event_type)

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO logs (
            timestamp,
            level,
            event_type,
            file_path,
            file_hash,
            risk_score,
            severity
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        timestamp,
        level,
        event_type,
        file_path,
        file_hash,
        risk_score,
        severity
    ))
    

    connection.commit()

    connection.close()

def get_file_timeline(file_path):

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            timestamp,
            event_type,
            level,
            file_hash
        FROM logs
        WHERE file_path = ?
        ORDER BY timestamp ASC
    """, (file_path,))

    records = cursor.fetchall()

    connection.close()

    return records
def get_all_files():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT DISTINCT file_path
        FROM logs
        ORDER BY file_path
    """)

    files = cursor.fetchall()

    connection.close()

    return files