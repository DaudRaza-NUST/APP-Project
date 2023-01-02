from tkinter import *
import mysql.connector
import customtkinter
from tkinter import messagebox
import os 

directory = r"F:/Masters/Semester1/APP/project"
os.chdir(directory)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# Creating the root window, assinging the name, and the icon

L_gui = customtkinter.CTk()
L_gui.title("Product Search")
# L_gui.geometry("265x125")
L_gui.iconbitmap('f:/masters/semester1/app/project/images/logo.ico')

username = customtkinter.CTkLabel(master= L_gui, text="Enter username: ")
username.grid(row=0, column=0, padx=5, pady=5)


user_enter = customtkinter.CTkEntry(L_gui, placeholder_text="Enter username")
user_enter.grid(row=0, column=1, padx=5, pady=5)

password = customtkinter.CTkLabel(master= L_gui, text="Enter password: ")
password.grid(row=1, column=0, padx=5, pady=5)


password_enter = customtkinter.CTkEntry(L_gui, placeholder_text="Enter password", show='*')
password_enter.grid(row=1, column=1, padx=5, pady=5)

def Log (event):
            user = user_enter.get()
            password = password_enter.get()
    
            itemdb = mysql.connector.connect(
                host = "localhost",
                database = "app_project",
                user = "root",
                password = "project1234"
            )
            
            query = "select * from login WHERE login.UserID = " + "'" + str(password) + "'" + " AND " + "login.UserName = " + "'" + str(user) + "'"
            
            mycurser = itemdb.cursor()
            mycurser.execute(query)
            records = mycurser.fetchall()
            
            if records == []:
                msg = messagebox.showerror("Error", "User does not exist!")
            else:
                L_gui.destroy()
                os.system('python Menu.py')
                        
            
login_but = customtkinter.CTkButton(L_gui, text="Log in", command = Log)
login_but.grid(row=2, column=0, columnspan = 2 , padx=5, pady=5)

L_gui.bind('<Return>', Log)

L_gui.mainloop()