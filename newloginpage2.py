from tkinter import *
from PIL import ImageTk, Image
import subprocess
import mysql.connector as sql
import tkinter.messagebox as mb

window = Tk()
window.geometry('750x500')
window.resizable(False,False)
window.title('Login Page')
img = PhotoImage(file="images\\Icon2.png")
window.iconphoto(False,img)

def show():
    hide_button = Button(lgn_frame, image=hide_image, command=hide, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
    hide_button.place(x=676, y=324)
    password_entry.config(show='')

def hide():
    show_button = Button(lgn_frame, image=show_image, command=show, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
    show_button.place(x=676, y=324)
    password_entry.config(show='*')

lgin = "customer"

def switch():
    global lgin

    if lgin == "customer":
        on_button.config(image = on)
        lgin = "admin"
    else:
        on_button.config(image = off)
        lgin = "customer"


    
def validateLogin():
    user = username_entry.get()
    user = (user.upper()).strip()
    passw = password_entry.get()
    con = sql.connect(host="localhost",user="root",password="bbit@123",database="project2")
    cur = con.cursor()
    cur.execute("select CUSTOMER_NAME,PASSWORD from customer_details;")
    data = cur.fetchall()
    if lgin == "customer":
        for i in data:
            if user==i[0].upper() and passw==i[1]:
                mb.showinfo("Login","Login Succesful \nClick Ok to Proceed")
                open("datafile.txt","w").write(user)
                try:
                    window.destroy()
                    pgname = "python details.py"
                    subprocess.run(pgname, shell=True, check=True)

                except Exception as e:
                    print(f"Error:{e}")
                break
        else:
            mb.showerror("Error","Invalid Username or Password")
    elif lgin == "admin":
        if user == "ADMIN" and passw == "adminpass":
            mb.showinfo("Login","Welcome admin \nClick Ok to Proceed")
            try:
                window.destroy()
                open("datafile.txt","w").write(user)
                pgname = "python admin.py"
                subprocess.run(pgname, shell=True, check=True)

            except Exception as e:
                print(f"Error:{e}")
        else:
            mb.showerror("Error","Invalid Admin Login Credentials")

def signup():
    try:
        window.destroy()
        open("datafile.txt","w").write("")
        pgname="python newsignuppage.py"
        subprocess.run(pgname,shell=True,check=True)

    except Exception as e:
        print(f"Error:{e}")

bg_frame = Image.open('images\\background1.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(window, image=photo)
bg_panel.image = photo
bg_panel.pack()

lgn_frame = Frame(window, bg='#040405', width=750, height=500)
lgn_frame.place(x=20, y=0)

# Define Our Images
on = PhotoImage(file = "images\\admin.png")
off = PhotoImage(file="images\\Customer.png")

# Create A Button
on_button = Button(window, image = off, bd = 0,command = switch,bg="#040405")
on_button.place(x=580,y=30,anchor="center")

heading = Label(lgn_frame, text="WELCOME", font=('yu gothic ui', 25, "bold"), bg="#040405", fg='white',bd=5, relief=FLAT)
heading.place(x=50, y=30, width=250, height=30)

side_image = Image.open('images\\vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(lgn_frame, image=photo, bg='#040405')
side_image_label.image = photo
side_image_label.place(x=5, y=60)

sign_in_image = Image.open('images\\hyy.png')
photo = ImageTk.PhotoImage(sign_in_image)
sign_in_image_label = Label(lgn_frame, image=photo, bg='#040405')
sign_in_image_label.image = photo
sign_in_image_label.place(x=480, y=70)

sign_in_label = Label(lgn_frame, text="Log In", bg="#040405", fg="white", font=("yu gothic ui", 17, "bold"))
sign_in_label.place(x=519, y=180)

#Username

username_label = Label(lgn_frame, text="Username", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
username_label.place(x=400, y=220)

username_icon = Image.open('images\\username_icon.png')
photo = ImageTk.PhotoImage(username_icon)
username_icon_label = Label(lgn_frame, image=photo, bg='#040405')
username_icon_label.image = photo
username_icon_label.place(x=400, y=250)

username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
username_entry.place(x=430, y=252, width=270)

username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
username_line.place(x=400, y=276)

#password

password_label = Label(lgn_frame, text="Password", bg="#040405", fg="white", font=("yu gothic ui", 13, "bold"))
password_label.place(x=400, y=290)

password_icon = Image.open('images\\password_icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(lgn_frame, image=photo, bg='#040405')
password_icon_label.image = photo
password_icon_label.place(x=400, y=320)

password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
password_entry.place(x=430, y=322, width=244)

show_image = ImageTk.PhotoImage(file='images\\show.png')
hide_image = ImageTk.PhotoImage(file='images\\hide.png')

show_button = Button(lgn_frame, image=show_image,command=show, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
show_button.place(x=676, y=324)

password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
password_line.place(x=400, y=348)

lgn_button = Image.open('images\\btn1.png')
photo = ImageTk.PhotoImage(lgn_button)
lgn_button_label = Label(lgn_frame, image=photo, bg='#040405')
lgn_button_label.image = photo
lgn_button_label.place(x=400, y=355)
login = Button(lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=validateLogin)
login.place(x=20, y=10)

sign_label = Label(lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"), relief=FLAT, borderwidth=0, background="#040405", fg='white')
sign_label.place(x=400, y=440)
signup_img = ImageTk.PhotoImage(file='images\\register.png')
signup_button_label = Button(lgn_frame, image=signup_img, bg='#98a65d', cursor="hand2", borderwidth=0,background="#040405", activebackground="#040405",command=signup)
signup_button_label.place(x=520, y=435, width=111, height=35)

window.mainloop()