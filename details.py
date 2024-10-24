from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as sql
import tkinter.messagebox as mb
import subprocess


d = open("datafile.txt","r").read()
con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
cur = con.cursor()
cur.execute("select CUSTOMER_NAME from customer_details")
data1 = cur.fetchall()
for i in data1:
    if d == i[0].upper():
        d = i[0]
        break

cur.execute("select * from customer_details natural join admin_details where CUSTOMER_NAME = '{}'".format(d))
data2 = list(cur.fetchone())
open("datafile.txt","w").write(d)
app = Tk()
app.title("Details")
app.geometry("320x550")
app.configure(bg="#2c2c2c")
app.resizable(False,False)
img = PhotoImage(file="images//Icon2.png")
app.iconphoto(False,img)

img = PhotoImage(file="images//Icon2.png")
label_width = 25
label_height = 25
width_factor = label_width / img.width()
height_factor = label_height / img.height()
rescale_factor = min(width_factor, height_factor)
resized_image = img.subsample(int(1 / rescale_factor), int(1 / rescale_factor))

logo = Label(app,image=resized_image)
logo.place(x=1,y=8)
bnl = Label(app, text="Heritage Finance Bank", font=("Algerian", 18),bg="#2c2c2c",fg="white")
bnl.place(x=30,y=1)
bnlcl = Label(app, text="Preserving Your Financial Legacy", font=("Helvetica", 10),bg="#2c2c2c",fg="white")
bnlcl.place(x=33,y=25)

col="#66ed9a"
def create_rounded_rectangle(canvas , x1 , y1 , x2 , y2 , radius):

    canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, fill=col,outline=col)
    canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, fill=col,outline=col)
    canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, fill=col,outline=col)
    canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, fill=col,outline=col)
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=col,outline=col)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=col,outline=col)

canvas = Canvas(app, width=300, height=125,background="#2c2c2c",highlightthickness=0)
canvas.place(x=10,y=55)


create_rounded_rectangle(canvas, 0, 0, 300, 125, 25)
fnt="Arial Rounded MT Bold"

balance = Label(canvas,text = "Balance :",font=(fnt, 25),bg=col)
balance.place(x=25,y=2)

INR = Label(canvas,text = "INR   :",font=(fnt, 20),bg=col)
INR.place(x=25,y=40)

#money2 = Label(canvas)
money=Label(canvas,text = "************",font=(fnt, 20),bg=col,width=11)
money.place(x=105,y=42)

def hideMoney():
    money.config(text="************")
    shbutton.config(text="View Balance",command=showMoney)

def showMoney():
    money.config(text=data2[5])
    shbutton.config(text="Hide Balance",command=hideMoney)

shb = Image.open('images\\hbt1.png')
photo = ImageTk.PhotoImage(shb)
shb_label = Label(canvas, image=photo, bg=col)
shb_label.image = photo
shb_label.place(x=130,y=70)
shbutton = Button(shb_label,text="View Balance",width=13,pady=5,bg='#3047ff',activebackground='#3047ff',fg="white",border=0,command=showMoney,font=("Calibri",12))
shbutton.place(x=12,y=5)

Bframe=Frame(app,width=280,height=300)
Bframe.place(x=10,y=185)

canvasscroll=Canvas(Bframe,bg="red",width=280,height=300)
canvasscroll.pack(side="left",fill="both")

frame=Frame(canvasscroll,bg="#2c2c2c")
scrollbar = ttk.Scrollbar(Bframe,orient="vertical",command=canvasscroll.yview)
scrollbar.pack(side="right",fill=Y)

canvasscroll.config(yscrollcommand=scrollbar.set)
canvasscroll.create_window((0,0),window=frame,anchor="nw")
canvasscroll.bind("<Configure>", lambda event, canvas=canvasscroll: canvasscroll.configure(scrollregion=canvasscroll.bbox("y")))
def update_canvas(event):
    canvasscroll.config(scrollregion=canvasscroll.bbox("all"))

canvasscroll.bind("<Configure>", update_canvas)
def on_mousewheel(event):
    try:
        canvasscroll.yview_scroll(-1*(event.delta//120), "units")
    except Exception as e:
        pass

canvasscroll.bind("<Configure>", update_canvas)
app.bind("<MouseWheel>", on_mousewheel)

Label(frame,text = "Other Details:",font=(fnt, 20),bg="#2c2c2c",fg="white").pack(anchor="w")

Label(frame,text = "Account Number:",font=(fnt, 10),fg="white",bg="#2c2c2c").pack(anchor="w")
Label(frame,text=data2[4],font=(fnt, 12),fg="white",bg="#2c2c2c").pack(anchor="w")
canvas1=Canvas(frame,width=295,height=3,highlightthickness=0)
canvas1.pack(anchor="w")
canvas1.create_line(0,2,295,2)

Label(frame,text = "Account Holder Name:",font=(fnt, 10),fg="white",bg="#2c2c2c").pack(anchor="w")
Label(frame,text=data2[1].title(),font=(fnt, 12),fg="white",bg="#2c2c2c").pack(anchor="w")
canvas2=Canvas(frame,width=295,height=3,highlightthickness=0)
canvas2.pack(anchor="w")
canvas2.create_line(0,2,295,2)

Label(frame,text = "Customer ID:",font=(fnt, 10),fg="white",bg="#2c2c2c").pack(anchor="w")
Label(frame,text=data2[0],font=(fnt, 12),fg="white",bg="#2c2c2c").pack(anchor="w")
canvas3=Canvas(frame,width=295,height=3,highlightthickness=0)
canvas3.pack(anchor="w")
canvas3.create_line(0,2,295,2)

Label(frame,text = "Date of Account Opening:",font=(fnt, 10),fg="white",bg="#2c2c2c").pack(anchor="w")
Label(frame,text=data2[2],font=(fnt, 12),fg="white",bg="#2c2c2c").pack(anchor="w")
canvas3=Canvas(frame,width=295,height=3,highlightthickness=0)
canvas3.pack(anchor="w")
canvas3.create_line(0,2,295,2)

Label(frame,text = "Account Type:",font=(fnt, 10),fg="white",bg="#2c2c2c").pack(anchor="w")
Label(frame,text=data2[-1],font=(fnt, 12),fg="white",bg="#2c2c2c").pack(anchor="w")
canvas4=Canvas(frame,width=295,height=3,highlightthickness=0)
canvas4.pack(anchor="w")
canvas4.create_line(0,2,295,2)

Label(frame,text = "Branch Code:",font=(fnt, 10),fg="white",bg="#2c2c2c").pack(anchor="w")
Label(frame,text=data2[8],font=(fnt, 12),fg="white",bg="#2c2c2c").pack(anchor="w")
canvas5=Canvas(frame,width=295,height=3,highlightthickness=0)
canvas5.pack(anchor="w")
canvas5.create_line(0,2,295,2)

Label(frame,text = "Date of Birth:",font=(fnt, 10),fg="white",bg="#2c2c2c").pack(anchor="w")
Label(frame,text=data2[3],font=(fnt, 12),fg="white",bg="#2c2c2c").pack(anchor="w")
canvas6=Canvas(frame,width=295,height=3,highlightthickness=0)
canvas6.pack(anchor="w")
canvas6.create_line(0,2,295,2)

Label(frame,text = "Gender:",font=(fnt, 10),fg="white",bg="#2c2c2c").pack(anchor="w")
Label(frame,text=(data2[7]).upper(),font=(fnt, 12),fg="white",bg="#2c2c2c").pack(anchor="w")
canvas7=Canvas(frame,width=295,height=3,highlightthickness=0)
canvas7.pack(anchor="w")
canvas7.create_line(0,2,295,2)

def changepass():
    app2=Tk()
    app2.title("Change Password")
    app2.geometry("300x110")
    app2.resizable(False,False)

    Label(app2,text="Old password :").grid(row=0,column=0)
    old = Entry(app2)
    old.grid(row=0,column=1)
    Label(app2,text="New password :").grid(row=1,column=0)
    new = Entry(app2)
    new.grid(row=1,column=1)
    Label(app2,text="Confirm password :").grid(row=2,column=0)
    new2 = Entry(app2)
    new2.grid(row=2,column=1)

    def checkpass():
        x=old.get()
        y=new.get()
        z=new2.get()
        if x == data2[6]:
            if y == z:
                con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
                cur = con.cursor()
                cur.execute("UPDATE customer_details SET PASSWORD = '{}' WHERE CUSTOMER_ID = '{}'".format(y,data2[0]))
                con.commit()
                mb.showinfo("Successful","Password updated successfully")
                app2.destroy()
            else:
                mb.showerror("Error","Password and Confirm Password not same")
        else:
            mb.showerror("Error","Incorrect Old Password")

    Button(app2,text="change password",width=15,pady=4,bg="#57a1f8",fg="white",border=0,command=checkpass,font=("Calibri",11)).place(x=60,y=70)


    app2.mainloop()


Label(frame,text = "Password:",font=(fnt, 10),fg="white",bg="#2c2c2c").pack(anchor="w")
Label(frame,text="*******",font=(fnt, 12),fg="white",bg="#2c2c2c").pack(anchor="w")
Button(frame,text="Change Password",width=15,pady=5,bg='#3047ff',activebackground='#3047ff',fg="white",border=0,command=changepass,font=("Calibri",12)).pack(anchor="w",padx=5)
canvas6=Canvas(frame,width=295,height=3,highlightthickness=0)
canvas6.pack(anchor="w")
canvas6.create_line(0,2,295,2)

def Logout():
    try:
        app.destroy()
        open("datafile.txt","w").write("")
        pgname="python newloginpage2.py"
        subprocess.run(pgname,shell=True,check=True)

    except Exception as e:
        print(f"Error:{e}")

lgout_button = Image.open('images\\btn2.png')
photo = ImageTk.PhotoImage(lgout_button)
lgout_button_label = Label(frame, image=photo, bg='#040405')
lgout_button_label.image = photo
lgout_button_label.pack(anchor="w",pady=5)
logout = Button(lgout_button_label, text='LOG OUT', font=("yu gothic ui", 13, "bold"), width=23, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=Logout)
logout.place(x=20, y=10)


def transaction():
    try:
        app.destroy()
        pgname="python Transaction.py"
        subprocess.run(pgname,shell=True,check=True)

    except Exception as e:
        print(f"Error:{e}")

t_button = Image.open('images\\Tbtn1.png')
photo = ImageTk.PhotoImage(t_button)
t_button_label = Label(app, image=photo, bg='#040405')
t_button_label.image = photo
t_button_label.place(x=5,y=490)
button=Button(t_button_label,text="Go to transactions",width=29,pady=6,font=(fnt,11),bg=col,fg="black",activebackground=col,border=0,command=transaction)
button.place(x=20,y=10)

app.mainloop()