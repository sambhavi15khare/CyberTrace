from modules.database import get_file_timeline


file_path = input("Enter file path: ")

records = get_file_timeline(file_path)

print("\n=== CyberTrace Timeline ===\n")

for record in records:

    timestamp, event_type, level, file_hash = record

    print(
        f"[{timestamp}] "
        f"[{level}] "
        f"{event_type}"
    )

print("\n==========================")
from modules.database import (
    get_file_timeline,
    get_all_files
)

print("\nFiles Found:\n")

files = get_all_files()

for index, file in enumerate(files, start=1):

    print(f"{index}. {file[0]}")
