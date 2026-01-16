import customtkinter as ctk

from fpdf import FPDF
import os

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

from tkinter import ttk

import database as db

from tkinter import messagebox as msg

import webbrowser

import ast

from datetime import datetime

import mysql.connector

import tkinter as tk

from PIL import Image,ImageTk


class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title('Dashboard')
        self.geometry('1366x768')
        self.resizable(False,False)
        
        self.configure(fg_color='#f5f6fa')
        db.database()
        self.Dashboard_Details()
        
                
    def Dashboard_Details(self):
        
        try:
            conn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                database = 'LedgerMage',
                password = 'your password'
            )
            with open('Name.txt','r') as f:
                key = f.read()
                data = ast.literal_eval(key)
            cursor = conn.cursor()
            query = "select First_Name from Account_Details where Account_Number=%s"
            query1 = "select Account_Number from Account_Details where Account_Number=%s"
            query3 = "select Last_Name from Account_Details where Account_Number=%s"
            query4 = "select Email from Account_Details where Account_Number=%s"
            query5 = "select Ph_No from Account_Details where Account_Number=%s"
            query6 = "select Cnic from Account_Details where Account_Number=%s"
            query7 = "select Dob from Account_Details where Account_Number=%s"
            query8 = "select balance from Balance where Account_Number=%s"
            cursor.execute(query,(data))
            result = cursor.fetchone()
            cursor.execute(query1,(data))
            Acc_no_fetch = cursor.fetchone()
            cursor.execute(query3,(data))
            L_Name = cursor.fetchone()
            cursor.execute(query4,(data))
            Email_id = cursor.fetchone()
            cursor.execute(query5,(data))
            Phone_num = cursor.fetchone()
            cursor.execute(query6,(data))
            Cnic_num = cursor.fetchone()
            cursor.execute(query7,(data))
            Account_opening = cursor.fetchone()
            cursor.execute(query8,(data))
            Balance = cursor.fetchone()
            
        except Exception as e:
            msg.showerror('Error',str(e))
            conn.commit()
            conn.close()
            
        for widget in self.winfo_children():
            widget.destroy()
            
        
        self.Frame = ctk.CTkFrame(self,bg_color='#f7faff',corner_radius=0,width=1250,height=650,fg_color='#ffffff',background_corner_colors=['red','blue','black','white'])
        self.Frame.place(x=60,y=40)
        
        self.Frame2 = ctk.CTkFrame(self.Frame,fg_color='#3b82f6',corner_radius=0,height=650,width=300,bg_color='#f7faff')
        self.Frame2.place(x=0,y=0) 
        Main_Label = ctk.CTkLabel(self.Frame2,text='LedgerMate',font=('Poopins',26,"bold"),text_color='#ffffff',fg_color='#3b82f6')
        icon = ctk.CTkImage(light_image=Image.open('ICONS/home.png'),dark_image=Image.open('ICONS/home.png'),size=(30,30))
        Icon_Label = ctk.CTkLabel(self.Frame2,text="",image=icon,compound='left')
        Icon_Label.place(x=40,y=20)
        Main_Label.place(x=90,y=20)
        Dashboard_Label = ctk.CTkButton(self.Frame2,text='Dashboard',hover='#000000',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"))
        icon1 = ctk.CTkImage(light_image=Image.open('ICONS/home.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
        Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
        Icon.place(x=65,y=140)
        Dashboard_Label.place(x=80,y=140)
        #####################1###########################
        
        def Account_details():
            
            for widget in self.winfo_children():
                widget.destroy()

            self.Frame = ctk.CTkFrame(self,bg_color='#f7faff',corner_radius=0,width=1250,height=650,fg_color='#ffffff',background_corner_colors=['red','blue','black','white'])
            self.Frame.place(x=60,y=40)
        
            self.Frame2 = ctk.CTkFrame(self.Frame,fg_color='#3b82f6',corner_radius=0,height=650,width=300,bg_color='#f7faff')
            self.Frame2.place(x=0,y=0) 
        
            Main_Label = ctk.CTkLabel(self.Frame2,text='LedgerMate',font=('Poopins',26,"bold"),text_color='#ffffff',fg_color='#3b82f6')
            icon = ctk.CTkImage(light_image=Image.open('ICONS/home.png'),dark_image=Image.open('ICONS/home.png'),size=(30,30))
            Icon_Label = ctk.CTkLabel(self.Frame2,text="",image=icon,compound='left')
            Icon_Label.place(x=40,y=20)
            Main_Label.place(x=90,y=20)
        
            Dashboard_Label = ctk.CTkButton(self.Frame2,text='Dashboard',hover='#000000',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=self.Dashboard_Details)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/home.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=65,y=140)
            Dashboard_Label.place(x=80,y=140)
        
            Account_Details_Label = ctk.CTkButton(self.Frame2,text='Account Details',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Account_details)
            Account_Details_Label.place(x=100,y=230)
            icon = ctk.CTkImage(light_image=Image.open('ICONS/account1.png'),dark_image=Image.open('ICONS/home.png'),size=(30,30))
            Icon_Label = ctk.CTkLabel(self.Frame2,text="",image=icon,compound='left')
            Icon_Label.place(x=70,y=230)
        
            Send_Money_Label = ctk.CTkButton(self.Frame2,text='Send Money',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Send_Money)
            Send_Money_Label.place(x=85,y=320)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/send_imresizer.png'),dark_image=Image.open('ICONS/send_imresizer.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=320)
        
            Bill_Payment_Label = ctk.CTkButton(self.Frame2,text='Check Bill',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Bill_Payment)
            Bill_Payment_Label.place(x=85,y=410)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/bill_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=410)
            
            Transction_Details_Label = ctk.CTkButton(self.Frame2,text='Transction History',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Transction_History)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/history1.png'),dark_image=Image.open('ICONS/history1.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=500)
            Transction_Details_Label.place(x=100,y=500)
        
            Logout_Label = ctk.CTkButton(self.Frame2,text='Logout',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Logout)
            Logout_Label.place(x=65,y=590)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/power_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=590)
        
        
        #Main Page
        
            self.Dashobard = ctk.CTkLabel(self.Frame,text='Account Details',font=('Poopins',26,'bold'),fg_color='#ffffff',bg_color='#ffffff',text_color='#000000')
            self.Dashobard.place(x=330,y=30)
        
            self.user_greeting_label = ctk.CTkLabel(self.Frame,text=f'Hi,{result[0]}',text_color='#6b7280',font=('Poopins',17),fg_color='#ffffff',bg_color='#ffffff')
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/user1.png'),dark_image=Image.open('ICONS/user1.png'),size=(35,35))
            Icon = ctk.CTkLabel(self.Frame,text="",image=icon1)
            Icon.place(x=1190,y=25)
            self.user_greeting_label.place(x=1090,y=30)
        
            Frame_Details = ctk.CTkFrame(master=self.Frame,width=890,height=520,fg_color='#ffffff',bg_color='#ffffff',border_width=2,border_color='#ffffff',corner_radius=0)
            Frame_Details.place(x=330,y=100)
            
            Account_Holder = ctk.CTkLabel(master=Frame_Details,text='Account Holder',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Account_Holder.place(x=100,y=25)
            
            Account_Holder_Name = ctk.CTkLabel(master=Frame_Details,text=f"{result[0]} {L_Name[0]}",font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Account_Holder_Name.place(x=450,y=25)
            
            Account_Holder_Number = ctk.CTkLabel(master=Frame_Details,text='Account Number',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Account_Holder_Number.place(x=100,y=80)
            
            Account_Holder_Number_Digits = ctk.CTkLabel(master=Frame_Details,text=Acc_no_fetch,font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Account_Holder_Number_Digits.place(x=450,y=80)
            
            Account_Type = ctk.CTkLabel(master=Frame_Details,text='Account Type',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Account_Type.place(x=100,y=135)
            
            Account_Type_Name = ctk.CTkLabel(master=Frame_Details,text='Savings',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Account_Type_Name.place(x=450,y=135)
            
            Email = ctk.CTkLabel(master=Frame_Details,text='Email',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Email.place(x=100,y=190)
            
            Email_Name = ctk.CTkLabel(master=Frame_Details,text=f'{Email_id[0]}',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Email_Name.place(x=450,y=190)
            
            Phone = ctk.CTkLabel(master=Frame_Details,text='Phone',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Phone.place(x=100,y=245)
            
            Phone_Number = ctk.CTkLabel(master=Frame_Details,text=f'{Phone_num[0]}',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Phone_Number.place(x=450,y=245)
            
            Cnic = ctk.CTkLabel(master=Frame_Details,text='CNIC',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Cnic.place(x=100,y=300)
            
            Cnic_Number = ctk.CTkLabel(master=Frame_Details,text=f'{Cnic_num[0]}',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Cnic_Number.place(x=450,y=300)
            
            Branch = ctk.CTkLabel(master=Frame_Details,text='Branch',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Branch.place(x=100,y=355)
            
            Branch_Name = ctk.CTkLabel(master=Frame_Details,text='Islamabad',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Branch_Name.place(x=450,y=355)
            
            Opening = ctk.CTkLabel(master=Frame_Details,text='Opening Date',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Opening.place(x=100,y=410)
            
            Opening_Date = ctk.CTkLabel(master=Frame_Details,text=f'{Account_opening[0]}',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Opening_Date.place(x=450,y=410)
            
            Status = ctk.CTkLabel(master=Frame_Details,text='Status',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Status.place(x=100,y=465)
            
            Account_Status = ctk.CTkLabel(master=Frame_Details,text='✔ Active',font=('Poopins',18,'bold'),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Account_Status.place(x=450,y=465)
            
            Edit_Account_info_btn = ctk.CTkButton(master=Frame_Details,text='Edit Account Info',text_color='#ffffff',fg_color='#3b82f6',bg_color='#ffffff',hover_color='#2563eb',font=('Poopins',17),width=250,height=40,corner_radius=10)
            Edit_Account_info_btn.place(x=640,y=400)
            
                        # ====================== GENERATE ACCOUNT DETAILS PDF ======================
            def generate_account_pdf():
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", 'B', 20)
                pdf.set_text_color(59, 130, 246)
                pdf.cell(0, 15, "LedgerMate - Account Details", ln=1, align='C')
                pdf.ln(15)

                pdf.set_font("Arial", 'B', 14)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(0, 10, f"Account Holder: {result[0]} {L_Name[0]}", ln=1)
                pdf.cell(0, 10, f"Account Number: {Acc_no_fetch[0]}", ln=1)
                pdf.cell(0, 10, f"Account Type: Savings", ln=1)
                pdf.cell(0, 10, f"Email: {Email_id[0]}", ln=1)
                pdf.cell(0, 10, f"Phone: {Phone_num[0]}", ln=1)
                pdf.cell(0, 10, f"CNIC: {Cnic_num[0]}", ln=1)
                pdf.cell(0, 10, f"Branch: Islamabad", ln=1)
                pdf.cell(0, 10, f"Opening Date: {Account_opening[0]}", ln=1)
                pdf.cell(0, 10, f"Current Balance: Rs {Balance[0]:,.2f}", ln=1)
                pdf.cell(0, 10, f"Status: Active", ln=1)
                pdf.ln(10)

                pdf.set_font("Arial", size=12)
                pdf.set_text_color(100, 100, 100)
                pdf.cell(0, 10, f"Report Generated On: {datetime.now().strftime('%d %B %Y, %I:%M %p')}", ln=1)

                filename = f"Account_Details_{Acc_no_fetch[0]}_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
                filepath = os.path.join(os.path.expanduser("~"), "Downloads", filename)
                pdf.output(filepath)

                msg.showinfo("Success", f"Account Details PDF Generated!\nSaved in Downloads folder\n{filename}")
                os.startfile(filepath)  # Opens the PDF automatically (Windows)

            # Generate PDF Button for Account Details
            generate_account_btn = ctk.CTkButton(
                master=Frame_Details,
                text="Generate PDF",
                fg_color="#3b82f6",
                hover_color="#1d4ed8",
                text_color="white",
                font=('Poopins', 17),
                width=250,
                height=40,
                corner_radius=10,
                command=generate_account_pdf
            )
            generate_account_btn.place(x=640, y=450)
        
        #End of Account details page
        Account_Details_Label = ctk.CTkButton(self.Frame2,text='Account Details',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Account_details)
        icon1 = ctk.CTkImage(light_image=Image.open('ICONS/account1.png'),dark_image=Image.open('ICONS/account1.png'),size=(23,23))
        Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
        Icon.place(x=70,y=230)
        Account_Details_Label.place(x=100,y=230)
        ##********************1*****************************
        
        
        #######################2############################
        
        #Send Money Page
        
        def Send_Money():
            
            def send_Money_Logic():
                conn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                database = 'LedgerMage',
                password = '12345'
            )
                cursor = conn.cursor()
                acc_no = Account_Number_Entry.get()
                query_acc_no = "select Account_Number from Balance where Account_Number=%s"
                Account_holder_Name = "select First_Name from Account_Details where Account_Number=%s"
                cursor.execute(query_acc_no,(acc_no,))
                res = cursor.fetchone()
                cursor.execute(Account_holder_Name,(acc_no,))
                name = cursor.fetchone()
                if res:
                    if float(Amount_Label_Entry.get()) > Balance[0]:
                        msg.showerror('Error','Insuffisent Balance')
                    else:
                        bal = float(Amount_Label_Entry.get())
                        query_balance = "update Balance set balance=balance+%s where Account_Number=%s"
                        cursor.execute(query_balance,(bal,res[0]))
                        bal_update = "update Balance set balance=balance-%s where Account_Number=%s"
                        cursor.execute(bal_update,(bal,data[0]))
                        msg.showinfo('Sucess','Amount Send Sucessfully')
                        # Fisrt_Name = result[0]
                        # Email = Email_id[0]
                        print(type(Email_id[0]),type(Acc_no_fetch),type(result[0]),type(bal),type(name[0]))
                        trans_q = """INSERT INTO Transaction_History(Account_Number,Transfer_Type,Amount,Receiver_or_Biller) VALUES(%s,%s,%s,%s)"""
                        # Use existing variables safely without Acc_no_fetch
                        cursor.execute(trans_q, (data[0],"Online Transfer",float(Amount_Label_Entry.get()),res[0]))

                        Account_Number_Entry.delete(0,ctk.END)
                        Amount_Label_Entry.delete(0,ctk.END)
                        conn.commit()
                        conn.close()
                        
                else:
                    msg.showerror('Error','Account not found')
            
            for widget in self.winfo_children():
                widget.destroy()
            self.Frame = ctk.CTkFrame(self,bg_color='#f7faff',corner_radius=0,width=1250,height=650,fg_color='#ffffff',background_corner_colors=['red','blue','black','white'])
            self.Frame.place(x=60,y=40)
        
            self.Frame2 = ctk.CTkFrame(self.Frame,fg_color='#3b82f6',corner_radius=0,height=650,width=300,bg_color='#f7faff')
            self.Frame2.place(x=0,y=0) 
        
            Main_Label = ctk.CTkLabel(self.Frame2,text='LedgerMate',font=('Poopins',26,"bold"),text_color='#ffffff',fg_color='#3b82f6')
            Main_Label.place(x=90,y=20)
            icon = ctk.CTkImage(light_image=Image.open('ICONS/home.png'),dark_image=Image.open('ICONS/home.png'),size=(30,30))
            Icon_Label = ctk.CTkLabel(self.Frame2,text="",image=icon,compound='left')
            Icon_Label.place(x=40,y=20)
        
            Dashboard_Label = ctk.CTkButton(self.Frame2,text='Dashboard',hover='#000000',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=self.Dashboard_Details)
            Dashboard_Label.place(x=80,y=140)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/home.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=65,y=140)
        
            Account_Details_Label = ctk.CTkButton(self.Frame2,text='Account Details',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Account_details)
            Account_Details_Label.place(x=100,y=230)
            icon = ctk.CTkImage(light_image=Image.open('ICONS/account1.png'),dark_image=Image.open('ICONS/home.png'),size=(30,30))
            Icon_Label = ctk.CTkLabel(self.Frame2,text="",image=icon,compound='left')
            Icon_Label.place(x=70,y=230)
        
            Send_Money_Label = ctk.CTkButton(self.Frame2,text='Send Money',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Send_Money)
            Send_Money_Label.place(x=85,y=320)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/send_imresizer.png'),dark_image=Image.open('ICONS/send_imresizer.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=320)
        
            Bill_Payment_Label = ctk.CTkButton(self.Frame2,text='Check Bill',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Bill_Payment)
            Bill_Payment_Label.place(x=85,y=410)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/bill_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=410)
            
            Transction_Details_Label = ctk.CTkButton(self.Frame2,text='Transction History',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Transction_History)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/history1.png'),dark_image=Image.open('ICONS/history1.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=500)
            Transction_Details_Label.place(x=100,y=500)
        
            Logout_Label = ctk.CTkButton(self.Frame2,text='Logout',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Logout)
            Logout_Label.place(x=65,y=590)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/power_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=590)
        
        #Main Page
        
            self.Dashobard = ctk.CTkLabel(self.Frame,text='Send Money',font=('Poopins',36,'bold'),fg_color='#ffffff',bg_color='#ffffff',text_color='#000000')
            self.Dashobard.place(x=360,y=100)
        
            self.user_greeting_label = ctk.CTkLabel(self.Frame,text=f'Hi,{result[0]}',text_color='#6b7280',font=('Poopins',17),fg_color='#ffffff',bg_color='#ffffff')
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/user1.png'),dark_image=Image.open('ICONS/user1.png'),size=(35,35))
            Icon = ctk.CTkLabel(self.Frame,text="",image=icon1)
            Icon.place(x=1190,y=25)
            self.user_greeting_label.place(x=1090,y=30)
            Recipient_label = ctk.CTkLabel(master=self.Frame,text='Recipient',font=('Poopins',20),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Recipient_label.place(x=360,y=180)
            
            Frame1 = ctk.CTkFrame(master=self.Frame,width=600,height=410,bg_color='#ffffff',fg_color='#ffffff',border_color=None,corner_radius=None)
            Frame1.place(x=330,y=230)
            
            Account_Number = ctk.CTkLabel(master=Frame1,text='Account Number',font=('Poopins',20),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Account_Number.place(x=30,y=25)
            
            Account_Number_Entry = ctk.CTkEntry(master=Frame1,placeholder_text='PK00000000',text_color='#000000',fg_color='#ffffff',bg_color='#ffffff',corner_radius=5,font=('Arial',17),width=270,height=40)
            Account_Number_Entry.place(x=200,y=20)
            
            Amount_Label = ctk.CTkLabel(master=Frame1,text='Amount (Rs.)',font=('Poopins',20),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Amount_Label.place(x=30,y=100)
            
            Amount_Label_Entry =  ctk.CTkEntry(master=Frame1,placeholder_text='Rs 5,000.00',text_color='#000000',fg_color='#ffffff',bg_color='#ffffff',corner_radius=5,font=('Arial',17),width=270,height=40)
            Amount_Label_Entry.place(x=200,y=100)
            
            Source_Amount_Label = ctk.CTkLabel(master=Frame1,text='Source Account',font=('Poopins',20),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Source_Amount_Label.place(x=30,y=175)
            
            Source_Amount_Choice = ctk.CTkComboBox(master=Frame1,values=['Savings (Rs 12,500.00)','Current (Rs 12,500.00)'],width=270,height=40)
            Source_Amount_Choice.place(x=200,y=170)
            
            Remarks_Label = ctk.CTkLabel(master=Frame1,text='Remarks',font=('Poopins',20),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Remarks_Label.place(x=30,y=255)
            
            Remarks_Label_Entry = ctk.CTkEntry(master=Frame1,placeholder_text='Monthly Transfer',text_color='#000000',fg_color='#ffffff',bg_color='#ffffff',corner_radius=5,font=('Arial',17),width=270,height=40)
            Remarks_Label_Entry.place(x=200,y=250)
            
            Send_Money_btn = ctk.CTkButton(master=Frame1,text='Send Money',text_color='#ffffff',fg_color='#3b82f6',bg_color='#ffffff',hover_color='#2563eb',font=('Poopins',17),width=200,height=40,corner_radius=7,command=send_Money_Logic)
            Send_Money_btn.place(x=30,y=340)
            
            Cancel_btn = ctk.CTkButton(master=Frame1,border_width=1,text='Cancel',text_color='#000000',fg_color='#ffffff',hover_color='#2563eb',bg_color='#ffffff',font=('Poopins',17),width=190,height=40,corner_radius=10)
            Cancel_btn.place(x=270,y=340)
            
            Recipient_Frame = ctk.CTkFrame(master=self.Frame,width=250,height=40,fg_color='#3b82f6',bg_color='#ffffff',corner_radius=0)
            Recipient_Frame.place(x=950,y=100)
            
            Recipient_Frame_label = ctk.CTkLabel(master=Recipient_Frame,text='Recipent',font=('Poopins',20),text_color='#ffffff',fg_color='#3b82f6',bg_color='#3b82f6')
            Recipient_Frame_label.place(x=10,y=5)
            
            Detail_Recipent_Name = ctk.CTkFrame(master=self.Frame,width=250,height=190,fg_color='light gray',bg_color='#ffffff',corner_radius=0)
            Detail_Recipent_Name.place(x=950,y=140)
            
            Detail_Recipent_Name_Label = ctk.CTkLabel(master=Detail_Recipent_Name,text='Waseem',font=('Poopins',20),text_color='#000000',fg_color='light gray',bg_color='light gray')
            Detail_Recipent_Name_Label.place(x=70,y=20)
            
            Detail_Recipent_Name_Label1 = ctk.CTkLabel(master=Detail_Recipent_Name,text='Umar',font=('Poopins',20),text_color='#000000',fg_color='light gray',bg_color='light gray')
            Detail_Recipent_Name_Label1.place(x=70,y=60)
            
            Detail_Recipent_Name_Label2 = ctk.CTkLabel(master=Detail_Recipent_Name,text='Junaid',font=('Poopins',20),text_color='#000000',fg_color='light gray',bg_color='light gray')
            Detail_Recipent_Name_Label2.place(x=70,y=100)
            
            Detail_Recipent_Name_Label3 = ctk.CTkLabel(master=Detail_Recipent_Name,text='Awais',font=('Poopins',20),text_color='#000000',fg_color='light gray',bg_color='light gray')
            Detail_Recipent_Name_Label3.place(x=70,y=140)

            transaction_query1 = ""
            
        
        Send_Money_Label = ctk.CTkButton(self.Frame2,text='Send Money',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Send_Money)
        icon1 = ctk.CTkImage(light_image=Image.open('ICONS/send_imresizer.png'),dark_image=Image.open('ICONS/send_imresizer.png'),size=(23,23))
        Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
        Icon.place(x=70,y=320)
        Send_Money_Label.place(x=85,y=320)
        
        #End of Send Money Page
        
        ##*********************2***************************
        
        
        ######################3#############################
        
        def Bill_Payment():
            for widget in self.winfo_children():
                widget.destroy()
            self.Frame = ctk.CTkFrame(self,bg_color='#f7faff',corner_radius=0,width=1250,height=650,fg_color='#ffffff',background_corner_colors=['red','blue','black','white'])
            self.Frame.place(x=60,y=40)
        
            self.Frame2 = ctk.CTkFrame(self.Frame,fg_color='#3b82f6',corner_radius=0,height=650,width=300,bg_color='#f7faff')
            self.Frame2.place(x=0,y=0) 
        
            Main_Label = ctk.CTkLabel(self.Frame2,text='LedgerMate',font=('Poopins',26,"bold"),text_color='#ffffff',fg_color='#3b82f6')
            Main_Label.place(x=90,y=20)
            icon = ctk.CTkImage(light_image=Image.open('ICONS/home.png'),dark_image=Image.open('ICONS/home.png'),size=(30,30))
            Icon_Label = ctk.CTkLabel(self.Frame2,text="",image=icon,compound='left')
            Icon_Label.place(x=40,y=20)
        
            Dashboard_Label = ctk.CTkButton(self.Frame2,text='Dashboard',hover='#000000',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=self.Dashboard_Details)
            Dashboard_Label.place(x=80,y=140)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/home.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=65,y=140)
        
            Account_Details_Label = ctk.CTkButton(self.Frame2,text='Account Details',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Account_details)
            Account_Details_Label.place(x=100,y=230)
            icon = ctk.CTkImage(light_image=Image.open('ICONS/account1.png'),dark_image=Image.open('ICONS/home.png'),size=(30,30))
            Icon_Label = ctk.CTkLabel(self.Frame2,text="",image=icon,compound='left')
            Icon_Label.place(x=70,y=230)
        
            Send_Money_Label = ctk.CTkButton(self.Frame2,text='Send Money',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Send_Money)
            Send_Money_Label.place(x=85,y=320)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/send_imresizer.png'),dark_image=Image.open('ICONS/send_imresizer.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=320)
        
            Bill_Payment_Label = ctk.CTkButton(self.Frame2,text='Check Bill',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Bill_Payment)
            Bill_Payment_Label.place(x=85,y=410)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/bill_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=410)
            
            Transction_Details_Label = ctk.CTkButton(self.Frame2,text='Transction History',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Transction_History)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/history1.png'),dark_image=Image.open('ICONS/history1.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=500)
            Transction_Details_Label.place(x=100,y=500)
        
            Logout_Label = ctk.CTkButton(self.Frame2,text='Logout',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Logout)
            Logout_Label.place(x=65,y=590)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/power_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=590)
        
        
        #Main Page
        
            self.Dashobard = ctk.CTkLabel(self.Frame,text='Check Bill',font=('Poopins',36,'bold'),fg_color='#ffffff',bg_color='#ffffff',text_color='#000000')
            self.Dashobard.place(x=360,y=100)
        
            self.user_greeting_label = ctk.CTkLabel(self.Frame,text=f'Hi,{result[0]}',text_color='#6b7280',font=('Poopins',17),fg_color='#ffffff',bg_color='#ffffff')
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/user1.png'),dark_image=Image.open('ICONS/user1.png'),size=(35,35))
            Icon = ctk.CTkLabel(self.Frame,text="",image=icon1)
            Icon.place(x=1190,y=25)
            self.user_greeting_label.place(x=1090,y=30)
            
            
            Recipient_label = ctk.CTkLabel(master=self.Frame,text='Biller',font=('Poopins',20),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Recipient_label.place(x=360,y=180)
            
            Frame1 = ctk.CTkFrame(master=self.Frame,width=600,height=410,bg_color='#ffffff',fg_color='#ffffff',border_color=None,corner_radius=None)
            Frame1.place(x=330,y=230)
            
            Account_Number = ctk.CTkLabel(master=Frame1,text='Biller',font=('Poopins',20),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Account_Number.place(x=30,y=25)
            
            Account_Number_Entry = ctk.CTkComboBox(master=Frame1,values=['Electricity Bill','Gas Bill','Ptcl Bill'],width=270,height=40)
            Account_Number_Entry.place(x=200,y=20)
            
            Amount_Label = ctk.CTkLabel(master=Frame1,text='Consumer ID',font=('Poopins',20),text_color='#000000',fg_color='#ffffff',bg_color='#ffffff')
            Amount_Label.place(x=30,y=100)
            
            Amount_Label_Entry =  ctk.CTkEntry(master=Frame1,placeholder_text='1234567890',text_color='#000000',fg_color='#ffffff',bg_color='#ffffff',corner_radius=5,font=('Arial',17),width=270,height=40)
            Amount_Label_Entry.place(x=200,y=100)
            
            def pay_Bill():
                Bill_value = Account_Number_Entry.get()
                ref_id = Amount_Label_Entry.get()

                
                if not ref_id:
                    msg.showerror('Error', 'Please enter a Reference ID')
                    return
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application"
                
                if Bill_value == "Electricity Bill":

                    ref_id = ""
                    url = f"https://pescobills.pk/?ref={ref_id}"  # Example — confirm exact parameter
                    webbrowser.open(url)

                elif Bill_value == "Gas Bill":
                    webbrowser.open(f"https://suigasbil.pk/?ref_id={ref_id}")
                elif Bill_value == "Ptcl Bill":
                    webbrowser.open(f"https://ptcl.com.pk/Customer/PublicBill_Payment?ref_id={ref_id}")
            
            Send_Money_btn = ctk.CTkButton(master=Frame1,text='Pay Bill',text_color='#ffffff',fg_color='#3b82f6',bg_color='#ffffff',hover_color='#2563eb',font=('Poopins',17),width=200,height=40,corner_radius=7,command=pay_Bill)
            Send_Money_btn.place(x=30,y=240)
            
            Cancel_btn = ctk.CTkButton(master=Frame1,border_width=1,text='Cancel',text_color='#000000',fg_color='#ffffff',hover_color='#2563eb',bg_color='#ffffff',font=('Poopins',17),width=190,height=40,corner_radius=10)
            Cancel_btn.place(x=270,y=240)
            
            Recipient_Frame = ctk.CTkFrame(master=self.Frame,width=250,height=40,fg_color='#3b82f6',bg_color='#ffffff',corner_radius=0)
            Recipient_Frame.place(x=950,y=100)
            
            Recipient_Frame_label = ctk.CTkLabel(master=Recipient_Frame,text='Recipent Payments',font=('Poopins',20),text_color='#ffffff',fg_color='#3b82f6',bg_color='#3b82f6')
            Recipient_Frame_label.place(x=10,y=5)
            
            Detail_Recipent_Name = ctk.CTkFrame(master=self.Frame,width=250,height=190,fg_color='light gray',bg_color='#ffffff',corner_radius=0)
            Detail_Recipent_Name.place(x=950,y=140)
            
            Detail_Recipent_Name_Label = ctk.CTkLabel(master=Detail_Recipent_Name,text='Broadband - Paid',font=('Poopins',20),text_color='#000000',fg_color='light gray',bg_color='light gray')
            Detail_Recipent_Name_Label.place(x=30,y=20)
            
            Detail_Recipent_Name_Label1 = ctk.CTkLabel(master=Detail_Recipent_Name,text='Water Bill - Paid',font=('Poopins',20),text_color='#000000',fg_color='light gray',bg_color='light gray')
            Detail_Recipent_Name_Label1.place(x=30,y=60)
            
            Detail_Recipent_Name_Label2 = ctk.CTkLabel(master=Detail_Recipent_Name,text='Credit Card - Pending',font=('Poopins',20),text_color='#000000',fg_color='light gray',bg_color='light gray')
            Detail_Recipent_Name_Label2.place(x=30,y=100)
            
            Detail_Recipent_Name_Label3 = ctk.CTkLabel(master=Detail_Recipent_Name,text='Gas Bill - Paid',font=('Poopins',20),text_color='#000000',fg_color='light gray',bg_color='light gray')
            Detail_Recipent_Name_Label3.place(x=30,y=140)
        
            
        
        #End of Check Bill Page
        Bill_Payment_Label = ctk.CTkButton(self.Frame2,text='Check Bill',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Bill_Payment)
        icon1 = ctk.CTkImage(light_image=Image.open('ICONS/bill_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
        Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
        Icon.place(x=70,y=410)
        Bill_Payment_Label.place(x=85,y=410)
        
        #*********************3*****************************
        
        def Transction_History():
            for widget in self.winfo_children():
                widget.destroy()

            self.Frame = ctk.CTkFrame(self,bg_color='#f7faff',corner_radius=0,width=1250,height=650,fg_color='#ffffff',background_corner_colors=['red','blue','black','white'])
            self.Frame.place(x=60,y=40)
        
            self.Frame2 = ctk.CTkFrame(self.Frame,fg_color='#3b82f6',corner_radius=0,height=650,width=300,bg_color='#f7faff')
            self.Frame2.place(x=0,y=0) 
        
            Main_Label = ctk.CTkLabel(self.Frame2,text='LedgerMate',font=('Poopins',26,"bold"),text_color='#ffffff',fg_color='#3b82f6')
            icon = ctk.CTkImage(light_image=Image.open('ICONS/home.png'),dark_image=Image.open('ICONS/home.png'),size=(30,30))
            Icon_Label = ctk.CTkLabel(self.Frame2,text="",image=icon,compound='left')
            Icon_Label.place(x=40,y=20)
            Main_Label.place(x=90,y=20)
        
            Dashboard_Label = ctk.CTkButton(self.Frame2,text='Dashboard',hover='#000000',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=self.Dashboard_Details)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/home.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=65,y=140)
            Dashboard_Label.place(x=80,y=140)
        
            Account_Details_Label = ctk.CTkButton(self.Frame2,text='Account Details',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Account_details)
            Account_Details_Label.place(x=100,y=230)
            icon = ctk.CTkImage(light_image=Image.open('ICONS/account1.png'),dark_image=Image.open('ICONS/home.png'),size=(30,30))
            Icon_Label = ctk.CTkLabel(self.Frame2,text="",image=icon,compound='left')
            Icon_Label.place(x=70,y=230)
        
            Send_Money_Label = ctk.CTkButton(self.Frame2,text='Send Money',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Send_Money)
            Send_Money_Label.place(x=85,y=320)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/send_imresizer.png'),dark_image=Image.open('ICONS/send_imresizer.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=320)
        
            Bill_Payment_Label = ctk.CTkButton(self.Frame2,text='Check Bill',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Bill_Payment)
            Bill_Payment_Label.place(x=85,y=410)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/bill_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=410)
            
            Transction_Details_Label = ctk.CTkButton(self.Frame2,text='Transction History',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Transction_History)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/history1.png'),dark_image=Image.open('ICONS/history1.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=500)
            Transction_Details_Label.place(x=100,y=500)
        
            Logout_Label = ctk.CTkButton(self.Frame2,text='Logout',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Logout)
            Logout_Label.place(x=65,y=590)
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/power_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
            Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
            Icon.place(x=70,y=590)
        
        
        #Main Page
        
            self.Dashobard = ctk.CTkLabel(self.Frame,text='Transction History',font=('Poopins',26,'bold'),fg_color='#ffffff',bg_color='#ffffff',text_color='#000000')
            self.Dashobard.place(x=330,y=30)
        
            self.user_greeting_label = ctk.CTkLabel(self.Frame,text=f'Hi,{result[0]}',text_color='#6b7280',font=('Poopins',17),fg_color='#ffffff',bg_color='#ffffff')
            icon1 = ctk.CTkImage(light_image=Image.open('ICONS/user1.png'),dark_image=Image.open('ICONS/user1.png'),size=(35,35))
            Icon = ctk.CTkLabel(self.Frame,text="",image=icon1)
            Icon.place(x=1190,y=25)
            self.user_greeting_label.place(x=1090,y=30)
        
            Frame_Details = ctk.CTkFrame(master=self.Frame,width=890,height=520,fg_color='#ffffff',bg_color='#ffffff',border_width=2,border_color='#ffffff',corner_radius=0)
            Frame_Details.place(x=330,y=100)
            
            columns = ("username","Account_No","Name","Transfer_type","Send_amount","Date")
            
                        # Paste this inside Transction_History() function 
            # right after the scrollbar is placed and before the function ends

            def generate_pdf():
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", 'B', 18)
                pdf.set_text_color(59, 130, 246)
                pdf.cell(0, 15, "LedgerMate - Transaction History", ln=1, align='C')
                pdf.ln(10)

                pdf.set_font("Arial", 'B', 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(0, 10, f"Account Holder: {result[0]} {L_Name[0]}", ln=1)
                pdf.cell(0, 10, f"Account Number: {Acc_no_fetch[0]}", ln=1)
                pdf.cell(0, 10, f"Generated: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}", ln=1)
                pdf.ln(10)

                # Header
                pdf.set_font("Arial", 'B', 11)
                pdf.set_fill_color(59, 130, 246)
                pdf.set_text_color(255, 255, 255)
                headers = ["Date", "Type", "Amount", "Receiver", "ID"]
                widths = [35, 40, 35, 50, 30]
                for i in range(len(headers)):
                    pdf.cell(widths[i], 10, headers[i], 1, 0, 'C', fill=True)
                pdf.ln()

                # Rows
                pdf.set_font("Arial", size=10)
                pdf.set_text_color(0, 0, 0)
                for item in tree.get_children():
                    vals = tree.item(item)['values']
                    pdf.cell(widths[0], 10, str(vals[5]), 1)                      # Date
                    pdf.cell(widths[1], 10, str(vals[3]), 1)                      # Transfer Type
                    pdf.cell(widths[2], 10, f"Rs {float(vals[2]):,.2f}", 1, align='R')  # Amount
                    pdf.cell(widths[3], 10, str(vals[4]), 1)                      # Receiver
                    pdf.cell(widths[4], 10, str(vals[0]), 1)                      # ID
                    pdf.ln()


                filename = f"Transaction_History_{Acc_no_fetch[0]}_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
                filepath = os.path.join(os.path.expanduser("~"), "Downloads", filename)
                pdf.output(filepath)
                msg.showinfo("Success", f"PDF Generated!\nSaved in Downloads folder\n{filename}")
                os.startfile(filepath)  # Opens the PDF (Windows only)

            # Generate PDF Button
            generate_btn = ctk.CTkButton(
                Frame_Details,
                text="Generate PDF",
                fg_color="#3b82f6",
                hover_color="#1d4ed8",
                text_color="white",
                font=('Poopins', 16, 'bold'),
                width=200,
                height=45,
                corner_radius=10,
                command=generate_pdf
            )
            generate_btn.place(x=650, y=460)
            
            tree = ttk.Treeview(Frame_Details, columns=columns, show="headings", height=19)

            tree.heading("username", text="id")
            tree.heading("Account_No", text="Account Number")
            tree.heading("Name", text="Amount")
            tree.heading("Transfer_type", text="Transfer Type")
            tree.heading("Send_amount", text="Reciever")
            tree.heading("Date", text="Date")

            for col in columns:
                tree.column(col, width=120)

            # Connect to MySQL and fetch data
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="LedgerMage"
            )
            cursor = conn.cursor()
            history_query = "SELECT id,Account_Number,Amount, Transfer_Type, Receiver_or_Biller,Transaction_Date FROM Transaction_History WHERE Account_Number = %s"
            cursor.execute(history_query,(Acc_no_fetch[0],))

            data = cursor.fetchall()  # list of tuples

            # Insert each row into Treeview
            for row in data:
                tree.insert("", "end", values=row)

            # Add vertical scrollbar
            scroolbar = ttk.Scrollbar(Frame_Details, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scroolbar.set)

            tree.place(x=10, y=5)
            scroolbar.place(x=10 + len(columns)*120, y=5, height=19*20)  # adjust position & height

            conn.close()

            # scroolbar.place(x=370,y=150)
            
        
        
        
        Transction_Details_Label = ctk.CTkButton(self.Frame2,text='Transction History',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Transction_History)
        icon1 = ctk.CTkImage(light_image=Image.open('ICONS/history1.png'),dark_image=Image.open('ICONS/history1.png'),size=(23,23))
        Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
        Icon.place(x=70,y=500)
        Transction_Details_Label.place(x=100,y=500)
        #############################4#############################
        #Logout Page
        
        def Logout():
              info =  msg.askyesno('Warning','Do You Want To Logout') 
              if info:
                  Dashboard.destroy(self)
                  return
              else:
                  return
        Logout_Label = ctk.CTkButton(self.Frame2,text='Logout',hover_color='#3b82f6',fg_color='#3b82f6',bg_color='#3b82f6',corner_radius=0,text_color='#ffffff',font=('Poopins',18,"bold"),command=Logout)
        icon1 = ctk.CTkImage(light_image=Image.open('ICONS/power_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(23,23))
        Icon = ctk.CTkLabel(self.Frame2,text="",image=icon1,compound='left')
        Icon.place(x=70,y=590)
        Logout_Label.place(x=65,y=590)
        
        #End of Logout Page   
        
        #**************************4********************************
        
        
        #Main Page
        
        self.Dashobard = ctk.CTkLabel(self.Frame,text='Dashboard',font=('Poopins',26,'bold'),fg_color='#ffffff',bg_color='#ffffff',text_color='#000000')
        self.Dashobard.place(x=330,y=30)
        
        self.user_greeting_label = ctk.CTkLabel(self.Frame,text=f'Hi,{result[0]}',text_color='#6b7280',font=('Poopins',17),fg_color='#ffffff',bg_color='#ffffff')
        icon1 = ctk.CTkImage(light_image=Image.open('ICONS/user1.png'),dark_image=Image.open('ICONS/user1.png'),size=(35,35))
        Icon = ctk.CTkLabel(self.Frame,text="",image=icon1,compound='left')
        Icon.place(x=1190,y=25)
        self.user_greeting_label.place(x=1090,y=30)
        
        self.Current_Balance_Label = ctk.CTkLabel(self.Frame,text='Current Balance',text_color='#6b7280',font=('Poopins',27),fg_color='#ffffff',bg_color='#ffffff')
        self.Current_Balance_Label.place(x=330,y=130)
        
        self.Balance_Details = ctk.CTkLabel(self.Frame,text=f'RS {Balance[0]}',text_color='#000000',font=('Poopins',38,'bold'),bg_color='#ffffff',fg_color='#ffffff')
        self.Balance_Details.place(x=330,y=180)
        
        self.Account_Details = ctk.CTkButton(self.Frame,text='View Account Details',text_color='#ffffff',fg_color='#3b82f6',bg_color='#ffffff',hover_color='#2563eb',font=('Poopins',17),width=250,height=40,corner_radius=10,command=Account_details)
        self.Account_Details.place(x=960,y=183)
        
        self.Send_Money_btn = ctk.CTkButton(self.Frame,text='Send Money',hover_color='#ffffff',text_color='#111827',fg_color='#ffffff',corner_radius=0,border_color='#6b7280',border_width=1,width=340,height=100,font=('Poopins',26,"bold"),command=Send_Money)
        self.Send_Money_btn.place(x=330,y=300)
        icon1 = ctk.CTkImage(light_image=Image.open('ICONS/send_imresizer.png'),dark_image=Image.open('ICONS/send_imresizer.png'),size=(35,35))
        Icon = ctk.CTkLabel(self.Frame,text="",image=icon1,compound='left',bg_color='#ffffff',fg_color='#ffffff')
        Icon.place(x=370,y=320)
        
        self.Bill_Payment_btn = ctk.CTkButton(self.Frame,text='Check Bill',hover_color='#ffffff',text_color='#111827',fg_color='#ffffff',corner_radius=0,border_color='#6b7280',border_width=1,width=340,height=100,font=('Poopins',26,"bold"),command=Bill_Payment)
        self.Bill_Payment_btn.place(x=700,y=300)
        icon1 = ctk.CTkImage(light_image=Image.open('ICONS/bill_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(35,35))
        Icon = ctk.CTkLabel(self.Frame,text="",image=icon1,compound='left',bg_color='#ffffff',fg_color='#ffffff')
        Icon.place(x=730,y=320)
        
        self.Transaction_History_btn = ctk.CTkButton(self.Frame,text='Transction\nHistory',hover_color='#ffffff',text_color='#111827',fg_color='#ffffff',corner_radius=0,border_color='#6b7280',border_width=1,width=340,height=100,font=('Poopins',26,"bold"),command=Transction_History)
        self.Transaction_History_btn.place(x=330,y=460)
        icon1 = ctk.CTkImage(light_image=Image.open('ICONS/history1.png'),dark_image=Image.open('ICONS/home.png'),size=(35,35))
        Icon = ctk.CTkLabel(self.Frame,text="",image=icon1,compound='left',bg_color='#ffffff',fg_color='#ffffff')
        Icon.place(x=370,y=480)
        
        self.Logout_btn = ctk.CTkButton(self.Frame,text='Logout',hover_color='#ffffff',text_color='#111827',fg_color='#ffffff',corner_radius=0,border_color='#6b7280',border_width=1,width=340,height=100,font=('Poopins',26,"bold"),command=Logout)
        self.Logout_btn.place(x=700,y=460)
        icon1 = ctk.CTkImage(light_image=Image.open('ICONS/power_imresizer.png'),dark_image=Image.open('ICONS/home.png'),size=(35,35))
        Icon = ctk.CTkLabel(self.Frame,text="",image=icon1,compound='left',bg_color='#ffffff',fg_color='#ffffff')
        Icon.place(x=740,y=480)
        
        
        
        
    
        
if __name__ == "__main__":
    App = Dashboard()
    App.mainloop()