from tkinter import *
import tkinter.font as font
from arrival1 import *
from departure1 import *

root = Tk()
root.geometry("768x1024")
root.minsize(768, 1024)
root.maxsize(768, 1024)

def myfuncb():
    root.destroy()
    my_funca()

def myfuncd():
    root.destroy()
    my_funcc()

myFont = font.Font(family='Consolas', size=15)

# Txt1 = Text(root, height = 5, width = 100)
l1 = Label(root, text = "Hello there!")
l1.config(font = ("Consolas", 15))
l1.place(relx = 0.5, rely = 0.3, anchor = 'center')

# Txt2 = Text(root, height = 5, width = 100)
l2 = Label(root, text = "Please click on the following buttons to continue-")
l2.config(font = ("Consolas", 15))
l2.place(relx = 0.5, rely = 0.35, anchor = 'center')

btndep = Button(root, text = 'Departure', bg = 'black', fg = 'white',  command = myfuncd)
btndep.place(relx = 0.4, rely = 0.45, anchor = 'e')
btndep['font'] = myFont



btnarr = Button(root, text = 'Arrival', bg = 'black', fg = 'white', command = myfuncb)
btnarr.place(relx = 0.62, rely = 0.45, anchor = 'w')
btnarr['font'] = myFont

#l1.pack()
#l2.pack()

root.mainloop()
