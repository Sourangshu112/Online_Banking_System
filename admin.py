from tkinter import *
from tkinter import ttk
import mysql.connector as sql
import subprocess


window = Tk()
window.title("Admin Control Panel")
window.geometry("995x500")
window.resizable(False,False)
img = PhotoImage(file="images//Icon2.png")
window.iconphoto(False,img)
def Back():
    try:
        window.destroy()
        open("datafile.txt","w").write("")
        pgname="python newloginpage2.py"
        subprocess.run(pgname,shell=True,check=True)

    except Exception as e:
        print(f"Error:{e}")

Cframe = Frame(window,width=995,height=35,bg="lightgrey")
Cframe.pack()
Head = Label()
tree = Label()
scrollbar = Label()
add = Label()
remove = Label()
goback = Button(Cframe,text = "<<< Go Back",command=Back,padx=10,pady=3)
goback.place(x=850,y=2)




def customer():
    global Head,tree,scrollbar,add,remove
    Head.destroy()
    tree.destroy()
    scrollbar.destroy()
    add.destroy()
    remove.destroy()

    def add():
        open("datafile.txt","w").write("from admin page")
        try:
            pgname="python signup.py"
            subprocess.run(pgname,shell=True,check=True)
            customer()

        except Exception as e:
            print(f"Error:{e}")

    def remove():
        sdata = tree.selection()
        if sdata:
            item_values = tree.item(sdata[0], 'values')
            con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
            cur = con.cursor()
            cur.execute("DELETE FROM customer_details WHERE CUSTOMER_ID ='{}'".format(item_values[0]))
            cur.execute("DELETE FROM admin_details WHERE CUSTOMER_ID ='{}'".format(item_values[0]))
            con.commit()
            customer()


    add = Button(Cframe,text="Add record",padx=10,pady=3, command=add)
    add.place(x=250,y=2)
    remove = Button(Cframe,text="Remove record",padx=10,pady=3,command=remove)
    remove.place(x=375,y=2)
    Head = Label(window,text="Customer Records :",font=("Helvetica",14))
    Head.pack()
    columns = [
        'Customer ID', "Name", "Date of Acc Opening", "Account No",
        "Balance", "Account Type", "Total Credit", "Total Debit",
        "Branch No.", "Gender", "Date of Birth"]
    tree = ttk.Treeview(window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col,anchor=CENTER)
        tree.column(col, width=89)

    con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
    cur = con.cursor()
    cur.execute("select CUSTOMER_ID,CUSTOMER_NAME,DOA,AC_NO,BALANCE,ACCOUNT_TYPE,CREDIT_AMOUNT,DEBIT_AMOUNT,B_NO,GENDER,DOB from customer_details natural join admin_details")
    data = cur.fetchall()
    con.commit()

    for row_data in data:
        tree.insert('', 'end', values=row_data)

    scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side="left", fill="both", expand=True,padx=2,pady=2)
    scrollbar.pack(side="right", fill="y")

def Transaction():
    global Head,tree,scrollbar,add,remove
    Head.destroy()
    tree.destroy()
    scrollbar.destroy()
    add.destroy()
    remove.destroy()
    Head = Label(window,text="Transaction Record :",font=("Helvetica",14))
    Head.pack()
    columns = [
        'Customer ID', 'TransactionId', "Type",
        "Amount Credited", "Ammount Debited", "2ndCustomerId", "Date",]
    tree = ttk.Treeview(window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col,anchor=CENTER)
        tree.column(col, width=89)

    con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
    cur = con.cursor()
    cur.execute("select * from transaction")
    data = cur.fetchall()
    con.commit()

    for row_data in data:
        tree.insert('', 'end', values=row_data)

    scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side="left", fill="both", expand=True,padx=2,pady=2)
    scrollbar.pack(side="right", fill="y")

def checkTable(a,b,c):
    x=table.get()
    if x == 'Customer Details':
        customer()
    elif x == 'Transactions':
        Transaction()


Label(Cframe,text="Table",font=("Helvetica",14),bg="lightgrey").place(x=10,y=2)
table = StringVar()
table.set("Customer Details")
OptionMenu(Cframe, table, 'Customer Details', "Transactions").place(x=70, y=2, width=150)
table.trace("w",checkTable)



customer()
window.mainloop()
