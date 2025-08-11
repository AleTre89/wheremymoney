import sqlite3

con = sqlite3.connect('database/database.db')
cur = con.cursor()

#table creation
# cur.execute("CREATE TABLE categories(id_cat,cod_cat,category)")
# cur.execute("CREATE TABLE sub_categories(id_subcat,id_cat,cod_subcat,subcategory)")
# cur.execute("CREATE TABLE matching(id_match,id_cat,id_subcat,string)")
# cur.execute("CREATE TABLE record(id_record,id_cat,id_subcat,date,amount)")

a=cur.execute('SELECT categories.category, sub_categories.subcategory '
             'FROM categories '
             'LEFT JOIN sub_categories ON categories.id_cat=sub_categories.id_cat')

print(a.fetchall())
con.commit()
con.close()