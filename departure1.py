from tkinter import *
import tkinter.font as font
from departure2 import *

def my_funcc():
    root = Tk()
    root.geometry("768x1024")
    root.minsize(768, 1024)
    root.maxsize(768, 1024)
    def myfuncf():
        root.destroy()
        mymap2()
    myFont = font.Font(family='Consolas', size=15)
    #labels
    fuell2 = Label(root, text="Enter Fuel Left(in litres)")
    fuell2.config(font=("Consolas", 15))
    fuell2.place(relx=0.3, rely=0.3, anchor='center')
    dwl2 = Label(root, text="Enter dry weight(in tons)")
    dwl2.config(font=("Consolas", 15))
    dwl2.place(relx=0.3, rely=0.35, anchor='center')
    arpl2 = Label(root, text="Enter Airport Code")
    arpl2.config(font=("Consolas", 15))
    arpl2.place(relx=0.3, rely=0.25, anchor='center')
    bgwl2 = Label(root, text="Enter baggage weight(tons")
    bgwl2.config(font=("Consolas", 15))
    bgwl2.place(relx=0.3, rely=0.4, anchor='center')
    gtnl = Label(root, text="Enter Gate Number")
    gtnl.config(font=("Consolas", 15))
    gtnl.place(relx=0.3, rely=0.45, anchor='center')
    pwl2 = Label(root, text="Enter Passenger Weight(in tons)")
    pwl2.config(font=("Consolas", 15))
    pwl2.place(relx=0.3, rely=0.5, anchor='center')
    #entryboxes
    flq2 = Entry(root)
    flq2.place(relx = 0.65, rely = 0.3, anchor = 'center')
    dw2 = Entry(root)
    dw2.place(relx=0.65, rely=0.35, anchor='center')
    arp2 = Entry(root)
    arp2.place(relx=0.65, rely=0.25, anchor='center')
    bgw2 = Entry(root)
    bgw2.place(relx=0.65, rely=0.4, anchor='center')
    gtn = Entry(root)
    gtn.place(relx=0.65, rely=0.45, anchor='center')
    pw2 = Entry(root)
    pw2.place(relx=0.65, rely=0.5, anchor='center')
    fuel2=0
    dryw2=0
    arpc2=0
    bgwq2=0
    gn=0
    pwq2=0
    def valuegetter2():
        An1 = flq2.get()
        fuel2 = int(An1)
        An2 = dw2.get()
        dryw2 = int(An2)
        An3 = arp2.get()
        arpc2 = int(An3)
        An4 = bgw2.get()
        bgwq2 = int(An4)
        An5 = gtn.get()
        gn = int(An5)
        An6 = pw2.get()
        pwq2 = int(An6)
        myfuncf()
    btn = Button(root, text= "Proceed", bg = 'black', fg = 'white', command = valuegetter2)
    btn.place(relx = 0.5, rely = 0.6, anchor = 'center')
    btn['font'] = myFont
    root.mainloop()

