import os

# ============================================
# CyberTrace Risk Engine
# ============================================

SUSPICIOUS_EXTENSIONS = [
    ".exe",
    ".dll",
    ".bat",
    ".cmd",
    ".scr",
    ".pif",
    ".com",
    ".vbs",
    ".js",
    ".jar",
    ".ps1"
]

PROTECTED_FOLDERS = [
    "Documents",
    "Desktop",
    "Downloads",
    "Pictures",
    "Videos"
]


def calculate_risk(event_type, file_path, file_hash=None):

    score = 0
    reasons = []

    extension = os.path.splitext(file_path)[1].lower()
    filename = os.path.basename(file_path)

    # ============================================
    # Event Type
    # ============================================

    event = event_type.lower()

    if event == "file created":
        score += 5
        reasons.append("New File Created")

    elif event == "file modified":
        score += 3
        reasons.append("File Modified")

    elif event == "file deleted":
        score += 15
        reasons.append("File Deleted")

    elif event == "file renamed/moved":
        score += 10
        reasons.append("File Renamed or Moved")

    # ============================================
    # Suspicious Extension
    # ============================================

    if extension in SUSPICIOUS_EXTENSIONS:
        score += 40
        reasons.append(f"Suspicious File Extension ({extension})")

    # ============================================
    # Protected Folder
    # ============================================

    for folder in PROTECTED_FOLDERS:

        if folder.lower() in file_path.lower():

            score += 20
            reasons.append(f"Protected Folder ({folder})")
            break

    # ============================================
    # Hidden File
    # ============================================

    if filename.startswith("."):

        score += 15
        reasons.append("Hidden File")

    # ============================================
    # SHA-256 Hash
    # ============================================

    if file_hash is not None:

        score += 10
        reasons.append("SHA-256 Integrity Hash Generated")

    # ============================================
    # Severity
    # ============================================

    if score >= 80:
        severity = "CRITICAL"

    elif score >= 60:
        severity = "HIGH"

    elif score >= 30:
        severity = "MEDIUM"

    else:
        severity = "LOW"

    # ============================================

    return score, severity, reasons