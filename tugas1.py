import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("data")
window.geometry('500x550')

Label1 = tkinter.Label(window, text="Sending Of Message Form", font=10).place(x=150, y=10)
Label2 = tkinter.Label(window, text="setting").place(x=50, y=50, height=35)
Label3 = tkinter.Label(window, text="Seader").place(x=30, y=200, height=35)
Label4 = tkinter.Label(window, text="Receiver").place(x=300, y=200, height=35)
Label5 = tkinter.Label(window, text="search").place(x=300, y=280)

#membuat label1
mode = tkinter.Label(window, text="Mode :").place(x=50, y=90)
Spinmode = Spinbox(window, from_= 0, to =5).place(x=100, y=90)

#membuat label2
subject = tkinter.Label(window, text="Subject :").place(x=50, y=120)
Spinmode = Spinbox(window, from_= 0, to =5).place(x=100, y=120)

#membuat label3
Connection = tkinter.Label(window, text="Connection:").place(x=250, y=90)
Spinmode = Spinbox(window, from_= 0, to =5).place(x=320, y=90)

#membuat label4
Label1 = Label(window, text="Remote IP :").place(x=250, y=120)
Entry = Entry(window, width=16).place(x=320, y=120)
Button = Button(window, text="   ").place(x=425, y=120)


#membuat label
mode = tkinter.Label(window, text="No Mes :").place(x=30, y=240)
Spinmode = Spinbox(window, from_= 0, to =5).place(x=100, y=240)

#membuat label
mode = tkinter.Label(window, text="Name :").place(x=30, y=270)
Spinmode = Spinbox(window, from_= 0, to =5).place(x=100, y=270)

#membuat label4
Label1 = Label(window, text="Subject Contect :").place(x=30, y=300)
#membuat label
mode = tkinter.Label(window, text="Source :").place(x=300, y=240)
Spinmode = Spinbox(window, from_= 0, to =5).place(x=350, y=240)




window.mainloop()
