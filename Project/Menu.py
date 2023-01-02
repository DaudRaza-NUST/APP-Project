from tkinter import *
from tkinter import messagebox
import customtkinter
import os

directory = r"F:/Masters/Semester1/APP/project"
os.chdir(directory)

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("green")

menu = customtkinter.CTk()
menu.title('Main Menu')
menu.iconbitmap('f:/masters/semester1/app/project/images/logo.ico')

menu_lab = customtkinter.CTkLabel(menu, text='Automotive Inventory Database')
menu_lab.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

menu_frame = customtkinter.CTkFrame(menu)
menu_frame.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

def search():
    os.system('python Search_GUI.py')

srh_but = customtkinter.CTkButton(menu_frame, text="Search Database", command = search)
srh_but.grid(row=0, column=0, padx=5, pady=5)

def add():
    os.system('python addproduct.py')

add_but = customtkinter.CTkButton(menu_frame, text="Add Product", command = add)
add_but.grid(row=1, column=0, padx=5, pady=5)

def consume():
    os.system('python consume.py')

con_but = customtkinter.CTkButton(menu_frame, text="Consume Product", command = consume)
con_but.grid(row=2, column=0, padx=5, pady=5)

def logout():
    menu.destroy()
    os.system('python login.py')

logout_but = customtkinter.CTkButton(menu, text="Logout", command = logout)
logout_but.grid(row=2, column=0, padx=5, pady=5, columnspan=2)


menu.mainloop()