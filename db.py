import sqlite3

con = sqlite3.connect('database/database.db')
cur = con.cursor()

#table creation
# cur.execute("CREATE TABLE categories(id_cat,cod_cat,category)")
# cur.execute("CREATE TABLE sub_categories(id_subcat,id_cat,cod_subcat,subcategory)")
# cur.execute("CREATE TABLE matching(id_match,id_cat,id_subcat,string)")
# cur.execute("CREATE TABLE record(id_record,id_cat,id_subcat,date,amount)")

cur.execute('DELETE FROM record')
a = cur.execute('select * from record')
print(a.fetchall())
con.close()