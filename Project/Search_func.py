import mysql.connector
from tkinter import *
import customtkinter
from tkinter import messagebox

class Search(object):
    
    def __init__(self,data,pid,name,ui):
        self.data = data
        self.pid = pid
        self.name = name
        self.ui = ui
        
        
    def return_win(self,records):
        
        return_srh = customtkinter.CTkToplevel(self.ui)
        return_srh.title("Search Result")
        return_srh.iconbitmap('f:/masters/semester1/app/project/images/logo.ico')
        # return_srh.geometry("850x200")
        record_fr = customtkinter.CTkFrame(return_srh)
        record_fr.grid(row=0, column=0 ,columnspan=6, padx=5, pady=5)
        
        id_head = customtkinter.CTkLabel(record_fr, text="ID")
        id_name = customtkinter.CTkLabel(record_fr, text="Description")
        id_assem = customtkinter.CTkLabel(record_fr, text="Assembly")
        id_quant = customtkinter.CTkLabel(record_fr, text="Quantity")
        id_cost = customtkinter.CTkLabel(record_fr, text="Cost")
        id_year = customtkinter.CTkLabel(record_fr, text="Year")
        id_head.grid(row=0, column=0)
        id_name.grid(row=0, column=1)
        id_assem.grid(row=0, column=2)
        id_quant.grid(row=0, column=3)
        id_cost.grid(row=0, column=4)
        id_year.grid(row=0, column=5)
        
        i = 0
        for rows in records:
            for j in range(len(rows)):
                e = customtkinter.CTkEntry(record_fr) 
                e.grid(row=i+1, column=j)
                e.insert(END, rows[j])
            i += 1
            
        exit_srh = customtkinter.CTkButton(return_srh, text = "Exit", command = return_srh.destroy)
        exit_srh.grid(row=1, column=2, columnspan=2)
        return_srh.mainloop()
        
    def srh_data(self):
        try:
            itemdb = mysql.connector.connect(
                host = "localhost",
                database = "app_project",
                user = "root",
                password = "project1234"
            )
            data_local = self.data
            pid = self.pid
            name = self.name
            ui = self.ui
            
            if name == "" and pid == "" and data_local != "":
                
                sql_slt_query = "select * from " + data_local

                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                
                self.return_win(records)
                
            
            elif name == "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".id" + " = " + str(pid)
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
            elif pid == "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemName" + " = " + "'" + str(name) +  "'"
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
                
            else:
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemName" + " = " + "'" + str(name) +  "'" + " AND " + data_local + ".id" + " = " + str(pid)
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
                
        except mysql.connector.Error as e:
            err_message = messagebox.showerror(title="Error",message=("Please enter a valid input!"))
            
        finally:
            
            if itemdb.is_connected():
                itemdb.close()
                mycurser.close()
        
class fil_srh(object):
    
    def __init__(self,ui,data,year,cost,assem,quant):
        self.ui = ui
        self.data = data
        self.year = year 
        self.cost = cost
        self.assem = assem
        self.quant = quant
        
        
    def return_win(self,records):
        
        return_srh = customtkinter.CTkToplevel(self.ui)
        return_srh.title("Search Result")
        return_srh.iconbitmap('f:/masters/semester1/app/project/images/logo.ico')
        # return_srh.geometry("850x200")
        record_fr = customtkinter.CTkFrame(return_srh)
        record_fr.grid(row=0, column=0 ,columnspan=6, padx=5, pady=5)
        
        id_head = customtkinter.CTkLabel(record_fr, text="ID")
        id_name = customtkinter.CTkLabel(record_fr, text="Description")
        id_assem = customtkinter.CTkLabel(record_fr, text="Assembly")
        id_quant = customtkinter.CTkLabel(record_fr, text="Quantity")
        id_cost = customtkinter.CTkLabel(record_fr, text="Cost")
        id_year = customtkinter.CTkLabel(record_fr, text="Year")
        id_head.grid(row=0, column=0)
        id_name.grid(row=0, column=1)
        id_assem.grid(row=0, column=2)
        id_quant.grid(row=0, column=3)
        id_cost.grid(row=0, column=4)
        id_year.grid(row=0, column=5)
        
        i = 0
        for rows in records:
            for j in range(len(rows)):
                e = customtkinter.CTkEntry(record_fr) 
                e.grid(row=i+1, column=j)
                e.insert(END, rows[j])
            i += 1
            
        exit_srh = customtkinter.CTkButton(return_srh, text = "Exit", command = return_srh.destroy)
        exit_srh.grid(row=1, column=2, columnspan=2)
        return_srh.mainloop()
        
    def filter_srh(self):
        try:
            itemdb = mysql.connector.connect(
                host = "localhost",
                database = "app_project",
                user = "root",
                password = "project1234"
            )
            data_local = self.data
            year_local = self.year
            cost_local = self.cost
            assem_local = self.assem
            quant_local = self.quant
            ui = self.ui
            
            
            if cost_local == "" and quant_local == "" and assem_local == "" and year_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemYear" + " <= " + year_local
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
            
            elif cost_local == "" and quant_local == "" and year_local == "" and assem_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemAssem" + " = " + "'" + str(assem_local) + "'"
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
                
            elif year_local == "" and quant_local == "" and assem_local == "" and cost_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".Itemcost" + " <= " + cost_local
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
            
            elif cost_local == "" and year_local == "" and assem_local == "" and quant_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemQuant" + " <= " + quant_local
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
            elif cost_local == "" and quant_local == "" and year_local != "" and assem_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemYear" + " <= " + year_local + " AND " + data_local + ".ItemAssem" + " = " + "'" + str(assem_local) +  "'"
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
            elif quant_local == "" and assem_local == "" and year_local != "" and cost_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemYear" + " <= " + year_local + " AND " + data_local + ".ItemCost" + " <= " + cost_local
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
            elif assem_local == "" and cost_local == "" and year_local != "" and quant_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemYear" + " <= " + year_local + " AND " + data_local + ".ItemQuant" + " <= " + quant_local
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
            elif year_local == "" and quant_local == "" and cost_local != "" and assem_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemAssem" + " = " + "'" + str(assem_local) +  "'" + " AND " + data_local + ".ItemCost" + " <= " + cost_local
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
            elif year_local == "" and cost_local == "" and quant_local != "" and assem_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemAssem" + " = " + "'" + str(assem_local) +  "'" + " AND " + data_local + ".ItemQuant" + " <= " + quant_local
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
            elif year_local == "" and assem_local == "" and cost_local != "" and quant_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemCost" + " <= " +  cost_local + " AND " + data_local + ".ItemQuant" + " <= " + quant_local
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
            elif quant_local == "" and year_local != "" and assem_local != "" and cost_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemYear" + " <= " +  year_local + " AND " + data_local + ".ItemCost" + " <= " + cost_local + " AND " + data_local + ".ItemAssem" + " = " + "'" + str(assem_local) +  "'"
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
            elif cost_local == "" and year_local != "" and assem_local != "" and quant_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemYear" + " <= " +  year_local + " AND " + data_local + ".ItemQuant" + " <= " + quant_local + " AND " + data_local + ".ItemAssem" + " = " + "'" + str(assem_local) +  "'"
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
            elif assem_local == "" and year_local != "" and quant_local != "" and cost_local != "":
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemYear" + " <= " +  year_local + " AND " + data_local + ".ItemQuant" + " <= " + quant_local + " AND " + data_local + ".ItemCost" + " <= "  + cost_local
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
                
            elif cost_local == "" and assem_local == "" and quant_local == "" and year_local == "" and data_local != "":
                
                messagebox.showerror('Error', 'No filters provided! Please enter a filter value!')
                
            else:
                
                sql_slt_query = "select * from " + data_local + " where " + data_local + ".ItemCost" + " <= " +  cost_local + " AND " + data_local + ".ItemQuant" + " <= " + quant_local + " AND " + data_local + ".ItemAssem" + " = " + "'" + str(assem_local) +  "'" + " AND " + data_local + ".ItemYear" + " <= " +  year_local
                mycurser = itemdb.cursor()
                mycurser.execute(sql_slt_query)
                records = mycurser.fetchall()
                if records == []:
                    messagebox.showinfo("Info","No such Record exists!")
                else:
                    self.return_win(records)
            
                
        except mysql.connector.Error as e:
            err_message = messagebox.showerror(title="Error",message=("Error Reading the Table",e))
        
        
        finally:
            
            if itemdb.is_connected():
                itemdb.close()
                mycurser.close()