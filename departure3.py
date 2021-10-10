from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
from departure4 import *

def mymap3():
    root = Tk()
    root.geometry("768x1024")
    root.minsize(768, 1024)
    root.maxsize(768, 1024)
    def myfuncg():
        root.destroy()
        mymap4()
    myFont = font.Font(family='Consolas', size=15)
    mapl2 = Label(root, text="Map for Arpt #1")
    mapl2.config(font=("Consolas", 15))
    mapl2.place(relx=0.8, rely=0.1, anchor='center')
    lb2 = Label(root, text="Taxi to 09L via B4 to A2")
    lb2.config(font=("Consolas", 15))
    lb2.place(relx=0.5, rely=0.55, anchor='center')
    btnn2 = Button(root, text='Next', bg='black', fg='white', command=myfuncg)
    btnn2.place(relx=0.5, rely=0.63, anchor='center')
    btnn2['font'] = myFont
    ll4 = Label(root, text="Press Next after Taxi")
    ll4.config(font=("Consolas", 10))
    ll4.place(relx=0.5, rely=0.67, anchor='center')
    img = Image.open("arpmap.jpg")
    img = img.resize((500, 500))
    tkimage = ImageTk.PhotoImage(img)
    map = Label(root, image=tkimage).grid()
    map.place(x=40, y =40)
    root.mainloop()