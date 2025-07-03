import tkinter as tk
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

#TODO if cbx is empty error message - approvation before adding category
#TODO cancel table column cod_cat
    def add_category(self):
        """Add data from categories combobox to db tabel categories """
        con = sqlite3.connect('database/database.db')
        cur = con.cursor()

        id_cat = cur.execute("SELECT MAX(id_cat) FROM categories").fetchone()[0]
        if id_cat == None:
            id_cat = 0
        else:
            id_cat+=1

        cod_cat = f"{self.cat_cbx.get()}_{id_cat}"

        category=self.cat_cbx.get()


        cur.execute("INSERT INTO categories VALUES (?,?,?)", (id_cat,cod_cat,category))
        con.commit()
        con.close()

