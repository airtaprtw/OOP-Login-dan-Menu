from tkinter import *
from tkinter import messagebox
import os

def login():
    user=username.get()
    code=password.get()

    if user=="Parvat" and code=="1234":
        root=Toplevel(screen)
        root.title("Bill")
        root.geometry("1280x720+150+80")
        root.configure(bg="#d7dae2")
        root.resizable(False, False)

        #copy and pasta ur code
        def Reset():
            entry_sandwich.delete(0, END)
            entry_cookies.delete(0, END)
            entry_Tea.delete(0, END)
            entry_coffee.delete(0, END)
            entry_juice.delete(0, END)
            entry_pancakes.delete(0, END)
            entry_pastery.delete(0, END)
        
        def Total():
            try: a1=int(sandwich.get())
            except: a1=0

            try: a2=int(cookies.get())
            except: a2=0

            try: a3=int(Tea.get())
            except: a3=0

            try: a4=int(coffee.get())
            except: a4=0

            try: a5=int(juice.get())
            except: a5=0

            try: a6=int(pancakes.get())
            except: a6=0

            try: a7=int(pastery.get())
            except: a7=0

            #define cost of each item per quantity
            c1=60*a1
            c2=30*a2
            c3=7*a3
            c4=100*a4
            c5=20*a5
            c6=15*a6
            c7=7*a7

            lbl_total=Label(f2, font=('aria', 20, 'bold'), text="Total", width=22, fg="lightyellow", bg="black")
            lbl_total.place(x=0,y=50)
            entry_total=Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_bill, bd=6, width=14, bg="lightgreen")
            entry_total.place(x=80,y=100)

            totalcost=c1+c2+c3+c4+c5+c6+c7
            string_bill="Rs.", str('%.2f' %totalcost)
            Total_bill.set(string_bill)

        Label(text="BILL MANAGEMENT", bg="black", fg="white", font=("calibri",33), width="300", height="4").pack()

        #MENU CARD
        f=Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=370, height=400)
        f.place(x=30, y=250)

        Label(f, text="Menu", font=("Gabriola", 40, "bold"), fg="black", bg="lightgreen").place(x=100,y=0)

        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="sandwich.......Rs.60/plate", fg="black", bg="lightgreen").place(x=10,y=80)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="cookies.......Rs.30/plate", fg="black", bg="lightgreen").place(x=10,y=110)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Tea.......Rs70/cup", fg="black", bg="lightgreen").place(x=10,y=140)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Coffee.......Rs.100/cup", fg="black", bg="lightgreen").place(x=10,y=170)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Juice.......Rs.100/glass", fg="black", bg="lightgreen").place(x=10,y=200)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Pancakes.......Rs.15/pack", fg="black", bg="lightgreen").place(x=10,y=230)
        Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Pastery.......Rs.25/pastery", fg="black", bg="lightgreen").place(x=10,y=260)

        #BILL
        f2=Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=370, height=400)
        f2.place(x=880, y=250)

        Bill=Label(f2, text="Bill", font=('calibri', 20), bg="lightyellow")
        Bill.place(x=160,y=10)

        #ENTRY WORK
        f1=Frame(root, bd=5, height=400, width=450, relief=RAISED)
        f1.pack(pady=30)
        sandwich=StringVar()
        cookies=StringVar()
        Tea=StringVar()
        coffee=StringVar()
        juice=StringVar()
        pancakes=StringVar()
        pastery=StringVar()
        Total_bill=StringVar()

        #LABEL
        lbl_sandwich=Label(f1, font=("aria", 20, 'bold'), text="sandwich", width=12, fg="blue4")
        lbl_cookies=Label(f1, font=("aria", 20, 'bold'), text="cookies", width=12, fg="blue4")
        lbl_Tea=Label(f1, font=("aria", 20, 'bold'), text="Tea", width=12, fg="blue4")
        lbl_coffee=Label(f1, font=("aria", 20, 'bold'), text="Coffee", width=12, fg="blue4")
        lbl_juice=Label(f1, font=("aria", 20, 'bold'), text="Juice", width=12, fg="blue4")
        lbl_pancakes=Label(f1, font=("aria", 20, 'bold'), text="Pancakes", width=12, fg="blue4")
        lbl_pastery=Label(f1, font=("aria", 20, 'bold'), text="Pastery", width=12, fg="blue4")

        lbl_sandwich.grid(row=1, column=0)
        lbl_cookies.grid(row=2, column=0)
        lbl_Tea.grid(row=3, column=0)
        lbl_coffee.grid(row=4, column=0)
        lbl_juice.grid(row=5, column=0)
        lbl_pancakes.grid(row=6, column=0)
        lbl_pastery.grid(row=7, column=0)

        #ENTRY
        entry_sandwich=Entry(f1, font=("aria", 20, 'bold'), textvariable=sandwich, bd=6, width=8, bg="lightpink")
        entry_cookies=Entry(f1, font=("aria", 20, 'bold'), textvariable=cookies, bd=6, width=8, bg="lightpink")
        entry_Tea=Entry(f1, font=("aria", 20, 'bold'), textvariable=Tea, bd=6, width=8, bg="lightpink")
        entry_coffee=Entry(f1, font=("aria", 20, 'bold'), textvariable=coffee, bd=6, width=8, bg="lightpink")
        entry_juice=Entry(f1, font=("aria", 20, 'bold'), textvariable=juice, bd=6, width=8, bg="lightpink")
        entry_pancakes=Entry(f1, font=("aria", 20, 'bold'), textvariable=pancakes, bd=6, width=8, bg="lightpink")
        entry_pastery=Entry(f1, font=("aria", 20, 'bold'), textvariable=pastery, bd=6, width=8, bg="lightpink")

        entry_sandwich.grid(row=1, column=1)
        entry_cookies.grid(row=2, column=1)
        entry_Tea.grid(row=3, column=1)
        entry_coffee.grid(row=4, column=1)
        entry_juice.grid(row=5, column=1)
        entry_pancakes.grid(row=6, column=1)
        entry_pastery.grid(row=7, column=1)

        #BUTTONS
        btn_reset=Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Reset", command=Reset)
        btn_reset.grid(row=8, column=0)

        btn_total=Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Reset", command=Total)
        btn_total.grid(row=8, column=1)

        #end of code
    
    #all alerts, when someone try to enter wrong uname and password

    elif user=="" and code=="":
        messagebox.showerror("Invalid", "Please enter username and password")

    elif user=="":
        messagebox.showerror("Invalid", "Username is required")
    
    elif code=="":
        messagebox.showerror("Invalid", "The password field is required")
    
    elif user!="Parvat" and code!="1234":
        messagebox.showerror("Invalid", "Invalid username and password")
    
    elif user!="Parvat":
        messagebox.showerror("Invalid", "Please enter a valid username")
    
    elif user!="1234":
        messagebox.showerror("Invalid", "Please enter a valid password")

from tkinter import Tk, Label, Entry, Frame, Button, StringVar, END
def main_screen():

    global screen
    global username
    global password

    screen=Tk()
    screen.geometry("1280x720+150+80")
    screen.configure(bg="#d7dae2")

    #icon
    image_icon=PhotoImage(file="login.png")
    screen.iconphoto(False, image_icon)
    screen.title("Login System")

    lbl_Title=Label(text="Login System", font=("arial", 50, 'bold'), fg="black", bg="#d7dae2")
    bordercolor=Frame(screen, bg="black", width=800, height=400)
    bordercolor.pack()

    mainframe=Frame(bordercolor, bg="#d7dae2", width=800, height=400)
    mainframe.pack(padx=20, pady=20)

    Label(mainframe, text="Username", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(mainframe, text="Password", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)
    
    username=StringVar()
    password=StringVar()

    entry_username=Entry(mainframe, textvariable=username, width=12, bd=12, font=("arial", 30))
    entry_username.place(x=400, y=50)
    entry_password=Entry(mainframe, textvariable=password, width=12, bd=2, font=("arial", 30))
    entry_password.place(x=400, y=150)

    def Reset():
        entry_username.delete(0, END)
        entry_password.delete(0, END)


    Button(mainframe, text="Login", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=login).place(x=100, y=250)
    Button(mainframe, text="Reset", height="2", width=23, bg="#1089ff", fg="white", bd=0, command=Reset).place(x=300, y=250)
    Button(mainframe, text="Exit", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=screen.destroy).place(x=500, y=250)

    screen.mainloop() 
main_screen()