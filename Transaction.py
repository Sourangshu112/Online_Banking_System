from tkinter import *
import mysql.connector as sql
import tkinter.messagebox as mb
from PIL import Image,ImageTk
from tkinter import ttk
import math,random
import datetime
import subprocess

ct=datetime.datetime.now()
date=str(ct.day)+"_"+str(ct.month)+"_"+str(ct.year)

app = Tk()
app.title("Transactions")
app.geometry("700x420")
app.configure(bg="#040405")
app.resizable(False,False)
img = PhotoImage(file="images//Icon2.png")
app.iconphoto(False,img)

frame = Frame(app,width=800,height=230,bg="#040405")
frame.pack()

frame2 = Frame(app,width=800,height=300,bg="#f2edd5")
frame2.pack()
Label(frame2,text="Last Transaction >>>",font=("yu gothic ui", 13, "bold"),bg="#f2edd5").place(x=5,y=5)

col="lightgrey"
def create_rounded_rectangle(canvas , x1 , y1 , x2 , y2 , radius):

    canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, fill=col,outline=col)
    canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, fill=col,outline=col)
    canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, fill=col,outline=col)
    canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, fill=col,outline=col)
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=col,outline=col)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=col,outline=col)

canvas1 = Canvas(frame2, width=300, height=125,background="#f2edd5",highlightthickness=0)
canvas1.place(x=10,y=35)
create_rounded_rectangle(canvas1, 0, 0, 300, 125, 25)

HeadL = Label()
IdL = Label()
AmtL = Label()
DateL = Label()
AccL = Label()

def sendH():
    global HeadL,IdL,AmtL,DateL,AccL
    HeadL.destroy()
    IdL.destroy()
    AmtL.destroy()
    DateL.destroy()
    AccL.destroy()
    HeadL=Label(canvas1,text = f"Money: {data2[2]}",font=("Helvetica",15),bg=col)
    HeadL.place(x=10,y=5)
    canvas2=Canvas(canvas1,width=295,height=3,highlightthickness=0,bg=col)
    canvas2.place(x=3,y=30)
    canvas2.create_line(0,2,295,2)
    IdL=Label(canvas1,text = f"Id: {data2[1]}",font=("Helvetica",12),bg=col)
    IdL.place(x=10,y=36)
    AmtL=Label(canvas1,text = f"Amount: {data2[4]}",font=("Helvetica",12),bg=col)
    AmtL.place(x=10,y=60)
    DateL=Label(canvas1,text = f"Date: {data2[-1]}",font=("Helvetica",12),bg=col)
    DateL.place(x=150,y=60)
    AccL = Label(canvas1,text = f"To:   *******{data2[5][-4:]}",font=("Helvetica",12),bg=col)
    AccL.place(x=10,y=85)

def receivedH():
    global HeadL,IdL,AmtL,DateL,AccL
    HeadL.destroy()
    IdL.destroy()
    AmtL.destroy()
    DateL.destroy()
    AccL.destroy()
    HeadL=Label(canvas1,text = f"Money: {data2[2]}",font=("Helvetica",15),bg=col)
    HeadL.place(x=10,y=5)
    canvas2=Canvas(canvas1,width=295,height=3,highlightthickness=0,bg=col)
    canvas2.place(x=3,y=30)
    canvas2.create_line(0,2,295,2)
    IdL=Label(canvas1,text = f"Id: {data2[1]}",font=("Helvetica",12),bg=col)
    IdL.place(x=10,y=36)
    AmtL=Label(canvas1,text = f"Amount: {data2[3]}",font=("Helvetica",12),bg=col)
    AmtL.place(x=10,y=60)
    DateL=Label(canvas1,text = f"Date: {data2[-1]}",font=("Helvetica",12),bg=col)
    DateL.place(x=150,y=60)
    AccL = Label(canvas1,text = f"From:   *******{data2[5][-4:]}",font=("Helvetica",12),bg=col)
    AccL.place(x=10,y=85)

def withdrawH():
    global HeadL,IdL,AmtL,DateL,AccL
    HeadL.destroy()
    IdL.destroy()
    AmtL.destroy()
    DateL.destroy()
    AccL.destroy()
    HeadL=Label(canvas1,text = f"Money: {data2[2]}",font=("Helvetica",15),bg=col)
    HeadL.place(x=10,y=5)
    canvas2=Canvas(canvas1,width=295,height=3,highlightthickness=0,bg=col)
    canvas2.place(x=3,y=30)
    canvas2.create_line(0,2,295,2)
    IdL=Label(canvas1,text = f"Id: {data2[1]}",font=("Helvetica",12),bg=col)
    IdL.place(x=10,y=36)
    AmtL=Label(canvas1,text = f"Amount: {data2[4]}",font=("Helvetica",12),bg=col)
    AmtL.place(x=10,y=60)
    DateL=Label(canvas1,text = f"Date: {data2[-1]}",font=("Helvetica",12),bg=col)
    DateL.place(x=150,y=60)

def depositeH():
    global HeadL,IdL,AmtL,DateL,AccL
    HeadL.destroy()
    IdL.destroy()
    AmtL.destroy()
    DateL.destroy()
    AccL.destroy()
    HeadL=Label(canvas1,text = f"Money: {data2[2]}",font=("Helvetica",15),bg=col)
    HeadL.place(x=10,y=5)
    canvas2=Canvas(canvas1,width=295,height=3,highlightthickness=0,bg=col)
    canvas2.place(x=3,y=30)
    canvas2.create_line(0,2,295,2)
    IdL=Label(canvas1,text = f"Id: {data2[1]}",font=("Helvetica",12),bg=col)
    IdL.place(x=10,y=36)
    AmtL=Label(canvas1,text = f"Amount: {data2[3]}",font=("Helvetica",12),bg=col)
    AmtL.place(x=10,y=60)
    DateL=Label(canvas1,text = f"Date: {data2[-1]}",font=("Helvetica",12),bg=col)
    DateL.place(x=150,y=60)


def typeCheck():
    if data2[2] == "SENT":
        sendH()
    elif data2[2] == "RECEIVED":
        receivedH()
    elif data2[2] == "WITHDRAW":
        withdrawH()
    elif data2[2] == "DEPOSITE":
        depositeH()

data = []
data2 = []
def Data():
    d = open("datafile.txt","r").read()
    con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
    cur = con.cursor()
    cur.execute("select * from customer_details natural join admin_details where CUSTOMER_NAME = '{}'".format(d))
    global data,data2
    data = list(cur.fetchone())
    cur.execute("select * from transaction where CUSTOMER_ID = '{}'".format(data[0]))
    data2 = cur.fetchall()[-1]
    con.commit()
    typeCheck()

Data()


Label(frame,text=f"Hi, {data[1]}".title(),font=("Helvetica",25,"bold"),bg="#040405",fg="white").place(x=15,y=15)

def TrasactionId():
    a=str(math.floor((random.random()*(10**12))))
    x=""
    for i in range (6):
        x=x+chr(random.randint(65,90))
    return(a+x)


def withdraw():
    app2 = Tk()
    app2.title("Withdraw money")
    app2.geometry("400x200")
    app2.config(bg="#040405")
    app2.resizable(False,False)
    Label(app2,text="Enter Amount ",bg="#040405",fg="white",font=("bold",14)).place(x=20,y=20)
    amt = Text(app2,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
    amt.place(x=20,y=50)
    Label(app2,text="Enter Password ",bg="#040405",fg="white",font=("bold",14)).place(x=20,y=85)
    Pass = Text(app2,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
    Pass.place(x=20,y=115)

    def verify():
        try:
            A = float(amt.get("1.0", "end-1c").strip())
        except :
            A="Amount"
        P = (Pass.get("1.0", "end-1c")).strip()
        if A != "" and A !="Amount":
            amt.config(highlightbackground="red", highlightthickness=0)
            if P == data[6]:
                Pass.config(highlightbackground="red",highlightthickness=0)
                if A < data[5]:
                    con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
                    cur = con.cursor()
                    rb = data[5]-A
                    cur.execute("UPDATE customer_details set BALANCE = {} WHERE CUSTOMER_ID = '{}'".format(rb,data[0]))
                    cur.execute("SELECT DEBIT_AMOUNT FROM admin_details WHERE CUSTOMER_ID ='{}'".format(data[0]))
                    d2=cur.fetchone()[0]
                    d2=d2+A
                    cur.execute("UPDATE admin_details set DEBIT_AMOUNT = {} WHERE CUSTOMER_ID = '{}'".format(d2,data[0]))
                    tid = TrasactionId()
                    cur.execute("INSERT INTO transaction (CUSTOMER_ID,TRANSACTION_ID,TYPE,CREDIT_AMT,DEBIT_AMT,2NDCUSTOMER_ID,DATE) VALUES('{}','{}','{}',{},{},'{}','{}')".format(data[0],tid,"WITHDRAW","NULL",A,"NULL",date))
                    con.commit()
                    mb.showinfo("Withdraw","Successful \nClick Ok to proceed")
                    app2.destroy()
                    Data()
                else:
                    amt.config(highlightbackground="red", highlightthickness=2)
                    mb.showerror("Error","Insufficient Balance!")
            else:
                Pass.config(highlightbackground="red",highlightthickness=2)
                mb.showerror("Error","Incorrect Password")
        else:
            amt.config(highlightbackground="red", highlightthickness=2)
            mb.showerror("Error", "Empty or Invalid Amount Fiels")


    Button(app2,text="Ok",width=10,pady=3,border=0,bg="#3047ff",fg="white", activebackground='#3047ff',font=("yu gothic ui", 13, "bold"),command=verify).place(x=90,y=155)



def deposite():
    app2 = Tk()
    app2.title("Deposite money")
    app2.geometry("400x200")
    app2.config(bg="#040405")
    app2.resizable(False,False)
    Label(app2,text="Enter Amount ",bg="#040405",fg="white",font=("bold",14)).place(x=20,y=20)
    amt = Text(app2,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
    amt.place(x=20,y=50)
    Label(app2,text="Enter Password ",bg="#040405",fg="white",font=("bold",14)).place(x=20,y=85)
    Pass = Text(app2,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
    Pass.place(x=20,y=115)
    def verify():
        try:
            A = float(amt.get("1.0", "end-1c").strip())
        except :
            A="Amount"
        P = (Pass.get("1.0", "end-1c")).strip()
        if A != "" and A !="Amount":
            amt.config(highlightbackground="red", highlightthickness=0)
            if P == data[6]:
                Pass.config(highlightbackground="red",highlightthickness=0)
                con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
                cur = con.cursor()
                rb = data[5]+A
                cur.execute("UPDATE customer_details set BALANCE = {} WHERE CUSTOMER_ID = '{}'".format(rb,data[0]))
                cur.execute("SELECT CREDIT_AMOUNT FROM admin_details WHERE CUSTOMER_ID ='{}'".format(data[0]))
                d2=cur.fetchone()[0]
                d2=d2+A
                cur.execute("UPDATE admin_details set CREDIT_AMOUNT = {} WHERE CUSTOMER_ID = '{}'".format(d2,data[0]))
                tid = TrasactionId()
                cur.execute("INSERT INTO transaction (CUSTOMER_ID,TRANSACTION_ID,TYPE,CREDIT_AMT,DEBIT_AMT,2NDCUSTOMER_ID,DATE) VALUES('{}','{}','{}',{},{},'{}','{}')".format(data[0],tid,"DEPOSITE",A,"NULL","NULL",date))
                con.commit()
                mb.showinfo("Deposite","Successful \nClick Ok to proceed")
                app2.destroy()
                Data()
            else:
                Pass.config(highlightbackground="red",highlightthickness=2)
                mb.showerror("Error","Incorrect Password")
        else:
            amt.config(highlightbackground="red", highlightthickness=2)
            mb.showerror("Error", "Empty or Invalid Amount Fiels")
            
    Button(app2,text="Ok",width=10,pady=3,border=0,bg="#3047ff",fg="white", activebackground='#3047ff',font=("yu gothic ui", 13, "bold"),command=verify).place(x=90,y=155)


def sendmoney():
    app2 = Tk()
    app2.title("Transfer money")
    app2.geometry("400x325")
    app2.config(bg="#040405")
    app2.resizable(False,False)

    Label(app2,text="Enter Amount ",bg="#040405",fg="white",font=("bold",14)).place(x=20,y=20)
    amt = Text(app2,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
    amt.place(x=20,y=50)

    Label(app2,text="Beneficiary name: ",bg="#040405",fg="white",font=("bold",14)).place(x=20,y=85)
    BName = Text(app2,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
    BName.place(x=20,y=115)

    Label(app2,text="Beneficiary Account number: ",bg="#040405",fg="white",font=("bold",14)).place(x=20,y=150)
    BAcNo = Text(app2,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
    BAcNo.place(x=20,y=180)

    Label(app2,text="Enter Password ",bg="#040405",fg="white",font=("bold",14)).place(x=20,y=215)
    Pass = Text(app2,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
    Pass.place(x=20,y=245)

    con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
    cur = con.cursor()
    cur.execute("select CUSTOMER_NAME,AC_NO from customer_details")
    info = cur.fetchall()
    con.commit()
    name =[]
    Acno = []
    for i in info:
        name.append((i[0]).upper())
        Acno.append(int(i[1]))

    def verify():
        try:
            A = float(amt.get("1.0", "end-1c").strip())
        except :
            A="Amount"
        P = (Pass.get("1.0", "end-1c")).strip()
        BN = (BName.get("1.0","end-1c")).strip()
        try:
            Ac = float(BAcNo.get("1.0", "end-1c").strip())
        except:
            Ac = "Account"

        if A!= "Amount":
            amt.config(highlightbackground="red",highlightthickness=0)
            if (BN).upper() in name:
                BName.config(highlightbackground="red",highlightthickness=0)
                if Ac in Acno:
                    BAcNo.config(highlightbackground="red",highlightthickness=0)
                    if P == data[6]:
                        Pass.config(highlightbackground="red",highlightthickness=0)
                        if A < data[5]:
                            c=name.index((BN).upper())
                            if Acno[c] == Ac:
                                con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
                                cur = con.cursor()
                                rb=data[5]-A
                                cur.execute("UPDATE customer_details set BALANCE = {} WHERE CUSTOMER_ID = '{}'".format(rb,data[0]))
                                cur.execute("SELECT CUSTOMER_ID,BALANCE FROM customer_details WHERE AC_NO = '{}'".format(int(Ac)))
                                md=cur.fetchone()
                                rb=md[1]+A
                                cur.execute("UPDATE customer_details set BALANCE = {} where AC_NO = '{}'".format(rb,int(Ac)))
                                cur.execute("select CREDIT_AMOUNT from admin_details where CUSTOMER_ID = '{}'".format(md[0]))
                                rb=cur.fetchone()[0]+A
                                cur.execute("UPDATE admin_details set CREDIT_AMOUNT = {} WHERE CUSTOMER_ID = '{}'".format(rb,md[0]))
                                cur.execute("SELECT DEBIT_AMOUNT FROM admin_details WHERE CUSTOMER_ID ='{}'".format(data[0]))
                                rb=cur.fetchone()[0]+A
                                cur.execute("UPDATE admin_details set DEBIT_AMOUNT = {} WHERE CUSTOMER_ID = '{}'".format(rb,data[0]))
                                tid=TrasactionId()
                                cur.execute("INSERT INTO transaction (CUSTOMER_ID,TRANSACTION_ID,TYPE,CREDIT_AMT,DEBIT_AMT,2NDCUSTOMER_ID,DATE) VALUES('{}','{}','{}',{},{},'{}','{}')".format(data[0],tid,"SENT","NULL",A,md[0],date))
                                cur.execute("INSERT INTO transaction (CUSTOMER_ID,TRANSACTION_ID,TYPE,CREDIT_AMT,DEBIT_AMT,2NDCUSTOMER_ID,DATE) VALUES('{}','{}','{}',{},{},'{}','{}')".format(md[0],tid,"RECEIVED",A,"NULL",data[0],date))
                                con.commit()
                                mb.showinfo("Send Money","Successful \nClick Ok to proceed")
                                app2.destroy()
                                Data()
                            else:
                                BAcNo.config(highlightbackground="red",highlightthickness=2)
                                BName.config(highlightbackground="red",highlightthickness=2)
                                mb.showerror("Error","Account Number and Beneficiar name does not match")

                        else:
                            amt.config(highlightbackground="red",highlightthickness=2)
                            mb.showerror("Error","Insufficient Balance!")
                    else:
                        Pass.config(highlightbackground="red",highlightthickness=2)
                        mb.showerror("Error","Incorrect Password")
                else:
                    BAcNo.config(highlightbackground="red",highlightthickness=2)
                    mb.showerror("Error","Incorrect Account Number")
            else:
                BName.config(highlightbackground="red",highlightthickness=2)
                mb.showerror("Error","Incorrect Beneficiary Name")
        else:
            amt.config(highlightbackground="red",highlightthickness=2)
            mb.showerror("Error","Invalid or Empty Amount")


    Button(app2,text="Ok",width=10,pady=3,border=0,bg="#3047ff",fg="white", activebackground='#3047ff',font=("yu gothic ui", 13, "bold"),command=verify).place(x=90,y=285)


def Back():
    try:
        app.destroy()
        pgname = "python details.py"
        subprocess.run(pgname, shell=True, check=True)

    except Exception as e:
        print(f"Error:{e}")

buttonimg = Image.open('images\\btn1.png')
photo = ImageTk.PhotoImage(buttonimg)

withdraw_button_label = Label(frame, image=photo, bg='#040405')
withdraw_button_label.image = photo
withdraw_button_label.place(x=15,y=60)
withdrawbutton = Button(withdraw_button_label,text="Withdraw money",width=25,pady=3,bg="#3047ff",fg="white", activebackground='#3047ff',border=0,font=("yu gothic ui", 13, "bold"),command=withdraw)
withdrawbutton.place(x=20, y=10)


deposite_button_label = Label(frame, image=photo, bg='#040405')
deposite_button_label.image = photo
deposite_button_label.place(x=15,y=125)
depositebutton = Button(deposite_button_label,text="Deposite money",width=25,pady=3,bg="#3047ff",fg="white", activebackground='#3047ff',border=0,font=("yu gothic ui", 13, "bold"),command=deposite)
depositebutton.place(x=20, y=10)


send_button_label = Label(frame, image=photo, bg='#040405')
send_button_label.image = photo
send_button_label.place(x=350,y=60)
sendbutton = Button(send_button_label,text="Send money",width=25,pady=3,bg="#3047ff",fg="white", activebackground='#3047ff',border=0,font=("yu gothic ui", 13, "bold"),command=sendmoney)
sendbutton.place(x=20, y=10)


Back_button_label = Label(frame, image=photo, bg='#040405')
Back_button_label.image = photo
Back_button_label.place(x=350,y=125)
Backbutton = Button(Back_button_label,text="Go back to details",width=25,pady=3,bg="#3047ff",fg="white", activebackground='#3047ff',border=0,font=("yu gothic ui", 13, "bold"),command=Back)
Backbutton.place(x=20, y=10)

typeCheck()

def history():
    app2 = Tk()
    app2.geometry("625x300")
    app2.title("Transaztion History")
    app2.resizable(False,False)
    columns = [
        'Customer ID', 'TransactionId', "Type",
        "Amount Credited", "Ammount Debited", "2ndCustomerId", "Date",]
    tree = ttk.Treeview(app2, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col,anchor=CENTER)
        tree.column(col, width=89)

    con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
    cur = con.cursor()
    cur.execute("select * from transaction where CUSTOMER_ID = '{}'".format(data[0]))
    data3 = cur.fetchall()
    con.commit()

    for row_data in data3:
        tree.insert('', 'end', values=row_data)

    scrollbar = ttk.Scrollbar(app2, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side="left", fill="both", expand=True,padx=2,pady=2)
    scrollbar.pack(side="right", fill="y")

history_button_label = Label(frame2, image=photo, bg='#f2edd5')
history_button_label.image = photo
history_button_label.place(x=350,y=30)
historybutton = Button(history_button_label,text="View all transactions",width=25,pady=3,bg="#3047ff",fg="white", activebackground='#3047ff',font=("yu gothic ui", 13, "bold"),border=0,command=history)
historybutton.place(x=20, y=10)


app.mainloop()