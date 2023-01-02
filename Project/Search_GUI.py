from tkinter import *
# from PIL import ImageTk,Image
from tkinter import messagebox
import customtkinter
import os

directory = r"F:/Masters/Semester1/APP/project"
os.chdir(directory)

from Search_func import *

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# Creating the root window, assinging the name, and the icon

s_gui = customtkinter.CTk()
s_gui.title("Product Search")
# s_gui.geometry("265x400")
s_gui.iconbitmap('f:/masters/semester1/app/project/images/logo.ico')

# Frame to highlight the search functions

srh_frame = customtkinter.CTkFrame(master = s_gui)
srh_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Data base selection 

srh_data = customtkinter.CTkLabel(master=srh_frame, text="Search Database")
srh_data.grid(row=0, column=0, padx=5, pady=5)

options = ['honda','suzuki','toyota']

srh_data_ent = customtkinter.CTkOptionMenu(srh_frame, values = ['honda','suzuki','toyota'])
# srh_data_ent = Entry(srh_frame, text="Select Database to Search from")
srh_data_ent.grid(row=0, column=1, padx=5, pady=5)

# Search by Product ID

id_srh = customtkinter.CTkLabel(srh_frame, text="Product ID")
id_srh.grid(row=1,column=0, padx=5,pady=5)

id_srh_ent = customtkinter.CTkEntry(srh_frame, placeholder_text="Enter Product ID")
id_srh_ent.grid(row=1, column=1, padx=5, pady=5)

# Search by product Name

name_srh = customtkinter.CTkLabel(srh_frame, text="Product Name")
name_srh.grid(row=2, column=0, padx=5, pady=5)

name_srh_ent = customtkinter.CTkEntry(srh_frame, placeholder_text="Enter Product Name")
name_srh_ent.grid(row=2,column=1, padx=5, pady=5)

#Importing the Search function from additional file and using it for 
#the search function

def srh():
    data_local = srh_data_ent.get()
    pid = id_srh_ent.get()
    name = name_srh_ent.get()
    search = Search(data_local,pid,name,s_gui)
    name_srh_ent.delete(0, 'end')
    id_srh_ent.delete(0, 'end')
    if any(chr.isdigit() for chr in name):
        messagebox.showerror("Error", "Please enter a valid Item name!")
    elif any(chr.isalpha() for chr in str(pid)):
        messagebox.showerror("Error", "Please enter a valid Item ID!")
    else:
        search.srh_data()
   
       

# Button for the search command

srh_but = customtkinter.CTkButton(srh_frame, text="Search", command = srh)
srh_but.grid(row=3, column=1, padx=5, pady=5)

# Adding additonal filters for advanced search

srh_filter = customtkinter.CTkFrame(s_gui)
srh_filter.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Adding features for the filter search

srh_year = customtkinter.CTkLabel(srh_filter, text = "Year")
srh_assem = customtkinter.CTkLabel(srh_filter, text= "Assembly")
srh_cost = customtkinter.CTkLabel(srh_filter, text = "Cost")
srh_quant = customtkinter.CTkLabel(srh_filter, text = "Quantity")

srh_year_ent = customtkinter.CTkEntry(srh_filter, placeholder_text="Enter Year")
srh_assem_ent = customtkinter.CTkEntry(srh_filter, placeholder_text="Enter Assembly")
srh_cost_ent = customtkinter.CTkEntry(srh_filter, placeholder_text="Enter Cost")
srh_quant_ent = customtkinter.CTkEntry(srh_filter, placeholder_text="Enter Quantity")

# Putting the filter search on the screen

srh_year.grid(row=0, column=0, padx=5, pady=5)
srh_assem.grid(row=1, column=0, padx=5, pady=5)
srh_cost.grid(row=2, column=0, padx=5, pady=5)
srh_quant.grid(row=3, column=0, padx=5, pady=5)
srh_year_ent.grid(row=0, column=1, padx=5, pady=5)
srh_assem_ent.grid(row=1, column=1, padx=5, pady=5)
srh_cost_ent.grid(row=2, column=1, padx=5, pady=5)
srh_quant_ent.grid(row=3, column=1, padx=5, pady=5)

def filter_search():
    data_local = srh_data_ent.get()
    year_local = srh_year_ent.get()
    cost_local = srh_cost_ent.get()
    quant_local = srh_quant_ent.get()
    assem_local = srh_assem_ent.get()
    fil_srch = fil_srh(s_gui, data_local, year_local, cost_local, assem_local, quant_local)
    srh_year_ent.delete(0, 'end')
    srh_cost_ent.delete(0, 'end')
    srh_quant_ent.delete(0, 'end')
    srh_assem_ent.delete(0, 'end')
    if any(chr.isdigit() for chr in assem_local):
        messagebox.showerror("Error", "Please enter a valid Item Assembly!")
    elif any(chr.isalpha() for chr in str(year_local)) or any(chr.isalpha() for chr in str(cost_local)) or any(chr.isalpha() for chr in str(quant_local)):
        messagebox.showerror("Error", "Please enter a valid input!")
    else:
        fil_srch.filter_srh()

# Button for filter search

filter_but = customtkinter.CTkButton(srh_filter, text="Filter Search", command = filter_search)
filter_but.grid(row=4,column=0,columnspan=2,padx=5,pady=5)


# Exit button to close the window

def exit_win():
    s_gui.destroy()
exit_but = customtkinter.CTkButton(s_gui, text="Exit", command = exit_win )
exit_but.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


s_gui.mainloop()