from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

from modules.logger import write_log
from modules.alerts import send_alert


class MonitorHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        write_log(
            "INFO - File Created",
            event.src_path
        )

        send_alert(
            "CyberTrace Alert",
            f"File Created: {event.src_path}"
        )

        # Detect executable files
        if event.src_path.endswith(".exe"):

            write_log(
                "CRITICAL - Executable File Detected",
                event.src_path
            )

            send_alert(
                "CyberTrace Critical Alert",
                f"Executable File Detected:\n{event.src_path}"
            )

    def on_deleted(self, event):

        if event.is_directory:
            return

        write_log(
            "WARNING - File Deleted",
            event.src_path
        )

        send_alert(
            "CyberTrace Warning",
            f"File Deleted: {event.src_path}"
        )

    def on_modified(self, event):

        if event.is_directory:
            return

        write_log(
            "INFO - File Modified",
            event.src_path
        )

        send_alert(
            "CyberTrace Alert",
            f"File Modified: {event.src_path}"
        )

    def on_moved(self, event):

        if event.is_directory:
            return

        print("MOVE EVENT DETECTED")

        write_log(
            "INFO - File Renamed/Moved",
            f"{event.src_path} -> {event.dest_path}"
        )

        send_alert(
            "CyberTrace Warning",
            f"File Renamed/Moved:\n{event.src_path} -> {event.dest_path}"
        )


def start_monitoring(folder_path):

    path = folder_path

    event_handler = MonitorHandler()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)

    observer.start()

    print("CyberTrace Monitoring Started...")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()