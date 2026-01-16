import mysql.connector
import customtkinter as ctk
from tkinter import messagebox as msg
from PIL import Image,ImageTk
import os
# import pyfingerprint

ctk.set_default_color_theme('blue')

class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.configure(fg_color='#E1E5EB')
        self.title('LedgerMage Login')
        self.geometry('900x600')
        self.resizable(False,False)
        # self.set_bg_image()
        self.LoginFrame()
        
    def LoginFrame(self):
        def open_Registration():
            os.system('python Register.py')
            
        def Login_Success():
        
            
            try:
                if username_entry.get() != "" and password_entry.get() != "":
                    conn = mysql.connector.connect(
                        host = 'localhost',
                        user = 'root',
                        database = 'LedgerMage',
                        password = 'your password'
                    )   
                    msg.showinfo('Sucess','Database Connected Sucessfully')
                    username = username_entry.get()
                    password = password_entry.get()
                    
                    cursor = conn.cursor()
                    query = "Select Account_Number from Login where Username=%s AND password_user=%s"
                    cursor.execute(query,(username,password))
                    result = cursor.fetchone()
                    primary_key_id = result
                    
                    with open('Name.txt','w') as f:
                        f.write(str(primary_key_id))
                    
                    if result:
                        username_entry.delete(0,ctk.END)
                        password_entry.delete(0,ctk.END)
                        msg.showinfo('Sucess','Login Sucess')
                        LoginPage.destroy(self)
                        os.system('python Dashboard.py')
                    else:
                        username_entry.delete(0,ctk.END)
                        password_entry.delete(0,ctk.END)
                        return msg.showerror('Failed','Login Failed Account Not Exists')
                else:
                    return msg.showwarning('Error','Fields Must be Filled')
            except Exception as e:
                msg.showerror('Error',str(e))
                conn.commit()
                conn.close()
            
                          
        label = ctk.CTkLabel(self,text='Login To LedgerMate',text_color='#000000',font=('Arial Rounded MT Bold',34))
        label.place(x=270,y=100)    
        
        username_entry = ctk.CTkEntry(self,text_color='#000000',bg_color='#e1e5eb',placeholder_text="Username",placeholder_text_color='#a0a0a0',fg_color='#f7f9fb',corner_radius=0,width=340,height=40,font=('Poopins',18))
        username_entry.place(x=270,y=165)
        
        password_entry = ctk.CTkEntry(self,text_color='#000000',bg_color='#e1e5eb',placeholder_text="Password",placeholder_text_color='#a0a0a0',fg_color='#f7f9fb',corner_radius=0,width=340,height=40,show='*',font=('Poopins',18))
        password_entry.place(x=270,y=224)
        
        Finger_Print = ctk.CTkButton(self,text='Finger Print',text_color='#ffffff',fg_color='blue',hover_color='orange',corner_radius=10,width=340,height=40,font=('Arial Rounded MT Bold',18))
        Finger_Print.place(x=270,y=285)
        
        Login_btn = ctk.CTkButton(self,text='Login',text_color='#ffffff',fg_color='blue',hover_color='orange',corner_radius=10,width=340,height=40,font=('Arial Rounded MT Bold',18),command=Login_Success)
        Login_btn.place(x=270,y=340)
        
        dont_have_acc_label = ctk.CTkLabel(self,text="Don't have an account?",text_color='blue',font=('Arial',16))
        dont_have_acc_label.place(x=350,y=400)
        
        Register_User_btn = ctk.CTkButton(self,text='Register Here',fg_color='blue',text_color='#ffffff',hover_color='orange',corner_radius=10,width=140,height=40,font=('Arial Rounded MT Bold',18),command=open_Registration)
        Register_User_btn.place(x=350,y=455)
        
        
if __name__ == "__main__":
    App = LoginPage()
    App.mainloop()