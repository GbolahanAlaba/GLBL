from tkinter import *
from tkinter import ttk
from datetime import *
from time import strftime
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import sqlite3
import dashboard
import sales
import customers
import addproduct
import salesorder



class AddCustomer:
    def __init__(self, window):
        self.window = window
        width = 800
        height = 500
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenwidth()
        x = (sw/5)
        y = (sh/11)
        self.window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.window.title('SOAR ACCT | Add New Customer Page')
        self.window.configure(bg='#f7f3f2')
        self.window.wm_iconbitmap('FMCG.ico')
        self.window.resizable(0, 0)

        # Database
        def AddCustomer():
            db = sqlite3.connect('GLBL.db')
            cursor = db.cursor()
            Val = ((NameEntry.get()), Combo.get(), MobileEntry.get(), DateEnt.get())
            cursor.executemany('insert into customers (Name, Location, MobileNo, Date) values(?, ?, ?, ?)', [Val])
            
            db.commit()
            db.close()

            NameEntry.delete(0, END)
            MobileEntry.delete(0, END)




        # First Frame & Menu
        MenuFrame = Frame(window)
        MenuFrame.pack(fill=X, expand='no')

        Menu = Button(MenuFrame, text = 'Overview', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'), command=self.dashb)
        Menu.grid(row=0, column=0, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=1, pady=10)

        Menu2 = Button(MenuFrame, text = 'Products', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
        Menu2.grid(row=0, column=2, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=3, pady=10)

        Menu3 = Button(MenuFrame, text = 'Sales', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'), command=self.saless)
        Menu3.grid(row=0, column=4, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=5, pady=10)

        Menu4 = Button(MenuFrame, text = 'Inventory', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
        Menu4.grid(row=0, column=6, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=7, pady=10)

        Menu5 = Button(MenuFrame, text = 'Expenses', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
        Menu5.grid(row=0, column=8, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=9, pady=10)

        Menu6 = Button(MenuFrame, text = 'Customers', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'), command=self.cus)
        Menu6.grid(row=0, column=10, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=11, pady=10)

        Menu7 = Button(MenuFrame, text = 'Employees', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
        Menu7.grid(row=0, column=12, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=13, pady=10)

        Menu9 = Button(MenuFrame, text = 'Log Out', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
        Menu9.grid(row=0, column=14, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=15, pady=10)


        Date = datetime.now()
        Menu10 = Label(MenuFrame, text=f"{Date:%A, %B, %d, %Y}", font=('roboto', 9, 'bold'), bg='green', fg='white')
        Menu10.grid(row=0, column=17, padx=5, pady=10)
        Time = strftime('%I:%M:%S')
        Menu11 = Label(MenuFrame, text=Time, font=('roboto', 9, 'bold'), bg='green', fg='white')
        Menu11.grid(row=0, column=18, pady=10)
        Menu11.after(1000, time)

        # Second Frames & Menu
        SideFrame = LabelFrame(window, height=300, width=150)
        SideFrame.pack(fill=Y, expand='no', anchor=W, padx=10, pady=40)


        SideMenu = Button(SideFrame, text='Add Product', font=('roboto', 9, 'bold'), bg='#d11c03', fg='white', bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=self.addp)
        SideMenu.grid(row=0, column=0, padx=10, pady=7)
        DivLine = Frame(SideFrame, height=2, width=100, bg='red')
        DivLine.grid(row=1, column=0, padx=10)

        SideMenu = Button(SideFrame, text='Add Customer', font=('roboto', 9, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white')
        SideMenu.grid(row=2, column=0, padx=10, pady=7)
        DivLine = Frame(SideFrame, height=2, width=100, bg='red')
        DivLine.grid(row=3, column=0, padx=10)

        SideMenu = Button(SideFrame, text='Sales Order', font=('roboto', 9, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=self.salesor)
        SideMenu.grid(row=4, column=0, padx=10, pady=7)
        DivLine = Frame(SideFrame, height=2, width=100, bg='red')
        DivLine.grid(row=5, column=0, padx=10)

        SideMenu = Button(SideFrame, text='Purchase Order', font=('roboto', 9, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white')
        SideMenu.grid(row=6, column=0, padx=10, pady=7)
        DivLine = Frame(SideFrame, height=2, width=100, bg='red')
        DivLine.grid(row=7, column=0, padx=10)

        SideMenu = Button(SideFrame, text='Generate Code', font=('roboto', 9, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white')
        SideMenu.grid(row=8, column=0, padx=10, pady=7)
        DivLine = Frame(SideFrame, height=2, width=100, bg='red')
        DivLine.grid(row=9, column=0, padx=10)

        SideMenu = Button(SideFrame, text='Add Employee', font=('roboto', 9, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white')
        SideMenu.grid(row=10, column=0, padx=10, pady=7)
        DivLine = Frame(SideFrame, height=2, width=100, bg='red')
        DivLine.grid(row=11, column=0, padx=10)

        SideMenu = Button(SideFrame, text='Payroll', font=('roboto', 9, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white')
        SideMenu.grid(row=12, column=0, padx=10, pady=7)



        # Center Frames & Labels
        AddCus = LabelFrame(window, text="Add New Customer", height=275, width=648, font=('roboto', 9, 'bold'), fg='green')
        AddCus.pack(fill=Y, expand='no')
        AddCus.place(x=140, y=75)

        Name = Label(AddCus, text="Full Name", font=('roboto', 10, 'bold'))
        Name.place(x=20, y=20)
        NameEntry = Entry(AddCus, bd=2, relief='groove', width=28, font=('roboto', 10, 'bold'))
        NameEntry.place(x=20, y=45)

        List = [
            'Ikotun',
            'Ijegun',
            'Igando',
            'Idimu',
            'Egbeda',
            'Iyana Ipaja',
            'Others'
        ]

        Location = Label(AddCus, text='Location', font=('roboto', 10, 'bold'))
        Location.place(x=250, y=20)
        Combo = ttk.Combobox(AddCus, value=List)
        Combo.current(0)
        Combo.bind('<<<ComboboxSelected>>>')
        Combo.place(x=250, y=45)

        Mobile = Label(AddCus, text="Mobile No.", font=('roboto', 10, 'bold'))
        Mobile.place(x=420, y=20)
        MobileEntry = Entry(AddCus, bd=2, relief='groove', width=20, font=('roboto', 10, 'bold'))
        MobileEntry.place(x=420, y=45)

        Date = Label(AddCus, text='Date', font=('roboto', 10, 'bold'))
        Date.place(x=20, y=90)
        DateEnt = DateEntry(AddCus, selectmode='day')
        DateEnt.place(x=20, y=115)

        Btn = Button(AddCus, text='Add Customer', font=('roboto', 9, 'bold'), bg='green', fg='white', cursor='hand2', command=AddCustomer)
        Btn.place(x=20, y=175)


    def dashb(self):
        win = Toplevel()
        dashboard.Dashboard(win)
        self.window.withdraw()
        win.deiconify()

    def saless(self):
        win = Toplevel()
        sales.Sales(win)
        self.window.withdraw()
        win.deiconify()
    
    def cus(self):
        win = Toplevel()
        customers.Customers(win)
        self.window.withdraw()
        win.deiconify()

    def addp(self):
        win = Toplevel()
        addproduct.AddProduct(win)
        self.window.withdraw()
        win.deiconify()

    def salesor(self):
        win = Toplevel()
        salesorder.SalesOrder(win)
        self.window.withdraw()
        win.deiconify()



def addcus():
    window = Tk()
    AddCustomer(window)
    window.mainloop()

if __name__ == '__main__':
    addcus()
