from tkinter import *

from PIL import ImageTk,Image




import pymysql



db = pymysql.connect('localhost', 'root', 'root', 'ambulance')

c = db.cursor()

class Login:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x1200")
        image = ImageTk.PhotoImage(file="C:\\Users\\lenovo\\Downloads\\project\\photo-1502740479091-635887520276.jpg")
        self.button = Button(self.master)
        self.button.config(image=image)
        self.button.image = image
        self.button.pack()
        r = "Protect and Promote quality of life and public safety"
        self.Label1 = Label(self.master, text=r, font=("Algerian", 24))
        self.Label1.pack(side=TOP)
        self.Label1.place(x=150, y=70)

        self.l1 = Label(self.master,text='Login Id',height=1,width=10, font=("Elephant", 10))
        self.l1.pack()
        self.l1.place(x=75,y=200)

        self.e1 = Entry(self.master,bd=5)
        self.e1.pack()
        self.e1.place(x=250,y=200)

        self.l2 = Label(self.master, text='Password', height=1, width=10, font=("Elephant", 10))
        self.l2.pack()
        self.l2.place(x=75, y=260)

        self.e2 = Entry(self.master, bd=5, show="*", width=15)
        self.e2.pack()
        self.e2.place(x=250, y=260)

        self.b2 = Button(self.master, text="Enter", command=self.check, height=2, width=10, font=("Elephant", 10))
        self.b2.pack(side=LEFT)
        self.b2.place(x=75, y=320)

    def check(self):

        log=self.e1.get()
        pas=self.e2.get()
        if((log=='Admin')&(pas=='Admin')):
            self.master.withdraw()
            self.last = Toplevel(self.master)
            bbb = Pg1(self.last)
            self.last.geometry("1200x1200")
        else:
            self.lbl=Label(self.master,text="Incorrect password or username, I don't know which one")
            self.lbl.pack()
            self.lbl.place(x=75,y=380)




class Pg1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x1200")
        image = ImageTk.PhotoImage(file="C:\\Users\\lenovo\\Downloads\\project\\amb3.png")
        self.button = Button(self.master)
        self.button.config(image=image)
        self.button.image = image
        self.button.pack()
        r="Protect and Promote quality of life and public safety"
        self.Label1 = Label(self.master,text=r,font=("Algerian",24))
        self.Label1.pack(side=TOP)
        self.Label1.place(x=150,y=70)

        self.b1 = Button(self.master, text="New Entry", command=self.newent, height=2, width=10,font=("Elephant", 10))
        self.b1.pack(side=LEFT)
        self.b1.place(x=75, y=200)
        self.b2 = Button(self.master, text="Enquiry", command=self.enquiry, height=2, width=10,font=("Elephant", 10))
        self.b2.pack(side=LEFT)
        self.b2.place(x=75, y=260)
        self.b3 = Button(self.master, text="Update", command=self.update, height=2, width=10,font=("Elephant", 10))
        self.b3.pack(side=LEFT)
        self.b3.place(x=75, y=320)
        self.b4 = Button(self.master, text="Delete", command=self.delete, height=2, width=10,font=("Elephant", 10))
        self.b4.pack(side=LEFT)
        self.b4.place(x=75, y=380)

    def newent(self):
        print("inside new entry")
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.newWindow.geometry("500x500")

        bb = Pg2(self.newWindow)


    def enquiry(self):
        print("inside enquiry entry")
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.newWindow.geometry("500x500")
        bb = Pg3(self.newWindow)

    def update(self):
        print("inside update entry")
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.newWindow.geometry("500x500")
        bb = Pg4(self.newWindow)

    def delete(self):
        print("inside delete entry")
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.newWindow.geometry("500x500")
        bb = Pg5(self.newWindow)


class Pg2:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x1200")
        image = ImageTk.PhotoImage(file="C:\\Users\\lenovo\\Downloads\\project\\amb3.png")

        self.button = Button(self.master)
        self.button.config(image=image)
        self.button.image = image
        self.button.pack()

        self.b1 = Button(self.master, text="Back", command=self.back, height=2, width=10, font=("Elephant", 10))
        self.b1.pack()
        self.b1.place(x=500, y=550)
        self.b2 = Button(self.master, text="Submit", command=self.submit, height=2, width=10, font=("Elephant", 10))
        self.b2.pack()
        self.b2.place(x=500, y=600)

        sa=self.genid()
        print(sa)
        self.LABEL=Label(text=sa)
        self.LABEL.pack()
        self.e1 = Entry(self.master, bd=5)
        self.e1.insert(10,sa)
        self.e1.pack(side=RIGHT)
        self.e1.place(x=250, y=200)
        self.l1 = Label(self.master, text="Patient Id:", height=2, width=10,font=("Elephant", 11))
        self.l1.pack(side=LEFT)
        self.l1.place(x=75, y=200)
        self.e2 = Entry(self.master, bd=5)  # bd border value
        self.e2.pack(side=RIGHT)
        self.e2.place(x=250, y=260)
        self.l2 = Label(self.master, text="Patient Name:", height=2, width=10,font=("Elephant", 11))
        self.l2.pack(side=LEFT)
        self.l2.place(x=75, y=260)
        self.e3 = Entry(self.master, bd=5)  # bd border value
        self.e3.pack(side=RIGHT)
        self.e3.place(x=250, y=320)
        self.l3 = Label(self.master, text="From:", height=2, width=10,font=("Elephant", 11))
        self.l3.pack(side=LEFT)
        self.l3.place(x=75, y=320)
        self.e4 = Entry(self.master, bd=5)  # bd border value
        self.e4.pack(side=RIGHT)
        self.e4.place(x=250, y=380)
        self.l4 = Label(self.master, text="To:", height=2, width=10,font=("Elephant", 11))
        self.l4.pack(side=LEFT)
        self.l4.place(x=75, y=380)

    def back(self):
        self.master.withdraw()
        self.last = Toplevel(self.master)
        bbb = Pg1(self.last)
        self.last.geometry("1200x1200")

    def submit(self):
        a = self.e1.get()
        a = int(a)
        b = self.e2.get()
        d = self.e3.get()
        e = self.e4.get()

        print(b)
        print(d)
        print(a)
        print(e)
        q1 = "insert into amb values('%d','%s','%s','%s')" % (a, b, d, e)
        c.execute(q1)
        db.commit()
        b = 'select * from amb'
        c.execute(b)

        results = c.fetchall()

        for y in results:
            a1 = y[0]
            a2 = y[1]
            a3 = y[2]
            a4 = y[3]
            print(a1, ' ', a2, ' ', a3, ' ', a4, ' ')

        self.Label=Label(self.master,text="Entry sucessfully submitted")
        self.Label.pack()
        self.Label.place(x=75, y=380)
    def genid(self):
        q1='Select max(id) from amb'
        c.execute(q1)
        r=c.fetchall()
        for y in r:
            al=y[0]
            print(al)
            return(al+1)


class Pg3:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x1200")
        image = ImageTk.PhotoImage(file="C:\\Users\\lenovo\\Downloads\\project\\amb3.png")

        self.button = Button(self.master)
        self.button.config(image=image)
        self.button.image = image
        self.button.pack()
        self.b1 = Button(self.master, text="Back", command=self.back, height=2, width=10, font=("Elephant", 10))
        self.b1.pack()
        self.b1.place(x=500, y=550)
        self.b2 = Button(self.master, text="Submit", command=self.submit, height=2, width=10, font=("Elephant", 10))
        self.b2.pack()
        self.b2.place(x=500, y=600)
        self.e1 = Entry(self.master, bd=5)  # bd border value
        self.e1.pack(side=RIGHT)
        self.e1.place(x=300, y=200)
        self.l1 = Label(self.master, text="Enter Patient Id:", height=2, width=12,font=("Elephant", 10))
        self.l1.pack(side=LEFT)
        self.l1.place(x=75, y=200)

    def back(self):
        self.master.withdraw()
        self.last = Toplevel(self.master)
        bbb = Pg1(self.last)
        self.last.geometry("1200x1200")

    def submit(self):
        self.la = Label(self.master, text='Id:',height=1,width=12)
        self.la.pack(side=LEFT)
        self.la.place(x=75, y=500)
        self.l2 = Label(self.master, text='id',height=1,width=12)
        self.l2.pack(side=LEFT)
        self.l2.place(x=200, y=500)
        self.lb = Label(self.master, text='Name:',height=1,width=12)
        self.lb.pack(side=LEFT)
        self.lb.place(x=75, y=520)
        self.l3 = Label(self.master, text='name',height=1,width=12)
        self.l3.pack(side=LEFT)
        self.l3.place(x=200, y=520)
        self.lc = Label(self.master, text='From:',height=1,width=12)
        self.lc.pack(side=LEFT)
        self.lc.place(x=75, y=540)
        self.l4 = Label(self.master, text='from',height=1,width=12)
        self.l4.pack(side=LEFT)
        self.l4.place(x=200, y=540)
        self.ld = Label(self.master, text='To:',height=1,width=12)
        self.ld.pack(side=LEFT)
        self.ld.place(x=75, y=560)
        self.l5 = Label(self.master, text='to',height=1,width=12)
        self.l5.pack(side=LEFT)
        self.l5.place(x=200, y=560)

        a = self.e1.get()
        a = int(a)
        q1 = "select * from amb where id = '%d'" % (a)
        c.execute(q1)
        r = c.fetchall()
        print(r)
        for y in r:
            a1 = y[0]
            a2 = y[1]
            a3 = y[2]
            a4 = y[3]
            print(a1, ' ', a2, ' ', a3, ' ', a4, ' ')
            self.l2.config(text=a1)
            self.l3.config(text=a2)
            self.l4.config(text=a3)
            self.l5.config(text=a4)


class Pg4:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x1200")
        image = ImageTk.PhotoImage(file="C:\\Users\\lenovo\\Downloads\\project\\amb3.png")

        self.button = Button(self.master)
        self.button.config(image=image)
        self.button.image = image
        self.button.pack()
        self.b1 = Button(self.master, text="Back", command=self.back, height=2, width=10, font=("Elephant", 10))
        self.b1.pack()
        self.b1.place(x=500, y=550)
        self.b2 = Button(self.master, text="Submit", command=self.submit, height=2, width=10, font=("Elephant", 10))
        self.b2.pack()
        self.b2.place(x=500, y=600)


        self.b3 = Button(self.master, text="Show", command=self.show, height=2, width=10, font=("Elephant", 10))
        self.b3.pack()
        self.b3.place(x=500, y=650)

        self.e1 = Entry(self.master, bd=5)  # bd border value
        self.e1.pack(side=RIGHT)
        self.e1.place(x=250, y=200)
        self.l1 = Label(self.master, text="To Be Updated:", height=2, width=12, font=("Elephant", 10))
        self.l1.pack(side=LEFT)
        self.l1.place(x=75, y=200)
        self.ea = Entry(self.master, bd=5)  # bd border value
        self.ea.pack(side=RIGHT)
        self.ea.place(x=250, y=260)
        self.la = Label(self.master, text="Patient Id:", height=2, width=12, font=("Elephant", 10))
        self.la.pack(side=LEFT)
        self.la.place(x=75, y=260)
        self.e2 = Entry(self.master, bd=5)  # bd border value
        self.e2.pack(side=RIGHT)
        self.e2.place(x=250, y=320)
        self.l2 = Label(self.master, text="Patient Name:", height=2, width=12, font=("Elephant", 10))
        self.l2.pack(side=LEFT)
        self.l2.place(x=75, y=320)
        self.e3 = Entry(self.master, bd=5)  # bd border value
        self.e3.pack(side=RIGHT)
        self.e3.place(x=250, y=380)
        self.l3 = Label(self.master, text="From:", height=2, width=12, font=("Elephant", 10))
        self.l3.pack(side=LEFT)
        self.l3.place(x=75, y=380)
        self.e4 = Entry(self.master, bd=5)  # bd border value
        self.e4.pack(side=RIGHT)
        self.e4.place(x=250, y=440)
        self.l4 = Label(self.master, text="To:", height=2, width=12, font=("Elephant", 10))
        self.l4.pack(side=LEFT)
        self.l4.place(x=75, y=440)

    def back(self):
        self.master.withdraw()
        self.last = Toplevel(self.master)
        bbb = Pg1(self.last)
        self.last.geometry("1200x1200")

    def submit(self):
        f = self.e1.get()
        f = int(f)
        a = self.ea.get()
        a = int(a)
        b = self.e2.get()
        d = self.e3.get()
        e = self.e4.get()
        qq = "update amb set id=('%d')where id = ('%d')" % (a, f)
        c.execute(qq)
        db.commit()
        q2 = "update amb set name=('%s')where id = ('%d')" % (b, f)
        c.execute(q2)
        db.commit()
        q3 = "update amb set origin=('%s')where id = ('%d')" % (d, f)
        c.execute(q3)
        db.commit()
        q4 = "update amb set destination=('%s')where id = ('%d')" % (e, f)
        c.execute(q4)
        db.commit()

        qqq = "select * from amb"
        c.execute(qqq)
        r = c.fetchall()

        for y in r:
            a1 = y[0]
            a2 = y[1]
            a3 = y[2]
            a4 = y[3]
            print(a1, ' ', a2, ' ', a3, ' ', a4, ' ')

    def show(self):
        self.la = Label(self.master, text='Id:', height=1, width=12)
        self.la.pack(side=LEFT)
        self.la.place(x=700, y=300)
        self.l2 = Label(self.master, text='id', height=1, width=12)
        self.l2.pack(side=BOTTOM)
        self.l2.place(x=900, y=300)
        self.lb = Label(self.master, text='Name:', height=1, width=12)
        self.lb.pack(side=BOTTOM)
        self.lb.place(x=700, y=320)
        self.l3 = Label(self.master, text='name', height=1, width=12)
        self.l3.pack(side=BOTTOM)
        self.l3.place(x=900, y=320)
        self.lc = Label(self.master, text='From:', height=1, width=12)
        self.lc.pack(side=BOTTOM)
        self.lc.place(x=700, y=340)
        self.l4 = Label(self.master, text='from', height=1, width=12)
        self.l4.pack(side=BOTTOM)
        self.l4.place(x=900, y=340)
        self.ld = Label(self.master, text='To:', height=1, width=12)
        self.ld.pack(side=BOTTOM)
        self.ld.place(x=700, y=360)
        self.l5 = Label(self.master, text='to', height=1, width=12)
        self.l5.pack(side=BOTTOM)
        self.l5.place(x=900, y=360)

        a = self.e1.get()
        a = int(a)
        q1 = "select * from amb where id = '%d'" % (a)
        c.execute(q1)
        r = c.fetchall()
        print(r)
        for y in r:
            a1 = y[0]
            a2 = y[1]
            a3 = y[2]
            a4 = y[3]
            print(a1, ' ', a2, ' ', a3, ' ', a4, ' ')
        self.l2.config(text=a1)
        self.l3.config(text=a2)
        self.l4.config(text=a3)
        self.l5.config(text=a4)


class Pg5:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x1200")
        image = ImageTk.PhotoImage(file="C:\\Users\\lenovo\\Downloads\\project\\amb3.png")

        self.button = Button(self.master)
        self.button.config(image=image)
        self.button.image = image
        self.button.pack()
        self.b1 = Button(self.master, text="Back", command=self.back, height=2, width=10, font=("Elephant", 10))
        self.b1.pack()
        self.b1.place(x=600, y=200)
        self.b2 = Button(self.master, text="Submit", command=self.submit, height=2, width=10, font=("Elephant", 10))
        self.b2.pack()
        self.b2.place(x=600, y=250)

        self.b3 = Button(self.master, text="Show", command=self.show, height=2, width=10, font=("Elephant", 10))
        self.b3.pack()
        self.b3.place(x=600, y=300)

        self.e1 = Entry(self.master, bd=5)  # bd border value
        self.e1.pack(side=RIGHT)
        self.e1.place(x=300, y=200)
        self.l1 = Label(self.master, text="Enter Patient Id:", height=2, width=12, font=("Elephant", 11))
        self.l1.pack(side=LEFT)
        self.l1.place(x=75, y=200)

    def back(self):
        self.master.withdraw()
        self.last = Toplevel(self.master)
        bbb = Pg1(self.last)
        self.last.geometry("1200x1200")

    def submit(self):
        a = self.e1.get()
        a = int(a)
        q1 = "delete from amb where id = '%d'" % (a)
        c.execute(q1)
        db.commit()
        qqq = "select * from amb"
        c.execute(qqq)
        r = c.fetchall()
        for y in r:
            a1 = y[0]
            a2 = y[1]
            a3 = y[2]
            a4 = y[3]
            print(a1, ' ', a2, ' ', a3, ' ', a4, ' ')

        self.Label = Label(text="Entry sucessfully submitted")
        self.Label.pack()

    def show(self):
        self.la = Label(self.master, text='id:')
        self.la.pack(side=LEFT)
        self.la.place(x=5, y=300)
        self.l2 = Label(self.master, text='id')
        self.l2.pack(side=BOTTOM)
        self.l2.place(x=100, y=300)
        self.lb = Label(self.master, text='name:')
        self.lb.pack(side=BOTTOM)
        self.lb.place(x=5, y=320)
        self.l3 = Label(self.master, text='name')
        self.l3.pack(side=BOTTOM)
        self.l3.place(x=100, y=320)
        self.lc = Label(self.master, text='from:')
        self.lc.pack(side=BOTTOM)
        self.lc.place(x=5, y=340)
        self.l4 = Label(self.master, text='from')
        self.l4.pack(side=BOTTOM)
        self.l4.place(x=100, y=340)
        self.ld = Label(self.master, text='to:')
        self.ld.pack(side=BOTTOM)
        self.ld.place(x=5, y=360)
        self.l5 = Label(self.master, text='to')
        self.l5.pack(side=BOTTOM)
        self.l5.place(x=100, y=360)
        a = self.e1.get()
        a = int(a)
        q1 = "select * from amb where id = '%d'" % (a)
        c.execute(q1)
        r = c.fetchall()
        print(r)
        for y in r:
            a1 = y[0]
            a2 = y[1]
            a3 = y[2]
            a4 = y[3]
            print(a1, ' ', a2, ' ', a3, ' ', a4, ' ')
            self.l2.config(text=a1)
            self.l3.config(text=a2)
            self.l4.config(text=a3)
            self.l5.config(text=a4)

root = Tk()
root.title("Welcome")
b =Login(root)

root.mainloop()

