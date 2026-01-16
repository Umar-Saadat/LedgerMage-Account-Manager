import customtkinter as ctk
# import pyfingerprint
import random
import re
from tkinter import messagebox as msg
from datetime import datetime
import mysql.connector
from tkcalendar import Calendar, DateEntry
import tkinter as tk

class Register(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title('Registration Page')
        self.geometry('1000x670+0+0')
        self.resizable(False,False)
        
        self.configure(fg_color='#e1e5eb')
        
        self.RegisterDetail()
        
    def RegisterDetail(self):
        
        self.register_label = ctk.CTkLabel(self,text='Register an Account',text_color='#000000',font=('Arial Rounded MT Bold',34))
        self.register_label.place(x=320,y=40)
        
        self.Email = ctk.CTkEntry(self,placeholder_text='Email',corner_radius=0,bg_color='#e1e5eb',fg_color='#f7f9fb',placeholder_text_color='#a0a0a0',font=('Poopins',18),width=400,height=45)
        self.Email.place(x=290,y=100)
        
        self.password = ctk.CTkEntry(self,placeholder_text='Password',show='*',corner_radius=0,bg_color='#e1e5eb',fg_color='#f7f9fb',placeholder_text_color='#a0a0a0',font=('Poopins',18),width=400,height=45)
        self.password.place(x=290,y=170)
        
        self.Cnic_Number = ctk.CTkEntry(self,placeholder_text='CNIC (12345-09876543-2)',corner_radius=0,bg_color='#e1e5eb',fg_color='#f7f9fb',placeholder_text_color='#a0a0a0',font=('Poopins',18),width=400,height=45)
        self.Cnic_Number.place(x=290,y=240)
        
        self.First_Name = ctk.CTkEntry(self,placeholder_text='First Name',corner_radius=0,bg_color='#e1e5eb',fg_color='#f7f9fb',placeholder_text_color='#a0a0a0',font=('Poopins',18),width=400,height=45)
        self.First_Name.place(x=290,y=310)
        
        self.Last_Name = ctk.CTkEntry(self,placeholder_text='Last Name',corner_radius=0,bg_color='#e1e5eb',fg_color='#f7f9fb',placeholder_text_color='#a0a0a0',font=('Poopins',18),width=400,height=45)
        self.Last_Name.place(x=290,y=380)
        
        # Replace DOB entry with a DateEntry
        self.dob1 = DateEntry(self, date_pattern='yyyy-mm-dd', font=('Poopins',18), width=18)
        self.dob1.place(x=290,y=450)
        
        self.ph_no = ctk.CTkEntry(self,placeholder_text='Ph.No (0000-0000000)',corner_radius=0,bg_color='#e1e5eb',fg_color='#f7f9fb',placeholder_text_color='#a0a0a0',font=('Poopins',18),width=400,height=45)
        self.ph_no.place(x=290,y=520)
        
        acc_no = f"PK{random.randint(10000000, 99999999)}"

        def Check_Entries():
            email_pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'  # Regex for gmail only
    
            if self.Email.get() != "" and self.password.get() != ""  and self.Cnic_Number.get() != "" and self.First_Name.get() != "" and self.Last_Name.get() != "" and self.dob1.get() != "":
        
                if not re.match(email_pattern, self.Email.get()):
                    msg.showerror('Error', 'Email must be a valid Gmail address (example@gmail.com)')
                    return
        
                Database_Conncetion()
            else:
                msg.showerror('Error','All Fields must filled')

        
        self.Register_btn = ctk.CTkButton(self,text='Register',fg_color='blue',hover_color='orange',text_color='#ffffff',font=('Poopins',17,"bold"),width=400,height=45,command=Check_Entries)
        self.Register_btn.place(x=290,y=600)
        
        def Database_Conncetion():
            try:
                try:
                    datetime.strptime(self.dob1.get(), "%Y-%m-%d")
                    Dob_entry = self.dob1.get()
                except Exception as e:
                    msg.showerror('Error',f"Error occur {e}")
                conn = mysql.connector.connect(
                    host = 'localhost',
                    database="LedgerMage",
                    password = 'your password',
                    user='root'
                )
                
                cursor = conn.cursor()
                Registration_Table = """CREATE TABLE IF NOT EXISTS Registration (
                Account_Number VARCHAR(20) PRIMARY KEY,
                Cnic VARCHAR(20) NOT NULL UNIQUE,
                Dob DATE NOT NULL,
                Ph_No VARCHAR(12) NOT NULL,
                Email VARCHAR(50) NOT NULL UNIQUE,
                password_user VARCHAR(64) NOT NULL,
                First_Name VARCHAR(20) NOT NULL,
                Last_Name VARCHAR(20) NOT NULL,
                Creation_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""

                Login_Table = """CREATE TABLE IF NOT EXISTS Login (
                Account_Number VARCHAR(20) PRIMARY KEY,
                Username VARCHAR(50) NOT NULL UNIQUE,
                password_user VARCHAR(64) NOT NULL,
                FOREIGN KEY (Account_Number) REFERENCES Registration(Account_Number) ON DELETE CASCADE);"""

                Balance_Table = """CREATE TABLE IF NOT EXISTS Balance (
                Account_Number VARCHAR(20) PRIMARY KEY,
                balance DECIMAL(12,2) DEFAULT 50000.00,
                FOREIGN KEY (Account_Number) REFERENCES Registration(Account_Number) ON DELETE CASCADE)"""

                Account_Details_Table = """CREATE TABLE IF NOT EXISTS Account_Details (
                Account_Number VARCHAR(20) PRIMARY KEY,
                Cnic VARCHAR(20),
                Email VARCHAR(50),
                First_Name VARCHAR(20),
                Last_Name VARCHAR(20),
                Dob DATE,
                Ph_No VARCHAR(12),
                FOREIGN KEY (Account_Number) REFERENCES Registration(Account_Number) ON DELETE CASCADE);"""
                
                Transction_History = """CREATE TABLE IF NOT EXISTS Transaction_History (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Account_Number VARCHAR(20) NOT NULL,
                Transfer_Type VARCHAR(30) NOT NULL,
                Amount DECIMAL(12,2) NOT NULL,
                Receiver_or_Biller VARCHAR(100),
                Transaction_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (Account_Number) REFERENCES Registration(Account_Number) ON DELETE CASCADE);""" 

                
                cursor.execute(Registration_Table)
                cursor.execute(Login_Table)
                cursor.execute(Balance_Table)
                cursor.execute(Account_Details_Table)
                cursor.execute(Transction_History)
                print('Db Connection Success')
                query = "insert into Registration(Account_Number,Cnic,Dob,Ph_No,Email,password_user,First_Name,Last_Name) Values(%s,%s,%s,%s,%s,%s,%s,%s)"
                query2 = "insert into Login(Username,password_user,Account_Number) Values(%s,%s,%s)"
                query3 = "insert into Balance(Account_Number) Values(%s)"
                query4 = "insert into Account_Details(Account_Number,Cnic,Email,First_Name,Last_Name,Dob,Ph_No) Values(%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(query,(acc_no,self.Cnic_Number.get(), Dob_entry,self.ph_no.get(),self.Email.get(),self.password.get(), self.First_Name.get(), self.Last_Name.get()))
                cursor.execute(query2,(self.Email.get(),self.password.get(),acc_no))
                cursor.execute(query3,(acc_no,))
                cursor.execute(query4,(acc_no,self.Cnic_Number.get(),self.Email.get(),self.First_Name.get(),self.Last_Name.get(),Dob_entry,self.ph_no.get()))
                conn.commit()
                msg.showinfo('Success','Registered Successfully')
                msg.showinfo(f'Account',f'Your Account Number is {acc_no}')
                self.Email.delete(0,ctk.END)
                self.password.delete(0,ctk.END)
                self.dob1.set_date('')  # Clear the calendar entry
                self.Cnic_Number.delete(0,ctk.END)
                self.First_Name.delete(0,ctk.END)
                self.Last_Name.delete(0,ctk.END)
                self.ph_no.delete(0,ctk.END)
                cursor.close()
            except mysql.connector.Error as e:
                msg.showerror('Error',f'Error in connecting database {e}')
            finally:
                if conn and conn.is_connected():
                    conn.close()
                    
if __name__ == "__main__":
    App = Register()
    App.mainloop()
