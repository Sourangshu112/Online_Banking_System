from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image
import subprocess
import mysql.connector as sql
import tkinter.messagebox as mb
import datetime
import math as m
import random as r

ct=datetime.datetime.now()
date=str(ct.day)+"_"+str(ct.month)+"_"+str(ct.year)

window = Tk()
window.geometry('750x540')
window.resizable(False,False)
window.title('SignUp Page')
img = PhotoImage(file="images//Icon2.png")
window.iconphoto(False,img)

bg_frame = Image.open('images\\background1.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(window, image=photo)
bg_panel.image = photo
bg_panel.pack()

lgn_frame = Frame(window, bg='#040405', width=750, height=540)
lgn_frame.place(x=20, y=0)

heading = Label(lgn_frame, text="CREATE A NEW ACCOUNT", font=('yu gothic ui', 20, "bold"), bg="#040405", fg='white',bd=5, relief=FLAT)
heading.place(x=40, y=30, width=320, height=30)

side_image = Image.open('images\\vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(lgn_frame, image=photo, bg='#040405')
side_image_label.image = photo
side_image_label.place(x=5, y=80)

sign_in_image = Image.open('images\\hyy.png')
photo = ImageTk.PhotoImage(sign_in_image)
sign_in_image_label = Label(lgn_frame, image=photo, bg='#040405')
sign_in_image_label.image = photo
sign_in_image_label.place(x=480, y=70)

frame1 = Frame(lgn_frame,bg="#040405",width=315,height=230)
frame1.place(x=400,y=180)
a=""
name,dob,gen,bal,acty,pas,cpas="","","",0,"","",""

step_icon = Image.open('images\\1.png')
photo = ImageTk.PhotoImage(step_icon)
step_label = Label(lgn_frame, image=photo, bg='#040405')
step_label.image = photo
step_label.place(x=400, y=10)

def callnext():
    if a == "personal":
        account()
    elif a == "account":
        authenticate()
    elif a == "authenticate":
        pass

def callprev():
    if a == "authenticate":
        account()
    elif a == "account":
        personal()
    elif a == "personal":
        pass


def close():
    try:
        window.destroy()
        pgname="python newloginpage2.py"
        subprocess.run(pgname,shell=True,check=True)

    except Exception as e:
        print(f"Error:{e}")


def personal():
    global name,dob,gen,bal,acty,pas,cpas
    global frame1,a,prevbutton_label,step_label
    step_label.destroy()
    step_icon = Image.open('images\\1.png')
    photo = ImageTk.PhotoImage(step_icon)
    step_label = Label(lgn_frame, image=photo, bg='#040405')
    step_label.image = photo
    step_label.place(x=400, y=10)
    a="personal"
    frame1.destroy()
    prevbutton_label.destroy()
    frame1 = Frame(lgn_frame,bg="#040405",width=315,height=230)
    frame1.place(x=400,y=180)
    sign_in_label = Label(frame1, text="Personal Details", bg="#040405", fg="white", font=("yu gothic ui", 17, "bold"))
    sign_in_label.place(x=75, y=0)
    username_label = Label(frame1, text="Username", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
    username_label.place(x=0, y=40)
    username_icon = Image.open('images\\username_icon.png')
    photo = ImageTk.PhotoImage(username_icon)
    username_icon_label = Label(frame1, image=photo, bg='#040405')
    username_icon_label.image = photo
    username_icon_label.place(x=0, y=70)
    username_entry = Entry(frame1, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
    username_entry.place(x=30, y=72, width=270)
    username_line = Canvas(frame1, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    username_line.place(x=0, y=96)

    Dob_label = Label(frame1, text="Date of Birth", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
    Dob_label.place(x=0, y=110)
    Dob_icon = Image.open('images\\calander.png')
    photo = ImageTk.PhotoImage(Dob_icon)
    Dob_icon_label = Label(frame1, image=photo, bg='#040405')
    Dob_icon_label.image = photo
    Dob_icon_label.place(x=0, y=140)
    date=StringVar()
    Dob_entry =  DateEntry(frame1,date_pattern="dd_mm_yyyy",textvariable=date)
    Dob_entry.place(x=30, y=142)
    Dob_line = Canvas(frame1, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    Dob_line.place(x=0, y=166)

    Gen_label = Label(frame1, text="Gender :", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
    Gen_label.place(x=0, y=180)
    gender=StringVar()
    style = ttk.Style()
    style.configure("TRadiobutton",foreground="white",font=("yu gothic ui", 13, "bold"),background="#040405")
    radio_male = ttk.Radiobutton(frame1, text="Male", variable=gender, value="MALE")
    radio_female = ttk.Radiobutton(frame1, text="Female", variable=gender, value="FEMALE")
    radio_male.place(x=80 ,y = 180)
    radio_female.place(x=160,y=180)

    if name != "" and dob != "" and gen != "":
        username_entry.insert("end",name)
        def update_date():
            current_date = dob  # Get the current date in dd_mm_yyyy format
            date.set(current_date)
            window.after(1000, update_date)
        update_date()
        gender.set(gen.upper())
    
    def check():
        global name,dob,gen,bal,acty,pas,cpas
        name=username_entry.get()
        dob=Dob_entry.get()
        #print(dob)
        gen=gender.get()
        if name == "" or dob =="" or gen == "":
            mb.showerror("Error","Enter all the required feilds")
        else:
            callnext()
    
    next.config(text="NEXT",command=check)
    


def account():
    global name,dob,gen,bal,acty,pas,cpas
    global frame1,a,prevbutton_label,step_label
    step_label.destroy()
    step_icon = Image.open('images\\2.png')
    photo = ImageTk.PhotoImage(step_icon)
    step_label = Label(lgn_frame, image=photo, bg='#040405')
    step_label.image = photo
    step_label.place(x=400, y=10)
    a = "account"
    frame1.destroy()
    prevbutton_label.destroy()
    frame1 = Frame(lgn_frame,bg="#040405",width=315,height=230)
    frame1.place(x=400,y=180)

    account_label = Label(frame1, text="Account Details", bg="#040405", fg="white", font=("yu gothic ui", 17, "bold"))
    account_label.place(x=75, y=0)

    amount_label = Label(frame1, text="Credit amount", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
    amount_label.place(x=0, y=40)
    amount_icon = Image.open('images\\rupee.png')
    photo = ImageTk.PhotoImage(amount_icon)
    amount_icon_label = Label(frame1, image=photo, bg='#040405')
    amount_icon_label.image = photo
    amount_icon_label.place(x=0, y=70)
    amount_entry = Entry(frame1, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
    amount_entry.place(x=30, y=72, width=270)

    amount_line = Canvas(frame1, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    amount_line.place(x=0, y=96)

    Account_label = Label(frame1, text="Account Type :", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
    Account_label.place(x=0, y=120)

    AcType=StringVar()
    style = ttk.Style()
    style.configure("TRadiobutton",foreground="white",font=("yu gothic ui", 13, "bold"),background="#040405")
    radio_savings = ttk.Radiobutton(frame1, text="SAVINGS", variable=AcType, value="SAVINGS")
    radio_current = ttk.Radiobutton(frame1, text="CURRENT", variable=AcType, value="CURRENT")
    radio_savings.place(x=50 ,y =150)
    radio_current.place(x=170,y=150)

    if bal != "" and acty != "":
        amount_entry.insert("end",bal)
        AcType.set(acty.upper())

    def check():
        global name,dob,gen,bal,acty,pas,cpas
        try:
            x = amount_entry.get()
            if x == "":
                bal= x
            else:
                bal = float(x)
            acty = AcType.get() 
            if bal == "" or acty == "":
                mb.showerror("Error","Enter all the required feilds")
            else:
                callnext()

        except :
            bal=""
            mb.showerror("Error","Amount must be in digit")

    next.config(text="NEXT",command=check)

    prevbutton = Image.open('images\\prev.png')
    photo = ImageTk.PhotoImage(prevbutton)
    prevbutton_label = Label(lgn_frame, image=photo, bg='#040405')
    prevbutton_label.image = photo
    prevbutton_label.place(x=400, y=415)
    back = Button(prevbutton_label, text='BACK', font=("yu gothic ui", 13, "bold"), width=9, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=callprev)
    back.place(x=40, y=10)



def entry(N,DB,G,B,AT,P):
    global step_label,date
    DA=date
    step_label.destroy()
    step_icon = Image.open('images\\4.png')
    photo = ImageTk.PhotoImage(step_icon)
    step_label = Label(lgn_frame, image=photo, bg='#040405')
    step_label.image = photo
    step_label.place(x=400, y=10)
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
    x="INSERT INTO customer_details (CUSTOMER_ID,CUSTOMER_NAME,DOA,DOB,AC_NO,BALANCE,PASSWORD,GENDER) VALUES('{}','{}','{}','{}','{}',{},'{}','{}')".format(ID,N.upper(),DA,DB,AC,B,P,G)
    y="INSERT INTO admin_details (CUSTOMER_ID,B_NO,CREDIT_AMOUNT,DEBIT_AMOUNT,ACCOUNT_TYPE) VALUES('{}','{}',{},{},'{}')".format(ID,BN,B,0,AT)
    z="INSERT INTO transaction (CUSTOMER_ID,TRANSACTION_ID,TYPE,CREDIT_AMT,DEBIT_AMT,2NDCUSTOMER_ID,DATE) VALUES('{}','{}','{}',{},{},'{}','{}')".format(ID,tid,"DEPOSITE",B,"NULL","NULL",DA)
    cur.execute(x)
    cur.execute(y)
    cur.execute(z)
    con.commit()
    mb.showinfo("signup"," Signup Successful \nClick Ok to Proceed")
    close()


def authenticate():
    global name,dob,gen,bal,acty,pas,cpas
    global frame1,a,prevbutton_label,step_label
    step_label.destroy()
    step_icon = Image.open('images\\3.png')
    photo = ImageTk.PhotoImage(step_icon)
    step_label = Label(lgn_frame, image=photo, bg='#040405')
    step_label.image = photo
    step_label.place(x=400, y=10)
    a = "authenticate"
    frame1.destroy()
    prevbutton_label.destroy()
    frame1 = Frame(lgn_frame,bg="#040405",width=315,height=230)
    frame1.place(x=400,y=180)
    account_label = Label(frame1, text="Authentication", bg="#040405", fg="white", font=("yu gothic ui", 17, "bold"))
    account_label.place(x=75, y=0)

    password_label = Label(frame1, text="Password", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
    password_label.place(x=0, y=40)
    password_icon = Image.open('images\\password_icon.png')
    photo = ImageTk.PhotoImage(password_icon)
    password_icon_label = Label(frame1, image=photo, bg='#040405')
    password_icon_label.image = photo
    password_icon_label.place(x=0, y=70)
    password_entry = Entry(frame1, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
    password_entry.place(x=30, y=72, width=270)
    password_line = Canvas(frame1, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    password_line.place(x=0, y=96)

    Cpassword_label = Label(frame1, text="Cofirm Password", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
    Cpassword_label.place(x=0, y=110)
    Cpassword_icon = Image.open('images\\password_icon.png')
    photo = ImageTk.PhotoImage(Cpassword_icon)
    Cpassword_icon_label = Label(frame1, image=photo, bg='#040405')
    Cpassword_icon_label.image = photo
    Cpassword_icon_label.place(x=0, y=140)
    Cpassword_entry = Entry(frame1, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
    Cpassword_entry.place(x=30, y=142, width=270)
    Cpassword_line = Canvas(frame1, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    Cpassword_line.place(x=0, y=166)

    if pas != "" and cpas != "":
        password_entry.insert("end",pas)
        Cpassword_entry.insert("end",cpas)

    def check():
        global name,dob,gen,bal,acty,pas,cpas
        pas = password_entry.get()
        cpas = Cpassword_entry.get()
        if pas == "" or cpas == "":
            mb.showerror("Error","Enter all the required feilds")
        else:
            if pas == cpas:
                entry(name,dob,gen,bal,acty,pas)
            else:
                mb.showerror("Error","Pasword and Confirm password not same")
    next.config(text="Sign Up",command=check)

    prevbutton = Image.open('images\\prev.png')
    photo = ImageTk.PhotoImage(prevbutton)
    prevbutton_label = Label(lgn_frame, image=photo, bg='#040405')
    prevbutton_label.image = photo
    prevbutton_label.place(x=400, y=415)
    back = Button(prevbutton_label, text='BACK', font=("yu gothic ui", 13, "bold"), width=9, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=callprev)
    back.place(x=40, y=10)




nextbutton = Image.open('images\\next.png')
photo = ImageTk.PhotoImage(nextbutton)
nextbutton_label = Label(lgn_frame, image=photo, bg='#040405')
nextbutton_label.image = photo
nextbutton_label.place(x=550, y=415)
next = Button(nextbutton_label, text='NEXT', font=("yu gothic ui", 13, "bold"), width=9, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=callnext)
next.place(x=20, y=10)

prevbutton = Image.open('images\\prev.png')
photo = ImageTk.PhotoImage(prevbutton)
prevbutton_label = Label(lgn_frame, image=photo, bg='#040405')
prevbutton_label.image = photo
prevbutton_label.place(x=400, y=415)
back = Button(prevbutton_label, text='BACK', font=("yu gothic ui", 13, "bold"), width=9, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=callprev)
back.place(x=40, y=10)

personal()

sign_label = Label(lgn_frame, text='Already have a account', font=("yu gothic ui", 11, "bold"), relief=FLAT, borderwidth=0, background="#040405", fg='white')
sign_label.place(x=400, y=490)
signup_img = ImageTk.PhotoImage(file='images\\login.png')
signup_button_label = Button(lgn_frame, image=signup_img, bg='#98a65d', borderwidth=0,background="#040405", activebackground="#040405",command=close)
signup_button_label.place(x=570, y=485, width=111, height=35)

window.mainloop()