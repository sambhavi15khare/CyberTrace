import os

from modules.database import create_table
from modules.file_monitor import start_monitoring

create_table()

folder_to_watch = input("Enter the folder path to monitor: ").strip()

while not os.path.exists(folder_to_watch):
    print("\n❌ Folder does not exist!")
    folder_to_watch = input("Enter a valid folder path: ").strip()

start_monitoring(folder_to_watch)