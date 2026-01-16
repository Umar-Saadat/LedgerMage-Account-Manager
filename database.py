import mysql.connector
from tkinter import messagebox
def database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your password"
        )
        cursor = conn.cursor()
    
        query = "create database if not exists LedgerMage"
        cursor.execute(query)
        
    except Exception as e:
        messagebox.showerror('Error',str(e))
        