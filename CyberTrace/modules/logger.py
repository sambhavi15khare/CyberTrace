from datetime import datetime
def write_log(event_type,file_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message =f"[{timestamp}]{event_type}->{file_path}\n"
    with open("logs/activity_log.txt","a") as log_file:
        log_file.write(log_message)
    print(log_message)