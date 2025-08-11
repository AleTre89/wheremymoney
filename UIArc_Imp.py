import tkinter as tk
from tkinter import ttk
import pandas as pd
import sqlite3

class Archive:
    def __init__(self):
        self.arc_mask = tk.Toplevel()
        self.arc_mask.title("Archive")
        self.arc_mask.geometry("1200x600")

        self.arc_tree = ttk.Treeview(self.arc_mask, columns=(
                                                "Date",
                                                "Amount",
                                                "Description",
                                                "Category",
                                                "Sub-Category"))

        self.arc_tree.column("#0",width=15)
        self.arc_tree.column("Date",width=100)
        self.arc_tree.heading("Date", text="Date")
        self.arc_tree.column("Amount",width=100)
        self.arc_tree.heading("Amount", text="Amount")
        self.arc_tree.column("Description",width=300)
        self.arc_tree.heading("Description", text="Description")
        self.arc_tree.column("Category",width=150)
        self.arc_tree.heading("Category", text="Category")
        self.arc_tree.column("Sub-Category",width=150)
        self.arc_tree.heading("Sub-Category", text="Sub-Category")



        self.description_text= tk.Label(self.arc_mask)


        self.date_lbl = tk.Label(self.arc_mask,text='Date')
        self.amount_lbl = tk.Label(self.arc_mask, text='Amount')
        self.category_lbl = tk.Label(self.arc_mask, text='Category')
        self.subcategory_lbl = tk.Label(self.arc_mask, text='Subcategory')

        self.date_text = tk.Label(self.arc_mask)
        self.amount_text = tk.Label(self.arc_mask)
        self.cat_cbx = ttk.Combobox(self.arc_mask,state='readonly')
        self.subcat_cbx = ttk.Combobox(self.arc_mask, state='readonly')

        self.update_button = tk.Button(self.arc_mask,text='Update', command=self.update_item)
        self.upload_button = tk.Button(self.arc_mask,text='Upload')
        self.cat_match_button = tk.Button(self.arc_mask,text='Category Matching')

        self.arc_tree.grid(row=1,column=0,padx=10,pady=10,rowspan=7)

        self.date_lbl.grid(row=1,column=1,padx=10,pady=10)
        self.date_text.grid(row=1, column=2, padx=10, pady=10)
        self.amount_lbl.grid(row=2, column=1, padx=10, pady=10)
        self.amount_text.grid(row=2, column=2, padx=10, pady=10)
        self.category_lbl.grid(row=3, column=1, padx=10, pady=10)
        self.cat_cbx.grid(row=3, column=2, padx=10, pady=10)
        self.subcategory_lbl.grid(row=4, column=1, padx=10, pady=10)
        self.subcat_cbx.grid(row=4, column=2, padx=10, pady=10)

        self.update_button.grid(row=5, column=2, padx=10, pady=10)
        self.upload_button.grid(row=6, column=2, padx=10, pady=10)
        self.cat_match_button.grid(row=7, column=2, padx=10, pady=10)

        self.description_text.grid(row=8,column=0,padx=10,pady=10)


        self.arc_tree.bind('<ButtonRelease-1>',self.get_descr)
        self.cat_cbx.bind('<<ComboboxSelected>>',self.get_subcat)

        self.getdata()
        self.cbx_filling()

        self.arc_mask.mainloop()

    def update_item(self):
        #TODO if cbx emtpy error
        cat_value = self.cat_cbx.get()
        subcat_value = self.subcat_cbx.get()


        item=self.arc_tree.selection()[0]
        date = self.arc_tree.item(item)['values'][0]
        amount = self.arc_tree.item(item)['values'][1]
        description = self.arc_tree.item(item)['values'][2]

        self.arc_tree.item(item, values=(date,amount,description,cat_value,subcat_value))




    def get_descr(self,event):
        desc_text = self.arc_tree.selection()[0]
        description = self.arc_tree.item(desc_text)['values']
        self.description_text.config(text=description[2],wraplength='500')

        self.date_text.config(text=description[0])
        self.amount_text.config(text=description[1])

    def cbx_filling(self):
        con = sqlite3.connect('database/database.db')
        cur = con.cursor()
        category_list = [cat[0] for cat in cur.execute("SELECT category FROM categories").fetchall()]
        self.cat_cbx.config(values=category_list)

    def get_subcat(self,event):
        self.subcat_cbx.set('')
        cat_selected =self.cat_cbx.get()
        con = sqlite3.connect('database/database.db')
        cur = con.cursor()
        selected_cat_list = cur.execute("SELECT categories.category, sub_categories.subcategory "
             "FROM categories "
             "LEFT JOIN sub_categories ON categories.id_cat=sub_categories.id_cat "
                                        "WHERE categories.category=?", (cat_selected,)).fetchall()
        subcat_list = [subcat[1] for subcat in selected_cat_list]

        if subcat_list[0] != None:
            self.subcat_cbx.config(values=subcat_list)
        else:
            self.subcat_cbx.config(values=[''])

        con.close()

    # DATA CONTABILE
    # DATA VALUTA
    # CAUSALE
    # DESCRIZIONE OPERAZIONE
    # IMPORTO IN EURO
    def getdata(self):
        df = pd.read_excel("./estratti/elenco.xlsx")
        df_dict = df.to_dict(orient="dict")

        tot_rec =len(df_dict["CAUSALE"])

        count = 0
        for rec in range(0,tot_rec):
            con = sqlite3.connect("database/database.db")
            cur = con.cursor()

            string_list = cur.execute("SELECT c.category,s.subcategory,m.string "
                           "FROM matching AS m "
                           "LEFT JOIN categories AS c ON c.id_cat = m.id_cat "
                           "LEFT JOIN sub_categories AS s ON s.id_subcat = m.id_subcat").fetchall()
            string_to_search = df_dict["DESCRIZIONE OPERAZIONE"][rec].upper()

            for element in string_list:
                if string_to_search.find(element[2]) >=0:
                    cat_subcat_match = [element[0],element[1]]
                else:
                    cat_subcat_match = ['','']


            self.arc_tree.insert('',index="end",iid=count,values=(
                df_dict["DATA CONTABILE"][rec],
                df_dict["IMPORTO IN EURO"][rec],
                df_dict["DESCRIZIONE OPERAZIONE"][rec],
                cat_subcat_match[0],
                cat_subcat_match[1]
            ))
            count+=1