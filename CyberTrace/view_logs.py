import sqlite3

connection = sqlite3.connect("database/cybertrace.db")
cursor = connection.cursor()

cursor.execute("""
SELECT
    id,
    timestamp,
    level,
    event_type,
    file_path,
    file_hash,
    risk_score,
    severity
FROM logs
""")

logs = cursor.fetchall()

print("\n" + "=" * 75)
print("                     CyberTrace Log Viewer")
print("=" * 75)

for log in logs:

    print(f"ID         : {log[0]}")
    print(f"Timestamp  : {log[1]}")
    print(f"Level      : {log[2]}")
    print(f"Event      : {log[3]}")
    print(f"Path       : {log[4]}")
    print(f"SHA-256    : {log[5]}")
    print(f"Risk Score : {log[6]}")
    print(f"Severity   : {log[7]}")

    print("-" * 75)

connection.close()