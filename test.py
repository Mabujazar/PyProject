from tkinter import *
from tkinter import messagebox

def Signup():
    username = txtSignUsername.get()
    password = txtSignPassword.get()

    myfile = open("username.txt", "a")
    myfile.write(username)
    myfile.write(",")
    myfile.write(password)
    myfile.write("\n")

    messagebox.showinfo("Welcome!", "Account created successfully!")
    Libsign.destroy()

def login():
    username = txtUsername.get()
    password = txtPassword.get()

    myfile = open("username.txt", "r")
    alldata = myfile.readlines()

    for x in alldata:
        linedata = x.strip().split(",")
        if username == linedata[0] and password == linedata[1]:
            lbl3.config(text="Welcome")
            Library2 = Tk()
            Library2.geometry("500x400")
            Library.destroy()

            def btn12():
                messagebox.showinfo("The Books : ", "-Rich Dad Poor Dad \n-The Millionaire Next Door \n-The Richest Man in BabylonYour\n-Money or Your Life\n-The Total Money Makeover")
            def btn22():
                messagebox.showinfo("The Books : ", "-Into the Wild\n-Eat, Pray, Love\n-The Alchemist\n-A Walk in the Woods\n-In a Sunburned Country")
            def btn32():
                messagebox.showinfo("The Books : ", "-A Sand County Almanac\n-Braiding Sweetgrass\n-The Hidden Life of Trees\n-Pilgrim at Tinker Creek\n-The Sixth Extinction")
            def btn42():
                messagebox.showinfo("The Books : ", "-Clean Code\n-The Pragmatic Programmer\n-Effective Java\n-JavaScript: The Good Parts\n-Design Patterns")
            def btn52():
                messagebox.showinfo("The Books : ", "-This Changes Everything\n-The Hidden Life of Trees\n-The Uninhabitable Earth\n-Earth: An Intimate History")

            Library2.title("Books")
            btn12 = Button(Library2, text="Wealth and Financial Success", bg="#fcf5e7", fg="black", command=btn12)
            btn22 = Button(Library2, text="Traveling", bg="#fcf5e7", fg="black", command=btn22)
            btn32 = Button(Library2, text="Nature", bg="#fcf5e7", fg="black", command=btn32)
            btn42 = Button(Library2, text="Programming", bg="#fcf5e7", fg="black", command=btn42)
            btn52 = Button(Library2, text="Earth", bg="#fcf5e7", fg="black", command=btn52)

            btn12.pack()
            btn22.pack()
            btn32.pack()
            btn42.pack()
            btn52.pack()

Libsign = Tk()
Libsign.geometry("300x200")

lblSign1 = Label(Libsign, text="Username")
txtSignUsername = Entry(Libsign)

lblSign2 = Label(Libsign, text="Password")
txtSignPassword = Entry(Libsign, show="*")

btnSignUp = Button(Libsign, text="Sign Up", command=Signup)

lblSign1.pack()
txtSignUsername.pack()
lblSign2.pack()
txtSignPassword.pack()
btnSignUp.pack()

Library = Tk()
Library.geometry("500x400")
frame1 = Frame(Library)
frame2 = Frame(Library)

lbl1 = Label(frame1, text="Username")
txtUsername = Entry(frame1)

lbl2 = Label(frame2, text="Password")
txtPassword = Entry(frame2, show="*")

btnLogin = Button(Library, text="Login", command=login)
lbl3 = Label(Library, text="Welcome to The Library")

txtUsername.pack()
txtPassword.pack()

lbl1.pack()
lbl2.pack()
lbl3.pack()

frame1.pack()
frame2.pack()

btnLogin.pack()

Libsign.mainloop()
