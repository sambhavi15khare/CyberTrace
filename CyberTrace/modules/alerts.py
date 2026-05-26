from plyer import notification

def send_alert(title, message):

    notification.notify(
        title=title,
        message=message,
        timeout=5
    )