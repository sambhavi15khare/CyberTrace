# 🛡️ CyberTrace

**CyberTrace** is a Python-based Digital Forensics and File Integrity Monitoring (FIM) system that continuously monitors filesystem activities, generates SHA-256 integrity hashes, calculates risk scores for suspicious events, stores forensic evidence in a SQLite database, and provides real-time desktop notifications.

The project was built to demonstrate practical cybersecurity concepts including file monitoring, digital forensics, integrity verification, event logging, and threat classification.

---

# 📌 Features

### 📁 Real-Time File Monitoring
CyberTrace continuously monitors a selected directory and detects:

- File Creation
- File Modification
- File Deletion
- File Rename / Move

---

### 🔐 SHA-256 File Integrity Hashing

Whenever a file is created or modified, CyberTrace generates a SHA-256 hash to verify file integrity and help identify unauthorized changes.

---

### ⚠️ Risk Assessment Engine

Every detected event is analyzed using a rule-based Risk Engine.

Risk is calculated based on:

- Event Type
- Suspicious File Extensions
- Protected Folder Detection
- Hidden File Detection
- SHA-256 Hash Generation

Each event is assigned:

- Risk Score
- Severity Level
    - LOW
    - MEDIUM
    - HIGH
    - CRITICAL

---

### 🗄️ SQLite Forensic Database

CyberTrace stores every event in a SQLite database containing:

- Timestamp
- Event Type
- File Path
- SHA-256 Hash
- Risk Score
- Severity
- Log Level

---

### 📝 Activity Logs

Every event is also recorded inside:

```
logs/activity_log.txt
```

for quick forensic analysis.

---

### 🔔 Desktop Notifications

CyberTrace generates Windows desktop notifications for important filesystem events including:

- File Creation
- File Deletion
- File Rename
- Suspicious File Detection

---

### 📊 Timeline Reconstruction

Investigators can reconstruct the sequence of events for a file using the Timeline module.

---

### 🔍 Log Viewer

Stored forensic logs can be viewed directly from the SQLite database using:

```
python view_logs.py
```

---

# 🏗️ Project Architecture

```
                User

                  │

                  ▼

        File System Events

                  │

                  ▼

          file_monitor.py

                  │

        ┌─────────┼─────────┐

        ▼         ▼         ▼

 Risk Engine   Logger     Alerts

        │         │

        ▼         ▼

      SQLite Database

              │

              ▼

      Timeline & Log Viewer
```

---

# 📂 Project Structure

```
CyberTrace/

│

├── database/
│     └── cybertrace.db
│
├── logs/
│     └── activity_log.txt
│
├── modules/
│     ├── alerts.py
│     ├── database.py
│     ├── file_monitor.py
│     ├── hash_utils.py
│     ├── logger.py
│     └── risk_engine.py
│
├── main.py
├── timeline.py
├── view_logs.py
├── README.md
└── requirements.txt
```

---

# 🛠 Technologies Used

- Python 3
- Watchdog
- SQLite3
- Plyer
- Hashlib
- OS Module

---

# ▶️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd CyberTrace
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🚀 Running CyberTrace

Start monitoring:

```bash
python main.py
```

Enter the folder path to monitor when prompted.

Example:

```
D:\CyberTraceTest
```

---

View stored logs:

```bash
python view_logs.py
```

View file timeline:

```bash
python timeline.py
```

---

# 📈 Sample Output

```
============================================================

CyberTrace Security Event

============================================================

Timestamp   : 2026-07-06 18:42:13

Event       : File Created

Path        : D:\CyberTraceTest\notes.txt

SHA-256     : e3b0c44298fc...

Risk Score  : 25

Severity    : LOW

============================================================
```

---

# ⚠️ Known Limitations

- Cloud-synchronized folders (OneDrive, Dropbox, Google Drive) may emit filesystem events differently due to background synchronization.
- CyberTrace is optimized for monitoring local NTFS directories.
- Administrative privileges may be required for monitoring certain protected system folders.

---

# 🚀 Future Enhancements

- PDF Incident Report Generation
- Advanced Search & Filtering
- Hash Baseline Comparison
- Multi-directory Monitoring
- Linux Support
- Email Notifications
- Web Dashboard

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- File Integrity Monitoring (FIM)
- Digital Forensics
- Event Logging
- SHA-256 Integrity Verification
- SQLite Database Integration
- Real-Time Filesystem Monitoring
- Rule-Based Threat Classification
- Modular Python Application Development

---

# 👩‍💻 Author

**Sambhavi Khare**

B.Tech – Computer Science Engineering (IoT, Cyber Security & Blockchain)

LNCT, Bhopal
