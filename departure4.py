from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

def mymap4():
    root = Tk()
    root.geometry("768x1024")
    root.minsize(768, 1024)
    root.maxsize(768, 1024)
    myFont = font.Font(family='Consolas', size=15)
    mapl2 = Label(root, text="Map for Arpt #1")
    mapl2.config(font=("Consolas", 15))
    mapl2.place(relx=0.8, rely=0.1, anchor='center')
    lb3 = Label(root, text="Approved for takeoff")
    lb3.config(font=("Consolas", 15))
    lb3.place(relx=0.5, rely=0.55, anchor='center')
    btnn3 = Button(root, text='End', bg='black', fg='white', command=root.destroy)
    btnn3.place(relx=0.5, rely=0.63, anchor='center')
    btnn3['font'] = myFont
    ll5 = Label(root, text="Press End after gear up")
    ll5.config(font=("Consolas", 10))
    ll5.place(relx=0.5, rely=0.67, anchor='center')
    img = Image.open("arpmap.jpg")
    img = img.resize((500, 500))
    tkimage = ImageTk.PhotoImage(img)
    map = Label(root, image=tkimage).grid()
    map.place(x=40, y =40)
    root.mainloop()