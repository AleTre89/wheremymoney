import tkinter as tk
from tkinter import ttk
import pandas as pd

class Archive:
    def __init__(self):
        self.arc_mask = tk.Toplevel()
        self.arc_mask.title("Archive")
        self.arc_mask.geometry("1000x600")

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

        self.arc_tree.grid(row=0,column=0,padx=10,pady=10)

        self.getdata()

        self.arc_mask.mainloop()

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

            self.arc_tree.insert('',index="end",iid=count,values=(
                df_dict["DATA CONTABILE"][rec],
                df_dict["IMPORTO IN EURO"][rec],
                df_dict["DESCRIZIONE OPERAZIONE"][rec],
                "",
                ""
            ))
            count+=1