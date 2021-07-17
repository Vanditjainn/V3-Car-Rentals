from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
import pandas
import pymysql
import time


def Connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect please try again', parent=dbroot)
            return
        try:
            strr = 'create database Carrentalsystem1'
            mycursor.execute(strr)
            strr = 'use Carrentalsystem1'
            mycursor.execute(strr)
            strr = 'create table Cardata1(id int,model varchar(100),color varchar(12),year varchar(30),rent varchar(100),mileage varchar(50),about varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table Cardata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table Cardata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database created! Now you are connected to the database',
                                parent=dbroot)
        except:
            strr = 'use Carrentalsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database!', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('mana.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='darkorange')
    # -------------------------------Connectdb Labels
    hostlabel = Label(dbroot, text="Enter Host : ", bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=13, anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text="Enter User : ", bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password : ", bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=13, anchor='w')
    passwordlabel.place(x=10, y=130)

    # ************** Connectdb entry *******************#
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('times', 15, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('times', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('times', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    # ******************* Connectdb Button ********************#
    submitbutton = Button(dbroot, text='Submit', font=('times', 20, 'bold'), width=10, bg='white', bd=5,
                          activebackground='skyblue', command=submitdb)
    submitbutton.place(x=150, y=190)

    dbroot.mainloop()


def addCar(cartable, DataEntryFrame):
    def submitadd():
        id = idval.get()
        model = modelval.get()
        color = colorval.get()
        year = yearval.get()
        rent = rentval.get()
        mileage = mileageval.get()
        about = aboutval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into Cardata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, model, color, year, rent, mileage, about, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notification',
                                            'Id- {} Model- {} Added sucessfully!Do you want to clean the form?'.format(id,
                                                                                                                     model),
                                            parent=addroot)
            if (res == True):
                idval.set('')
                modelval.set('')
                colorval.set('')
                yearval.set('')
                rentval.set('')
                mileageval.set('')
                aboutval.set('')
        except:
            messagebox.showerror('Notification', 'Id already exists try another id...', parent=addroot)
        strr = 'select * from Cardata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        cartable.delete(*cartable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            cartable.insert('', END, values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Car Rental System')
    addroot.config(bg='darkorange')
    addroot.iconbitmap('mana.ico')
    addroot.resizable(False, False)
    # --------------------------------------------------- Add Car Labels
    idlabel = Label(addroot, text='Car Id : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    modellabel = Label(addroot, text='Car Model : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    modellabel.place(x=10, y=70)

    colorlabel = Label(addroot, text='Car Color : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    colorlabel.place(x=10, y=130)

    yearlabel = Label(addroot, text='Reg. Year : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    yearlabel.place(x=10, y=190)

    rentlabel = Label(addroot, text='Rent/day(INR) : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=13, anchor='w')
    rentlabel.place(x=10, y=250)

    mileagelabel = Label(addroot, text='Car Mileage : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    mileagelabel.place(x=10, y=310)

    aboutlabel = Label(addroot, text='About Car : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    aboutlabel.place(x=10, y=370)

    # ----------------------------------------------------------- Add Car Entry
    idval = StringVar()
    modelval = StringVar()
    colorval = StringVar()
    yearval = StringVar()
    rentval = StringVar()
    mileageval = StringVar()
    aboutval = StringVar()

    identry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    modelentry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=modelval)
    modelentry.place(x=250, y=70)

    colorentry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=colorval)
    colorentry.place(x=250, y=130)

    yearentry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=yearval)
    yearentry.place(x=250, y=190)

    rententry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=rentval)
    rententry.place(x=250, y=250)

    mileageentry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=mileageval)
    mileageentry.place(x=250, y=310)

    aboutentry = Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=aboutval)
    aboutentry.place(x=250, y=370)
    ############------------------------- add button
    submitbtn = Button(addroot, text='Submit', font=('times', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='white', command=submitadd)
    submitbtn.place(x=150, y=420)

    addroot.mainloop()


def searchCar(Cartable, DataEntryFrame):
    def search():
        id = idval.get()
        model = modelval.get()
        color = colorval.get()
        year = yearval.get()
        rent = rentval.get()
        mileage = mileageval.get()
        about = aboutval.get()
        addeddate = time.strftime("%d/%m/%Y")

        def execute(var, str):
            mycursor.execute(str, (var))
            datas = mycursor.fetchall()
            Cartable.delete(*Cartable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                Cartable.insert('', END, values=vv)

        if id != '':
            str = 'select *from Cardata1 where id=%s'
            execute(id, str)
        elif model != '':
            str = 'select *from Cardata1 where model=%s'
            execute(model, str)
        elif color != '':
            str = 'select *from Cardata1 where color=%s'
            execute(color, str)
        elif year != '':
            str = 'select *from Cardata1 where year=%s'
            execute(year, str)
        elif rent != '':
            str = 'select *from Cardata1 where rent=%s'
            execute(rent, str)
        elif mileage != '':
            str = 'select *from Cardata1 where mileage=%s'
            execute(mileage, str)
        elif about != '':
            str = 'select *from Cardata1 where about=%s'
            execute(about, str)

        elif addeddate != '':
            str = 'select *from Cardata1 where addeddate=%s'
            execute(addeddate, str)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Car Rental System')
    searchroot.config(bg='darkorange')
    searchroot.iconbitmap('mana.ico')
    searchroot.resizable(False, False)
    # --------------------------------------------------- SSearch Car Labels
    idlabel = Label(searchroot, text='Search Id : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    modellabel = Label(searchroot, text='Search Model : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    modellabel.place(x=10, y=70)

    colorlabel = Label(searchroot, text='Search Color : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    colorlabel.place(x=10, y=130)

    yearlabel = Label(searchroot, text='Search Reg. Year : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=14, anchor='w')
    yearlabel.place(x=10, y=190)

    rentlabel = Label(searchroot, text='Search Rent(INR) : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=14, anchor='w')
    rentlabel.place(x=10, y=250)

    mileagelabel = Label(searchroot, text='Search Mileage : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    mileagelabel.place(x=10, y=310)

    aboutlabel = Label(searchroot, text='Search About : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    aboutlabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Search Date : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    ##----------------------------------------------------------- Search Car Entry
    idval = StringVar()
    modelval = StringVar()
    colorval = StringVar()
    yearval = StringVar()
    rentval = StringVar()
    mileageval = StringVar()
    aboutval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    modelentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=modelval)
    modelentry.place(x=250, y=70)

    colorentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=colorval)
    colorentry.place(x=250, y=130)

    yearentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=yearval)
    yearentry.place(x=250, y=190)

    rententry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=rentval)
    rententry.place(x=250, y=250)

    mileageentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=mileageval)
    mileageentry.place(x=250, y=310)

    aboutentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=aboutval)
    aboutentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)
    ############------------------------- Add button
    submitbtn = Button(searchroot, text='Search', font=('times', 15, 'bold'), width=20, bd=5,
                       activebackground='skyblue', activeforeground='white',
                       bg='white', command=search)
    submitbtn.place(x=150, y=480)

    searchroot.mainloop()


def deleteCar(Cartable):
    cc = Cartable.focus()
    content = Cartable.item(cc)
    pp = content['values'][0]
    strr = "delete from Cardata1 where id=%s"
    mycursor.execute(strr, pp)
    con.commit()
    messagebox.showinfo('Notifications', 'id {} deleted sucessfully...'.format(pp))
    strr = 'select *from Cardata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    Cartable.delete(*Cartable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        Cartable.insert('', END, values=vv)


def updateCar(Cartable, DataEntryFrame):
    def update():
        id = idval.get()
        model = modelval.get()
        color = colorval.get()
        year = yearval.get()
        rent = rentval.get()
        mileage = mileageval.get()
        about = aboutval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update Cardata1 set model=%s,color=%s,year=%s,rent=%s,mileage=%s,about=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr, (model, color, year, rent, mileage, about, date, time, id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully!'.format(id), parent=updateroot)
        strr = 'select *from Cardata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        Cartable.delete(*Cartable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            Cartable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Car Rental System')
    updateroot.config(bg='darkorange')
    updateroot.iconbitmap('mana.ico')
    updateroot.resizable(False, False)
    # --------------------------------------------------- Update Car Labels
    idlabel = Label(updateroot, text='Update ID : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    modellabel = Label(updateroot, text='Update Model : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    modellabel.place(x=10, y=70)

    colorlabel = Label(updateroot, text='Update Color : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    colorlabel.place(x=10, y=130)

    yearlabel = Label(updateroot, text='Update Year : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    yearlabel.place(x=10, y=190)

    rentlabel = Label(updateroot, text='Update Rent(INR) : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=14, anchor='w')
    rentlabel.place(x=10, y=250)

    mileagelabel = Label(updateroot, text='Update Mileage : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    mileagelabel.place(x=10, y=310)

    aboutlabel = Label(updateroot, text='Update About : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    aboutlabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Update Date : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Update Time : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=490)

    ##----------------------------------------------------------- Update Car Entry
    idval = StringVar()
    modelval = StringVar()
    colorval = StringVar()
    yearval = StringVar()
    rentval = StringVar()
    mileageval = StringVar()
    aboutval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    modelentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=modelval)
    modelentry.place(x=250, y=70)

    colorentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=colorval)
    colorentry.place(x=250, y=130)

    yearentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=yearval)
    yearentry.place(x=250, y=190)

    rententry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=rentval)
    rententry.place(x=250, y=250)

    mileageentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=mileageval)
    mileageentry.place(x=250, y=310)

    aboutentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=aboutval)
    aboutentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)
    ############------------------------- Update button
    submitbtn = Button(updateroot, text='Update', font=('times', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='white', command=update)
    submitbtn.place(x=150, y=540)
    cc = Cartable.focus()
    content = Cartable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        idval.set(pp[0])
        modelval.set(pp[1])
        colorval.set(pp[2])
        yearval.set(pp[3])
        rentval.set(pp[4])
        mileageval.set(pp[5])
        aboutval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()


def showCar(Cartable):
    strr = 'select * from Cardata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    Cartable.delete(*Cartable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        Cartable.insert('', END, values=vv)


def exportCar(Cartable):
    ff = filedialog.asksaveasfilename()
    gg = Cartable.get_children()
    id, model, color, year, rent, mileage, about, addeddate, addedtime = [], [], [], [], [], [], [], [], []
    for i in gg:
        content = Cartable.item(i)
        pp = content['values']
        id.append(pp[0]), model.append(pp[1]), color.append(pp[2]), year.append(pp[3]), rent.append(
            pp[4]), mileage.append(pp[5]),
        about.append(pp[6]), addeddate.append(pp[7]), addedtime.append(pp[8])
    dd = ['Id', 'Model', 'Color', 'Year', 'Rent', 'Mileage', 'About', 'Added Date', 'Added Time']
    df = pandas.DataFrame(list(zip(id, model, color, year, rent, mileage, about, addeddate, addedtime)), columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notification', 'Car data is Saved {}'.format(paths))
