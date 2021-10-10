from tkinter import *
import tkinter.font as font
from arrival2 import *

def my_funca():
    root = Tk()
    root.geometry("768x1024")
    root.minsize(768, 1024)
    root.maxsize(768, 1024)
    def myfunce():
        root.destroy()
        mymap()
    myFont = font.Font(family='Consolas', size=15)
    #labels
    fuell = Label(root, text="Enter Fuel Left(in litres)")
    fuell.config(font=("Consolas", 15))
    fuell.place(relx=0.3, rely=0.3, anchor='center')
    dwl = Label(root, text="Enter dry weight(in tons)")
    dwl.config(font=("Consolas", 15))
    dwl.place(relx=0.3, rely=0.35, anchor='center')
    arpl = Label(root, text="Enter Airport Code")
    arpl.config(font=("Consolas", 15))
    arpl.place(relx=0.3, rely=0.25, anchor='center')
    bgwl = Label(root, text="Enter baggage weight(tons")
    bgwl.config(font=("Consolas", 15))
    bgwl.place(relx=0.3, rely=0.4, anchor='center')
    altl = Label(root, text="Enter Altitude(in feet)")
    altl.config(font=("Consolas", 15))
    altl.place(relx=0.3, rely=0.45, anchor='center')
    pwl = Label(root, text="Enter Passenger Weight(in tons)")
    pwl.config(font=("Consolas", 15))
    pwl.place(relx=0.3, rely=0.5, anchor='center')
    #entryboxes
    flq = Entry(root)
    flq.place(relx = 0.65, rely = 0.3, anchor = 'center')
    dw = Entry(root)
    dw.place(relx=0.65, rely=0.35, anchor='center')
    arp = Entry(root)
    arp.place(relx=0.65, rely=0.25, anchor='center')
    bgw = Entry(root)
    bgw.place(relx=0.65, rely=0.4, anchor='center')
    alt = Entry(root)
    alt.place(relx=0.65, rely=0.45, anchor='center')
    pw = Entry(root)
    pw.place(relx=0.65, rely=0.5, anchor='center')
    fuel=0
    dryw=0
    arpc=0
    bgwq=0
    alth=0
    pwq=0
    def valuegetter():
        an1 = flq.get()
        fuel = int(an1)
        an2 = dw.get()
        dryw = int(an2)
        an3 = arp.get()
        arpc = int(an3)
        an4 = bgw.get()
        bgwq = int(an4)
        an5 = alt.get()
        alth = int(an5)
        an6 = pw.get()
        pwq = int(an6)
        if arpc == 1:
            myfunce()
        else:
            print('error')
    btn = Button(root, text= "Proceed", bg = 'black', fg = 'white', command = valuegetter)
    btn.place(relx = 0.5, rely = 0.6, anchor = 'center')
    btn['font'] = myFont
    root.mainloop()

