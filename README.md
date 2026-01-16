# LedgerMage – Personal Account Management System

A complete **desktop application** for managing personal accounts with a modern UI, secure login, real-time balance tracking, money transfers, bill checking utility, transaction history, and professional PDF report generation.

Built as a Semester Project for **Software Engineering** course.

https://github.com/YOUR_USERNAME/LedgerMage

## ✨ Features

- User Registration & Secure Login system
- Modern, clean GUI using **CustomTkinter**
- MySQL database with proper relational design (foreign keys, cascades)
- Dashboard showing real-time account balance
- Account-to-Account money transfer with balance validation
- Transaction history logging & beautiful table view
- Bill checking utility (Electricity, Gas, PTCL) with direct website links
- Professional PDF generation:
  - Account Details summary
  - Full Transaction History report
- Input validation, exception handling & user-friendly messages

## 🛠️ Tech Stack

- **Language**: Python 3
- **GUI**: CustomTkinter + tkinter + tkcalendar
- **Database**: MySQL (mysql-connector-python)
- **PDF Generation**: FPDF
- **Other Libraries**: Pillow (PIL), datetime, random, re, os, webbrowser

## 📸 Screenshots

(Add your screenshots here later – recommended: Login, Register, Dashboard, Send Money, Transaction History, PDF example)

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MySQL Server (running on localhost)
- Required Python packages:
  ```bash
  pip install customtkinter mysql-connector-python fpdf pillow tkcalendar
