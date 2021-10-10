from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

def mymap():
    root = Tk()
    root.geometry("768x1024")
    root.minsize(768, 1024)
    root.maxsize(768, 1024)
    mapl = Label(root, text="Map for Arpt #1")
    mapl.config(font=("Consolas", 15))
    mapl.place(relx=0.8, rely=0.1, anchor='center')
    img = Image.open("arpmap.jpg")
    img = img.resize((500, 500))
    tkimage = ImageTk.PhotoImage(img)
    map = Label(root, image=tkimage).grid()
    map.place(x=40, y =40)
    root.mainloop()