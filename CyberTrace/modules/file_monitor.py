from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

from modules.logger import write_log
from modules.alerts import send_alert

from modules.risk_engine import calculate_risk

SUSPICIOUS_EXTENSIONS = [
    ".exe",
    ".bat",
    ".vbs",
    ".ps1",
    ".dll"
]


class MonitorHandler(FileSystemEventHandler):
    def process_event(self, level, event_type, file_path):

        score, severity, reasons = calculate_risk(
            event_type,
            file_path
        )

        write_log(
            level,
            event_type,
            file_path,
            score,
            severity,
            reasons
        )

        print("\n========== CyberTrace Risk Analysis ==========")
        print(f"Risk Score : {score}")
        print(f"Severity   : {severity}")

        print("\nReasons:")

        for reason in reasons:
            print(f"• {reason}")

        print("=============================================\n")

        print("-" * 35)
    def __init__(self):
        super().__init__()
        self.last_modified={}

    def on_created(self, event):
        print(f"File Created: {event.src_path}")

        if event.is_directory:
            return

        self.process_event(
            "INFO",
            "File Created",
            event.src_path
        )

        send_alert(
            "CyberTrace Alert",
            f"File Created: {event.src_path}"
        )

        file_path = event.src_path

        for extension in SUSPICIOUS_EXTENSIONS:

            if file_path.endswith(extension):

                write_log(
                    "CRITICAL",
                    "Suspicious File Detected",
                    file_path
                )

                send_alert(
                    "CyberTrace Critical Alert",
                    f"Suspicious File Detected:\n{file_path}"
                )

                break

    def on_deleted(self, event):
        print(f"File Deleted: {event.src_path}")

        if event.is_directory:
            return

        self.process_event(
            "WARNING",
            "File Deleted",
            event.src_path
        )

        send_alert(
            "CyberTrace Warning",
            f"File Deleted: {event.src_path}"
        )

    def on_modified(self, event):
        print(f"File Modified: {event.src_path}")

        if event.is_directory:
            return

        current_time = time.time()

        if event.src_path in self.last_modified:

            if current_time - self.last_modified[event.src_path] < 2:
                return

        self.last_modified[event.src_path] = current_time
        self.process_event(
                "INFO",
                "File Modified",
                event.src_path
            )

       # send_alert(
        #        "CyberTrace Alert",
         #       f"File Modified: {event.src_path}"
         #   )

    def on_moved(self, event):

        if event.is_directory:
            return

        self.process_event(
            "INFO",
            "File Renamed/Moved",
            event.dest_path)

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