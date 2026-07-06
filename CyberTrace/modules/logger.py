from datetime import datetime

from modules.database import insert_log
from modules.hash_utils import calculate_hash


def write_log(level, event_type, file_path, risk_score=None, severity=None, reasons=None):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_hash = None

    if (
        "Created" in event_type
        or "Modified" in event_type
    ):
        file_hash = calculate_hash(file_path)

    log_message = (
        f"\n{'=' * 60}\n"
        f"Timestamp   : {timestamp}\n"
        f"Event       : {event_type}\n"
        f"Level       : {level}\n"
        f"Path        : {file_path}\n"
        f"SHA-256     : {file_hash}\n"
        f"Risk Score  : {risk_score}\n"
        f"Severity    : {severity}\n"
        f"{'=' * 60}\n"
    )

    with open(
        "logs/activity_log.txt",
        "a",
        encoding="utf-8"
    ) as log_file:

        log_file.write(log_message)

    print(log_message)

    insert_log(
        timestamp,
        level,
        event_type,
        file_path,
        file_hash,
        risk_score,
        severity
    )