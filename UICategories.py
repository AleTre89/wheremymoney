import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3

class Categories:
    def __init__(self):
        self.cat_mask = tk.Toplevel()
        self.cat_mask.title("Categories")
        self.cat_mask.geometry("400x600")

        #labels
        self.cat_label= tk.Label(self.cat_mask, text="Category")
        self.subcat_label = tk.Label(self.cat_mask, text="Subcategory")

        #combobox
        self.cat_cbx= ttk.Combobox(self.cat_mask)
        self.subcat_cbx = ttk.Combobox(self.cat_mask)

        #buttons
        self.cat_button = tk.Button(self.cat_mask,text="Add Category",width=15,command=self.add_category)
        self.subcat_button = tk.Button(self.cat_mask,text="Add SubCategory",width=15)

        #positioning
        self.cat_label.grid(row=0, column=0, padx=10, pady=10)
        self.cat_cbx.grid(row=0, column=1, padx=10, pady=10)
        self.cat_button.grid(row=0, column=2, padx=10, pady=10)

        self.subcat_label.grid(row=1, column=0, padx=10, pady=10)
        self.subcat_cbx.grid(row=1, column=1, padx=10, pady=10)
        self.subcat_button.grid(row=1, column=2, padx=10, pady=10)

        self.cat_tree = ttk.Treeview(self.cat_mask)
        self.cat_tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


        self.cat_mask.mainloop()

#TODO create column active - True by default
#TODO create gestione button to activate / deactivate categories
    def add_category(self):
        """Add data from categories combobox to db table categories"""
        con = sqlite3.connect('database/database.db')
        cur = con.cursor()

        id_cat = cur.execute("SELECT MAX(id_cat) FROM categories").fetchone()[0]
        if id_cat == None:
            id_cat = 0
        else:
            id_cat+=1
        category=self.cat_cbx.get()

        category_list= [cat[0] for cat in cur.execute("SELECT category FROM categories").fetchall()]

        if category == "":
            error_no_record = messagebox.showerror("Error: No category digited",
                                                   "You didn't insert new category.\n"
                                                           "Digit category in combobox.")
        elif category in category_list:
            error_already_exixst = messagebox.showerror("Error: Category already exists",
                                                        "Category already exists")
        else:
            want_to_insert = messagebox.askokcancel("insert new category?",
                                   f"Do you want to insert the category: {category}?",)
            if want_to_insert:
                cur.execute("INSERT INTO categories VALUES (?,?)", (id_cat,category))
                con.commit()
                con.close()

