from tkinter import *
from tkinter import ttk
import random as r
import math as m
import tkinter.messagebox as mb
import mysql.connector as sql
import subprocess


app = Tk()
app.title("SignUp")
app.geometry("400x580")
app.configure(bg="#18484d")
app.resizable(False,False)
img = PhotoImage(file="images//Icon2.png")
app.iconphoto(False,img)

con= sql.connect(host="localhost", user="root", password="bbit@123", database="project2")
cur = con.cursor()
cur.execute("SELECT CUSTOMER_NAME FROM CUSTOMER_DETAILS")
names=[]
for i in cur.fetchall():
    names.append(i[0].upper())

adm = ""

frame = Frame(app,width=400,height=580)
frame.pack()
frame.place(relx=0.5,rely=0.5,anchor=CENTER)
frame.config(bg="#18484d")

label1 = Label(frame,text="SignUp!",font=("Helvetica",25), padx=20,pady=5,bg="#18484d",fg="white")
label1.pack()
label1.place(x=120,y=10)

def on_Name_click(event):
    if NameE.get("1.0","end-1c") == "Enter your name":
        NameE.delete("1.0", "end")
        NameE.config(fg="black")

def on_Name_leave(event):
    if NameE.get("1.0","end-1c") == "":
        NameE.insert("1.0", "Enter your name")
        NameE.config(fg="gray")

Name = Label(frame,text="Name :",bg="#18484d",fg="white",font="bold")
Name.pack()
Name.place(x=75,y=60)
NameE = Text(frame,height = 1,width=30,pady=5,padx=10,borderwidth=2,relief=RIDGE)
NameE.pack(pady = (0,10))
NameE.insert("1.0", "Enter your name")
NameE.bind("<FocusIn>", on_Name_click)
NameE.bind("<FocusOut>", on_Name_leave)
NameE.place(x=76,y=80)

def on_DOA_click(event):
    if DOAE.get("1.0","end-1c") == "DD_MM_YYYY":
        DOAE.delete("1.0", "end")
        DOAE.config(fg="black")

def on_DOA_leave(event):
    if DOAE.get("1.0","end-1c") == "":
        DOAE.insert("1.0", "DD_MM_YYYY")
        DOAE.config(fg="gray")

DOA = Label(frame,text="Date of Account opening :",bg="#18484d",fg="white",font="bold")
DOA.pack()
DOA.place(x=75,y=115)
DOAE = Text(frame,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
DOAE.pack(pady = (0,10))
DOAE.insert("1.0", "DD_MM_YYYY")
DOAE.bind("<FocusIn>", on_DOA_click)
DOAE.bind("<FocusOut>", on_DOA_leave)
DOAE.place(x=75,y=137)

def on_DOB_click(event):
    if DOBE.get("1.0","end-1c") == "DD_MM_YYYY":
        DOBE.delete("1.0", "end")
        DOBE.config(fg="black")

def on_DOB_leave(event):
    if DOBE.get("1.0","end-1c") == "":
        DOBE.insert("1.0", "DD_MM_YYYY")
        DOBE.config(fg="gray")


DOB = Label(frame,text="Date of Birth: ",bg="#18484d",fg="white",font="bold")
DOB.pack()
DOB.place(x=75,y=172)
DOBE = Text(frame,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
DOBE.pack(pady=(0,10))
DOBE.insert("1.0", "DD_MM_YYYY")
DOBE.bind("<FocusIn>", on_DOB_click)
DOBE.bind("<FocusOut>", on_DOB_leave)
DOBE.place(x=75,y=194)

Gen = Label(frame,text="Gender: ",bg="#18484d",fg="white",font="bold")
Gen.pack()
Gen.place(x=75,y=229)
gender=StringVar()
style = ttk.Style()
style.configure("TRadiobutton",foreground="white",font="bold",background="#18484d")
radio_male = ttk.Radiobutton(frame, text="Male", variable=gender, value="MALE")
radio_female = ttk.Radiobutton(frame, text="Female", variable=gender, value="FEMALE")
radio_male.place(x=150 ,y = 229)
radio_female.place(x=225,y=229)

def on_Balance_click(event):
    if BalanceE.get("1.0","end-1c") == "Amount":
        BalanceE.delete("1.0", "end")
        BalanceE.config(fg="black")

def on_Balance_leave(event):
    if BalanceE.get("1.0","end-1c") == "":
        BalanceE.insert("1.0", "Amount")
        BalanceE.config(fg="gray")

Balance = Label(frame,text="Credit Amount: ",bg="#18484d",fg="white",font="bold")
Balance.pack()
Balance.place(x=75,y=257)
BalanceE = Text(frame,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
BalanceE.pack(pady=(0,10))
BalanceE.insert("1.0", "Amount")
BalanceE.bind("<FocusIn>", on_Balance_click)
BalanceE.bind("<FocusOut>", on_Balance_leave)
BalanceE.place(x=75,y=279)

AcTypeL= Label(frame,text="Account Type: ",bg="#18484d",fg="white",font="bold")
AcTypeL.pack()
AcTypeL.place(x=75,y=313)
AcType=StringVar()
style1 = ttk.Style()
style1.configure("TRadiobutton",foreground="white",font="bold",background="#18484d")
radio_savings = ttk.Radiobutton(frame, text="SAVINGS", variable=AcType, value="SAVINGS")
radio_current = ttk.Radiobutton(frame, text="CURRENT", variable=AcType, value="CURRENT")
radio_savings.place(x=100 ,y = 336)
radio_current.place(x=212,y=336)

def on_Password_click(event):
    if PasswordE.get("1.0","end-1c") == "Enter Password":
        PasswordE.delete("1.0", "end")
        PasswordE.config(fg="black")

def on_Password_leave(event):
    if PasswordE.get("1.0","end-1c") == "":
        PasswordE.insert("1.0", "Enter Password")
        PasswordE.config(fg="gray")

Password = Label(frame,text="Password: ",bg="#18484d",fg="white",font="bold")
Password.pack()
Password.place(x=75,y=358)
PasswordE = Text(frame,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
PasswordE.pack(pady=(0,10))
PasswordE.insert("1.0", "Enter Password")
PasswordE.bind("<FocusIn>", on_Password_click)
PasswordE.bind("<FocusOut>", on_Password_leave)
PasswordE.place(x=75,y=378)

def on_ComPassword_click(event):
    if ComPasswordE.get("1.0","end-1c") == "Reenter Password":
        ComPasswordE.delete("1.0", "end")
        ComPasswordE.config(fg="black")

def on_ComPassword_leave(event):
    if ComPasswordE.get("1.0","end-1c") == "":
        ComPasswordE.insert("1.0", "Reenter Password")
        ComPasswordE.config(fg="gray")


ComPassword = Label(frame,text=" Confirm Password: ",bg="#18484d",fg="white",font="bold")
ComPassword.pack()
ComPassword.place(x=75,y=413)
ComPasswordE = Text(frame,height = 1,width=30,pady = 5,padx=10,borderwidth=2,relief=RIDGE)
ComPasswordE.pack(pady=(0,10))
ComPasswordE.insert("1.0", "Reenter Password")
ComPasswordE.bind("<FocusIn>", on_ComPassword_click)
ComPasswordE.bind("<FocusOut>", on_ComPassword_leave)
ComPasswordE.place(x=75,y=433)


def close():
    try:
        app.destroy()
        pgname="python Login_Page.py"
        subprocess.run(pgname,shell=True,check=True)

    except Exception as e:
        print(f"Error:{e}")


def entry(N,DA,DB,B,P,G,AT):
    AC = m.ceil(r.random() * (10 ** 10))
    b = str(m.ceil(r.random() * (10 ** 9)))
    c = r.randint(65, 90)
    ID = b + chr(c)
    BN = "B0"+str(r.randint(0,9))
    tid=str(m.floor((r.random()*(10**12))))
    for i in range (6):
        tid=tid+chr(r.randint(65,90))
    con = sql.connect(host="localhost", user="root", passwd="bbit@123", database="project2")
    cur = con.cursor()
    x="INSERT INTO customer_details (CUSTOMER_ID,CUSTOMER_NAME,DOA,DOB,AC_NO,BALANCE,PASSWORD,GENDER) VALUES('{}','{}','{}','{}','{}',{},'{}','{}')".format(ID,N,DA,DB,AC,B,P,G)
    y="INSERT INTO admin_details (CUSTOMER_ID,B_NO,CREDIT_AMOUNT,DEBIT_AMOUNT,ACCOUNT_TYPE) VALUES('{}','{}',{},{},'{}')".format(ID,BN,B,0,AT)
    z="INSERT INTO transaction (CUSTOMER_ID,TRANSACTION_ID,TYPE,CREDIT_AMT,DEBIT_AMT,2NDCUSTOMER_ID,DATE) VALUES('{}','{}','{}',{},{},'{}','{}')".format(ID,tid,"DEPOSITE",B,"NULL","NULL",DA)
    cur.execute(x)
    cur.execute(y)
    cur.execute(z)
    con.commit()
    if adm.strip() == "from admin page":
        mb.showinfo("Add record"," Successful \nClick Ok to Proceed")
    else:
        mb.showinfo("signup"," Signup Successful \nClick Ok to Proceed")
        close()


def SignUp():
    N = (NameE.get("1.0","end-1c")).strip()
    DA = (DOAE.get("1.0","end-1c")).strip()
    DB = (DOBE.get("1.0","end-1c")).strip()
    try:
        B = float(BalanceE.get("1.0", "end-1c").strip())
    except :
        B="Amount"
    P = (PasswordE.get("1.0","end-1c")).strip()
    CP = (ComPasswordE.get("1.0","end-1c")).strip()
    G = gender.get()
    AT = AcType.get()
    if N != "Enter your name" and N!="":
        NameE.config(highlightbackground="black", highlightthickness=0)
        if DA != "DD_MM_YYYY" and DA!="" :
            DOAE.config(highlightbackground="black", highlightthickness=0)
            if DB != "DD_MM_YYYY" and DB!="" :
                DOBE.config(highlightbackground="black", highlightthickness=0)
                if G != "":
                    Gen.config(highlightbackground="black", highlightthickness=0)
                    if B != "Amount" and B!="":
                        BalanceE.config(highlightbackground="black", highlightthickness=0)
                        if AT != "":
                            AcTypeL.config(highlightbackground="black",highlightthickness=0)
                            if P != "Enter Password" and P!="":
                                PasswordE.config(highlightbackground="black", highlightthickness=0)
                                if CP != "Reenter Password" and P != "":
                                    ComPasswordE.config(highlightbackground="black",highlightthickness=0)
                                    if P == CP:
                                        if N.upper() not in names:
                                            entry(N,DA,DB,B,P,G,AT)
                                        else:
                                            NameE.config(highlightbackground="red", highlightthickness=2)
                                            mb.showerror("Error","Username already exits. You can Log in or change Username")
                                    else:
                                        ComPasswordE.config(highlightbackground="red",highlightthickness=2)
                                        PasswordE.config(highlightbackground="red",highlightthickness=2)
                                        mb.showerror("Error","Password and Confirm password not same")
                                else:
                                    ComPasswordE.config(highlightbackground="red",highlightthickness=2)
                                    mb.showerror("Error","Enter all the required feilds")
                            else:
                                PasswordE.config(highlightbackground="red",highlightthickness=2)
                                mb.showerror("Error","Enter all the required feilds")
                        else:
                            AcTypeL.config(highlightbackground="red",highlightthickness=2)
                            mb.showerror("Error","Enter all the required feilds")
                    else:
                        BalanceE.config(highlightbackground="red", highlightthickness=2)
                        if B == "Amount" and B=="":
                            mb.showerror("Error", "Enter all the required feilds")
                        elif not B.isdigit():
                            mb.showerror("Error", "Amount must be in digits")
                else:
                    Gen.config(highlightbackground="red", highlightthickness=2)
                    mb.showerror("Error", "Enter all the required feilds")
            else:
                DOBE.config(highlightbackground="red", highlightthickness=2)
                mb.showerror("Error", "Enter all the required feilds")
        else:
            DOAE.config(highlightbackground="red", highlightthickness=2)
            mb.showerror("Error", "Enter all the required feilds")
    else:
        NameE.config(highlightbackground="red",highlightthickness=2)
        mb.showerror("Error", "Enter all the required feilds")

buttonsg = Button(frame,text="Sign Up",padx=10,command=SignUp,font=("Arial Rounded MT",16),width=8,pady=4,bg="#57a1f8",fg="white",border=0)
buttonsg.pack(pady=(0,10))
buttonsg.place(x=145,y=478)

buttonLg = Button(frame,text="Go Back to Login",padx=5,command=close,font=("Arial Rounded MT",14),width=18,pady=4,bg="#57a1f8",fg="white",border=0)
buttonLg.pack(pady=(0,10))
buttonLg.place(x=100,y=530)

def Fromadmin():
    global buttonsg,buttonLg,adm,label1
    adm = open("datafile.txt","r").read()
    if adm.strip() == "from admin page":
        buttonsg.config(text = "Add record")
        buttonLg.config(text = "close", command = app.quit)
        app.title("Add record")
        label1.config(text="Add Record")

Fromadmin()
app.mainloop()