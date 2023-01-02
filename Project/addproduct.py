from tkinter import *
# from PIL import ImageTk,Image
from tkinter import messagebox
import customtkinter
import mysql.connector

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("green")

a_gui = customtkinter.CTk()
a_gui.title("Add Product")
# a_gui.geometry("265x350")
a_gui.iconbitmap('f:/masters/semester1/app/project/images/logo.ico')

adp_frame = customtkinter.CTkFrame(master = a_gui)
adp_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

adp_data = customtkinter.CTkLabel(master=adp_frame, text="Add New Product")
adp_data.grid(row=0, column=0, padx=5, pady=5)




options = ['honda','suzuki','toyota']

adp_data_ent = customtkinter.CTkOptionMenu(adp_frame, values = ['honda','suzuki','toyota'])
# srh_data_ent = Entry(srh_frame, text="Select Database to Search from")
adp_data_ent.grid(row=0, column=1, padx=5, pady=5)

#add product I'D

id_adp = customtkinter.CTkLabel(adp_frame, text="Product ID")
id_adp.grid(row=1,column=0, padx=5,pady=5)

id_adp_ent = customtkinter.CTkEntry(adp_frame, placeholder_text="Add Product ID")
id_adp_ent.grid(row=1, column=1, padx=5, pady=5)


# add product Name

name_adp = customtkinter.CTkLabel(adp_frame, text="Product Name")
name_adp.grid(row=2, column=0, padx=5, pady=5)

name_adp_ent = customtkinter.CTkEntry(adp_frame, placeholder_text="Add Product Name")
name_adp_ent.grid(row=2,column=1, padx=5, pady=5)


# add year 

year_adp = customtkinter.CTkLabel(adp_frame, text="Product Year")
year_adp.grid(row=3, column=0, padx=5, pady=5)

year_adp_ent = customtkinter.CTkEntry(adp_frame, placeholder_text="Add year")
year_adp_ent.grid(row=3,column=1, padx=5, pady=5)

# add assembly 

asm_adp = customtkinter.CTkLabel(adp_frame, text="Product Assembly")
asm_adp.grid(row=4, column=0, padx=5, pady=5)

asm_adp_ent = customtkinter.CTkEntry(adp_frame, placeholder_text="Add Assembly")
asm_adp_ent.grid(row=4, column=1, padx=5, pady=5)


# add cost 

cost_adp = customtkinter.CTkLabel(adp_frame, text="Product Cost")
cost_adp.grid(row=5, column=0, padx=5, pady=5)

cost_adp_ent = customtkinter.CTkEntry(adp_frame, placeholder_text="Add Product Cost")
cost_adp_ent.grid(row=5, column=1, padx=5, pady=5)

# add quantity

qnt_adp = customtkinter.CTkLabel(adp_frame, text="Product Quantity")
qnt_adp.grid(row=6, column=0, padx=5, pady=5)

qnt_adp_ent = customtkinter.CTkEntry(adp_frame, placeholder_text="Add Product Quantity")
qnt_adp_ent.grid(row=6, column=1, padx=5, pady=5)


def add_product():
    
    category=adp_data_ent.get()
    userid=id_adp_ent.get()
    name=name_adp_ent.get()
    year=year_adp_ent.get()
    assembly=asm_adp_ent.get()
    cost=cost_adp_ent.get()
    quantity = qnt_adp_ent.get()
    id_adp_ent.delete(0, 'end')
    name_adp_ent.delete(0, 'end')
    year_adp_ent.delete(0, 'end')
    asm_adp_ent.delete(0, 'end')
    cost_adp_ent.delete(0, 'end')
    qnt_adp_ent.delete(0, 'end')
    itemdb = mysql.connector.connect(
        host = "localhost",
        database = "app_project",
        user = "root",
        password = "project1234"
        )
    
    
    if category=='honda':
        query1='INSERT INTO honda(`ID`, `ItemName`, `ItemAssem`, `ItemQuant`, `ItemCost`, `ItemYear`) VALUES (%s, %s, %s, %s, %s, %s)'
        mycurser = itemdb.cursor()
        record1=(userid,name,assembly,quantity,cost,year)
        mycurser.execute(query1,record1)
        itemdb.commit()
    
    elif category=='suzuki':
        query1='INSERT INTO suzuki(`ID`, `ItemName`, `ItemAssem`, `ItemQuant`, `ItemCost`, `ItemYear`) VALUES (%s, %s, %s, %s, %s, %s)'
        mycurser = itemdb.cursor()
        record1=(userid,name,assembly,quantity,cost,year)
        mycurser.execute(query1,record1)
        itemdb.commit()
        
    elif category=='toyota':
        query1='INSERT INTO toyota(`ID`, `ItemName`, `ItemAssem`, `ItemQuant`, `ItemCost`, `ItemYear`) VALUES (%s, %s, %s, %s, %s, %s)'
        mycurser = itemdb.cursor()
        record1=(userid,name,assembly,quantity,cost,year)
        mycurser.execute(query1,record1)
        itemdb.commit()
    else:
       err_message = messagebox.showerror(title="Error",message=("category does not exist"))
    

# Button for the Adding Product

adp_but = customtkinter.CTkButton(adp_frame, text="ADD", command = add_product)
adp_but.grid(row=7, column=1, padx=5, pady=5)

def exiting():
    a_gui.destroy()


# Button for the Exiting

adp_ext = customtkinter.CTkButton(a_gui,text="Exit", command = exiting)
adp_ext.grid(row=8, column=1, padx=5, pady=5)

a_gui.mainloop()