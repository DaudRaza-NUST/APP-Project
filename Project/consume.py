from tkinter import *
from tkinter import messagebox
import customtkinter
import mysql.connector

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("green")

c_gui = customtkinter.CTk()
c_gui.title("Consume Product")
# c_gui.geometry("265x230")
c_gui.iconbitmap('f:/masters/semester1/app/project/images/logo.ico')

cp_frame = customtkinter.CTkFrame(master = c_gui)
cp_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

cp_data = customtkinter.CTkLabel(master=cp_frame, text="Category")
cp_data.grid(row=0, column=0, padx=5, pady=5)

#Category Selection
options = ['honda','suzuki','toyota']
cp_data_ent = customtkinter.CTkOptionMenu(cp_frame, values = ['honda','suzuki','toyota'])
cp_data_ent.grid(row=0, column=1, padx=5, pady=5)

#enter product name

name_cp = customtkinter.CTkLabel(cp_frame, text="Product Name")
name_cp.grid(row=2, column=0, padx=5, pady=5)

name_cp_ent = customtkinter.CTkEntry(cp_frame, placeholder_text="Enter Product Name")
name_cp_ent.grid(row=2,column=1, padx=5, pady=5)


# add consumed quantity

qnt_cp = customtkinter.CTkLabel(cp_frame, text="Consumed Quantity")
qnt_cp.grid(row=6, column=0, padx=5, pady=5)

qnt_cp_ent = customtkinter.CTkEntry(cp_frame, placeholder_text="Add Consumed Quantity")
qnt_cp_ent.grid(row=6, column=1, padx=5, pady=5)

def consume_product():
    
    category=cp_data_ent.get()    
    name=name_cp_ent.get()    
    quantity = qnt_cp_ent.get()
    name_cp_ent.delete(0, 'end')
    qnt_cp_ent.delete(0, 'end')
    
    if quantity<='0':
        err_message = messagebox.showerror(title="Error",message=("Unconsumable Quantity"))
        
    
        
    itemdb = mysql.connector.connect(
        host = "localhost",
        database = "app_project",
        user = "root",
        password = "project1234"
        )
    if category=='honda':
        query_3="select ItemQuant from honda where ItemName= %s"
        qnt_imp=(name,)
        mycurser1 = itemdb.cursor()
        mycurser1.execute(query_3,qnt_imp)
        previous_qunatity = mycurser1.fetchone()
        itemdb.commit()
    elif category=='suzuki':
         query_3="select ItemQuant from suzuki where ItemName= %s"
         qnt_imp=(name,)
         mycurser1 = itemdb.cursor()
         mycurser1.execute(query_3,qnt_imp)
         previous_qunatity = mycurser1.fetchone()
         itemdb.commit()
    elif category=='toyota':
         query_3="select ItemQuant from toyota where ItemName= %s"
         qnt_imp=(name,)
         mycurser1 = itemdb.cursor()
         mycurser1.execute(query_3,qnt_imp)
         previous_qunatity = mycurser1.fetchone()
         itemdb.commit()
  
    previous_qnt_int=int(previous_qunatity[0])
   
    quantity_int=int(quantity)
    
    print(previous_qnt_int)
    print(quantity_int)
  
    
    new_quantity=previous_qnt_int-quantity_int
    
    print(new_quantity)
    
    if new_quantity < 0:
        err_message = messagebox.showerror(title="Error",message=("Less QUantity Available, Can't consume this product"))
    elif category=='honda':
       
        query_2="UPDATE honda SET ItemQuant = %s WHERE ItemName = %s"
        value=(new_quantity, name)
        mycurser = itemdb.cursor()
        mycurser.execute(query_2,value)
        itemdb.commit()
    elif category=='suzuki':
        query_2="UPDATE suzuki SET ItemQuant = %s WHERE ItemName = %s"
        value=(new_quantity, name)
        mycurser = itemdb.cursor()
        mycurser.execute(query_2,value)
   
        itemdb.commit()
    elif category=='toyota':
        query_2="UPDATE toyota SET ItemQuant = %s WHERE ItemName = %s"
        value=(new_quantity, name)
        mycurser = itemdb.cursor()
        mycurser.execute(query_2,value)
        itemdb.commit()


consume_but = customtkinter.CTkButton(cp_frame, text="Consume", command = consume_product)
consume_but.grid(row=7, column=1, padx=5, pady=5)

def exiting():
    c_gui.destroy()


# Button for the Exiting

cp_ext = customtkinter.CTkButton(c_gui,text="Exit", command = exiting)
cp_ext.grid(row=8, column=1, padx=5, pady=5)

c_gui.mainloop()