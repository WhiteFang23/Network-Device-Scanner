## 🛰️ Network Device Scanner

A web-based network scanning tool built using Python, Flask, and Nmap that allows authenticated users to scan networks, identify live hosts, detect open ports, and discover running services through an interactive dashboard.

The application automates Nmap scanning using a Flask backend and stores scan results in a database, enabling users to track and monitor network services efficiently.
---
## 📌 Project Overview

Network scanning is a crucial step in cybersecurity for identifying exposed services and potential attack surfaces within a network.

This project implements a Network Device Scanner that integrates Nmap with a web-based interface to automate network scanning tasks such as:

🔍 Host discovery

🚪 Port scanning

⚙️ Service detection

The system provides an authenticated dashboard where users can perform scans and view results in a structured format.
---
## ✨ Key Features
🔐 Authentication System

Secure user login and registration

Password hashing using Werkzeug

Session management using Flask-Login

🌐 Network Scanning

Host discovery using Nmap

SYN-based port scanning (-sS)

Service version detection (-sV)

🗂️ Scan Result Logging

Stores scan results in a SQLite database

Tracks target IP, open ports, and services

Maintains scan history

📊 Dashboard Interface

Displays scan results in a structured table

Allows users to perform scans from the web interface

Shows previously scanned results
---
## 🛠️ Tech Stack
⚙️ Backend

🐍 Python

🌐 Flask

🔎 Networking

🛰️ Nmap

🧰 Python-Nmap

🗄️ Database

🗃️ SQLite

🧱 SQLAlchemy ORM

🔐 Authentication

Flask-Login

Werkzeug password hashing

🎨 Frontend

HTML
---
## 🧠 Security Concepts Demonstrated

🔎 Network reconnaissance

🚪 Port scanning

⚙️ Service enumeration

🔐 Authentication & session management

🔑 Secure password storage

🚀 Future Improvements

🧠 OS detection using Nmap

📈 Scan analytics dashboard

📄 Export scan reports

⏱️ Real-time scan progress

🐳 Docker deployment
---
## 👨‍💻 Author

Prabhat Patel
🎓 B.Tech Computer Science
🛡️ Cybersecurity Enthusiast
---
## ⚠️ Disclaimer

This project is intended for educational and security research purposes only. Do not scan networks without proper authorization.
---
