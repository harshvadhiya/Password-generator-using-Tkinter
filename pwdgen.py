import tkinter as tk
from tkinter import *
from tkinter import font
import random 
import string

class Password_generator:
    def __init__(self,root):
        self.root=root
        self.root.title("Password Generator By Harsh")
        self.root.geometry("700x400")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="#ccbceb") # use ccbcab
        self.logo=PhotoImage(file="images\password.png")
        self.var_genpwd=StringVar()
        
        title=Label(self.root,text="  Password Generator", image=self.logo,compound=LEFT, font=("Bahnschrift",20,"bold"), bg="#032738", fg="#ffffff", anchor="w").place(x=0, y=0, relwidth=2)
        
        lbl=Label(self.root,text="Your Generated Password is: ", font=("Bahnschrift",15,"bold"),bg="#ccbceb", fg="#032738").place(x=10,y=190)
        
        generated_password = Entry(self.root,textvariable=self.var_genpwd, font=("consolas",15,"bold"), state='readonly', bg="black", fg="#032738").place(x=280,y=190,height=30,width=120)
        
        generate=Button(self.root,text="GENERATE",command=self.genratebtn,bd=2,relief=RAISED, font=("Bahnschrift",15,"bold"), bg="#032738", fg="white",cursor="hand2", activebackground="#031e2b", activeforeground="white").place(x=420,y=190, height=30)

        notice = Label(self.root,text="*click again for shuffle",bg="#ccbceb",fg="black").place(x=450,y=220)

    def genratebtn(self):
        lwrCase = string.ascii_lowercase
        uprCase = string.ascii_uppercase
        digits = string.digits
        pun = "$*&/[]{}()%@!?"
        a = lwrCase + uprCase + digits + pun
        ran = random.choice(a) 

        result = ''.join((random.choice(a) for x in range(10))) 
        self.var_genpwd.set(result)

root=tk.Tk()
obj=Password_generator(root)
root.mainloop()
