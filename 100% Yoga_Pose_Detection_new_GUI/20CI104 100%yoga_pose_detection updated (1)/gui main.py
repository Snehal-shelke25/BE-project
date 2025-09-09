# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""

from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
from pymsgbox import *


root=tk.Tk()

root.title("Yoga Pose Detection")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

image2 =Image.open('WhatsApp Image 1.jpeg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="Yoga Pose Detection System",width=70,background="purple",fg="white", height=2,font=("Times new roman",27,"bold"))
w.place(x=0,y=0)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="skyblue")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


# wlcm=tk.Label(root,text="......Welcome to Yoga Pose Detection System ......",width=85,height=1,background="purple",foreground="black",font=("Times new roman",22,"bold"))
# wlcm.place(x=0,y=657)




d2=tk.Button(root,text="Login",command=Login,width=6,bd=4,background="white",foreground="black",font=("times new roman",19,"bold"))
d2.place(x=1007,y=15)


d3=tk.Button(root,text="Register",command=Register,width=7,bd=4,background="white",foreground="black",font=("times new roman",19,"bold"))
d3.place(x=1145,y=15)



root.mainloop()
