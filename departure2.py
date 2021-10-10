from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
from departure3 import *

def mymap2():
    root = Tk()
    root.geometry("768x1024")
    root.minsize(768, 1024)
    root.maxsize(768, 1024)
    def myfuncv():
        root.destroy()
        mymap3()
    myFont = font.Font(family='Consolas', size=15)
    mapl1 = Label(root, text="Map for Arpt #1")
    mapl1.config(font=("Consolas", 15))
    mapl1.place(relx=0.8, rely=0.1, anchor='center')
    lb1 = Label(root, text="Clear for push and start after 5 mins")
    lb1.config(font=("Consolas", 15))
    lb1.place(relx=0.5, rely=0.55, anchor='center')
    btnn = Button(root, text='Next', bg='black', fg='white', command=myfuncv)
    btnn.place(relx=0.5, rely=0.63, anchor='center')
    btnn['font'] = myFont
    ll3 = Label(root, text="Press Next after Push and Start")
    ll3.config(font=("Consolas", 10))
    ll3.place(relx=0.5, rely=0.67, anchor='center')
    img = Image.open("arpmap.jpg")
    img = img.resize((500, 500))
    tkimage = ImageTk.PhotoImage(img)
    map = Label(root, image=tkimage).grid()
    map.place(x=40, y =40)
    root.mainloop()