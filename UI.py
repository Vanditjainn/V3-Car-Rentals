import functions as func
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import time


# Time on the leftTop
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :' + date_string + "\n" + "Time : " + time_string)
    clock.after(200, tick)


# Introduction Label
def IntroLabelTick():
    global count, text
    if count >= len(ss):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(170, IntroLabelTick)


def exitCar():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if res:
        root.destroy()


root = Tk()
root.title("Car Rental")
root.config(bg='skyblue')
root.geometry('1174x700+200+50')
root.iconbitmap('mana.ico')
root.resizable(False, False)

"""Frames"""

DataEntryFrame = Frame(root, bg='white', relief=SOLID, borderwidth=3)
DataEntryFrame.place(x=10, y=80, width=500, height=600)

"""Data Entry Frame"""
frontlabel = Label(DataEntryFrame, text='------------COMMENÇONS------------', width=25,
                   font=('calibri', 30, 'italic bold'))
frontlabel.pack(side=TOP, expand=TRUE)
addbtn = Button(DataEntryFrame, text='1. Add Car', width=25, font=('calibri', 20, 'bold'), bg='pink', bd=3,
                activebackground='skyblue', relief=SOLID, command=lambda: func.addCar(Cartable, DataEntryFrame))
addbtn.pack(side=TOP, expand=TRUE)

searchbtn = Button(DataEntryFrame, text='2. Search Car', width=25, font=('calibri', 20, 'bold'), bg='pink', bd=3,
                   activebackground='skyblue', relief=SOLID, command=lambda: func.searchCar(Cartable, DataEntryFrame))
searchbtn.pack(side=TOP, expand=TRUE)

deletebtn = Button(DataEntryFrame, text='3. Delete Car', width=25, font=('calibri', 20, 'bold'), bg='pink', bd=3,
                   activebackground='skyblue', relief=SOLID, command=lambda: func.deleteCar(Cartable))
deletebtn.pack(side=TOP, expand=TRUE)

updatebtn = Button(DataEntryFrame, text='4. Update Car', width=25, font=('calibri', 20, 'bold'), bg='pink', bd=3,
                   activebackground='skyblue', relief=SOLID, command=lambda: func.updateCar(Cartable, DataEntryFrame))
updatebtn.pack(side=TOP, expand=TRUE)

showallbtn = Button(DataEntryFrame, text='5. Show All', width=25, font=('calibri', 20, 'bold'), bg='pink', bd=3,
                    activebackground='skyblue', relief=SOLID, command=lambda: func.showCar(Cartable))
showallbtn.pack(side=TOP, expand=TRUE)

exportbtn = Button(DataEntryFrame, text='6. Export Data', width=25, font=('calibri', 20, 'bold'), bg='pink', bd=3,
                   activebackground='skyblue', relief=SOLID, command=lambda: func.exportCar(Cartable))
exportbtn.pack(side=TOP, expand=TRUE)

exitbtn = Button(DataEntryFrame, text='7. Exit', width=25, font=('calibri', 20, 'bold'), bg='pink', bd=3,
                 activebackground='skyblue', relief=SOLID, command=exitCar)
exitbtn.pack(side=TOP, expand=TRUE)

"""Show Data Frame"""
ShowDataFrame = Frame(root, bg='white', relief=SOLID, borderwidth=3)
ShowDataFrame.place(x=530, y=80, width=620, height=600)

style = ttk.Style()
style.configure('Treeview.Heading', font=('times', 15, 'bold'))
style.configure('Treeview', font=('times', 13, 'bold'), background='pink', foreground='black')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
Cartable = Treeview(ShowDataFrame,
                    columns=('id', 'model', 'color', 'year', 'rent', 'mileage', 'about', 'Added Date', 'Added Time'),
                    yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=Cartable.xview)
scroll_y.config(command=Cartable.yview)
Cartable.heading('id', text='ID')
Cartable.heading('model', text='Model')
Cartable.heading('color', text='Color')
Cartable.heading('year', text='Year')
Cartable.heading('rent', text='Rent')
Cartable.heading('mileage', text='Mileage')
Cartable.heading('about', text='About')
Cartable.heading('Added Date', text='Added Date')
Cartable.heading('Added Time', text='Added Time')
Cartable['show'] = 'headings'
Cartable.column('id', width=100)
Cartable.column('model', width=200)
Cartable.column('color', width=100)
Cartable.column('year', width=100)
Cartable.column('rent', width=150)
Cartable.column('mileage', width=100)
Cartable.column('about', width=200)
Cartable.column('Added Date', width=150)
Cartable.column('Added Time', width=150)
Cartable.pack(fill=BOTH, expand=1)

"""Sliders"""
ss = 'Welcome To SS Car Rentals'
count = 0
text = ''
SliderLabel = Label(root, text=ss, font=('calibri', 30, 'italic bold'), relief=SOLID, borderwidth=3, width=25,
                    bg="pink")
SliderLabel.place(x=260, y=0)
IntroLabelTick()

"""Clock"""
clock = Label(root, font=('calibri', 14, 'italic bold'), relief=SOLID, borderwidth=3, width=15, height=2, bg="pink")
clock.place(x=0, y=0)
tick()

"""Connect Database Button"""
connectbutton = Button(root, text='Connect to Database', font=('calibri', 14, 'italic bold'), relief=SOLID,
                       borderwidth=3,
                       width=23, bg='pink', activebackground='black', activeforeground='white', command=func.Connectdb)
connectbutton.place(x=930, y=0)

root.mainloop()
