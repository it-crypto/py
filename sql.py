from tkinter import*
import sqlite3


root=Tk()
root.title('DATABASE DEMO')
root.geometry("400x400")

# create a database
conn = sqlite3.connect('product_info.db')

# create cursor whatever have to be done it is done through cursor
c = conn.cursor()

# create table
'''
c.execute("""CREATE TABLE products(
      Customer_Name text,
      product_name text,
      cost real,
      quantity integer,
      order_id integer)
      """)
      '''

# create Submit function
def submit():
    conn = sqlite3.connect('product_info.db')

    # create cursor whatever have to be done it is done through cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO products VALUES(:C_name, :P_name, :cost , :quant, :o_id)",
              {
                  'C_name': C_name.get(),
                  'P_name': P_name.get(),
                  'cost': cost.get(),
                  'quant': quant.get(),
                  'o_id': o_id.get()
              })


    conn.commit()

    # close connection
    conn.close()




    # clear the text boxes
    C_name.delete(0, END)
    P_name.delete(0, END)
    cost.delete(0, END)
    quant.delete(0, END)
    o_id.delete(0, END)

# create show function
def show():
    conn = sqlite3.connect('product_info.db')

    # create cursor whatever have to be done it is done through cursor
    c = conn.cursor()

    # show database records
    c.execute("SELECT *, oid FROM products")
    records = c.fetchall()
    #print(records)

    #loop through results
    print_records = ''
    for record in records:
        #print_records += str(record) + "\n"
        print_records += str(record[1]) + " " + str(record[3]) + "\n"

    show_label = Label(root, text=print_records)
    show_label.grid(row=7, column=0, columnspan=2)



    conn.commit()

    # close connection
    conn.close()






# create text boxes
C_name = Entry(root, width=30)
C_name.grid(row=0, column=1, padx=20)
P_name = Entry(root, width=30)
P_name.grid(row=1, column=1, padx=20)
cost = Entry(root, width=30)
cost.grid(row=2, column=1, padx=20)
quant = Entry(root, width=30)
quant.grid(row=3, column=1, padx=20)
o_id = Entry(root, width=30)
o_id.grid(row=4, column=1, padx=20)

# create text box labels
C_name_label = Label(root, text="Customer_Name")
C_name_label.grid(row=0, column=0)
P_name_label = Label(root, text="Product_Name")
P_name_label.grid(row=1, column=0)
cost_label = Label(root, text="Cost")
cost_label.grid(row=2, column=0)
quant_label = Label(root, text="Quantity")
quant_label.grid(row=3, column=0)
o_id_label = Label(root, text="Purchase_ID")
o_id_label.grid(row=4, column=0)

# create submit Button
submit_btn = Button(root, text="Add record to Databse",command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

show_btn= Button(root, text="Show Records",command=show)
show_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)




# whatever changes are done it is committed
conn.commit()

# close connection
conn.close()



root.mainloop()