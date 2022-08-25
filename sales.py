from itertools import count
from tkinter import *
from tkinter import ttk
from datetime import *
from time import strftime
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import sqlite3
import signin
import dashboard
import products
import customers
import addsales
import searchsales

class Sales:
    def __init__(self, window):
        self.window = window
        width = 800
        height = 500
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenwidth()
        x = (sw/5)
        y = (sh/11)
        self.window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.window.title('TCP Management | Sales page')
        self.window.configure(bg='#f7f3f2')
        self.window.wm_iconbitmap('FMCG.ico')
        self.window.resizable(0, 0)

        # Database
        def SalesData():
            db = sqlite3.connect('GLBL.db')
            cursor = db.cursor()
            cursor.execute('select sales.sid, customers.name, sales.product, sales.quantity, sales.rate, sales.amount, sales.date from sales inner join customers on sales.CID = customers.CID')
            records = cursor.fetchall()
            
            global count
            count = 0
            for record in records:
                SalesView.insert(parent='', index='end', iid=count, values=(record[0], 
                                    record[1], record[2], record[3], record[4], record[5], record[6])) 
                count = count + 1

            db.commit()
            db.close()


        def Sum():
            db = sqlite3.connect('GLBL.db')
            cursor = db.cursor()
            cursor.execute('select sum(amount) from sales')
            records = cursor.fetchall()

            count = 0
            for record in records:
                value = record[0]
                count = count + 1
            currency = "₦{:,.2f}".format(value)
            SumVar.set(currency)

            db.commit()
            db.close()



        SumVar = IntVar()

        # First Frame & Menu
        MenuFrame = Frame(window)
        MenuFrame.pack(fill=X, expand='no')

        Menu = Button(MenuFrame, text = 'Overview', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'), command=self.dashb)
        Menu.grid(row=0, column=0, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=1, pady=10)

        Menu2 = Button(MenuFrame, text = 'Products', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'), command=self.prod)
        Menu2.grid(row=0, column=2, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=3, pady=10)

        Menu3 = Button(MenuFrame, text = 'Sales', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
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

        Menu9 = Button(MenuFrame, text = 'Log Out', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'),command=self.logout)
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


        SideMenu = Button(SideFrame, text='Add Sale', font=('roboto', 9, 'bold'), bg='#d11c03', fg='white', bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=self.adds)
        SideMenu.grid(row=0, column=0, padx=10, pady=7)
        DivLine = Frame(SideFrame, height=2, width=100, bg='red')
        DivLine.grid(row=1, column=0, padx=10)

        SideMenu = Button(SideFrame, text='Search By Date', font=('roboto', 9, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=self.searchsale)
        SideMenu.grid(row=2, column=0, padx=10, pady=7)





        # Center Frames & Labels
        Sales = LabelFrame(window, text="All Time Sales", height=275, width=648, font=('roboto', 9, 'bold'), fg='green')
        Sales.pack(fill=Y, expand='no')
        Sales.place(x=140, y=75)

        Style = ttk.Style()
        Style.theme_use('clam')
        Style.configure('Treeview',
                        font=('roboto', 10, 'bold'),
                        background='#f7f3f2',
                        rowheight=20,
                        activebackground="#81C44C")

        Style.map('Treeview', background=[('selected', 'green')])
        # #bd2505

        Tscroll = Scrollbar(Sales, orient='vertical')
        Tscroll.pack(side=RIGHT, fill=Y)

        SalesView = ttk.Treeview(Sales, yscrollcommand=Tscroll.set, selectmode='extended')
        SalesView.pack(pady=10, padx=10)
        Tscroll.configure(command=SalesView.yview)
        SalesView['columns'] = ('SID', 'STORE', 'PRODUCT', 'QUANTITY', 'RATE', 'AMOUNT', 'DATE')

        SalesView.column('#0', width=0, stretch=NO)
        SalesView.column('SID', anchor=CENTER, width=70)
        SalesView.column('STORE', anchor=CENTER, width=170)
        SalesView.column('PRODUCT', anchor=CENTER, width=100)
        SalesView.column('QUANTITY', anchor=CENTER, width=55)
        SalesView.column('RATE', anchor=CENTER, width=50)
        SalesView.column('AMOUNT', anchor=CENTER, width=90)
        SalesView.column('DATE', anchor=CENTER, width=70)

        SalesView.heading('#0', text='', anchor=CENTER)
        SalesView.heading('SID', text='SID', anchor=CENTER)
        SalesView.heading('STORE', text='CUSTOMER', anchor=CENTER)
        SalesView.heading('PRODUCT', text='PRODUCT', anchor=CENTER)
        SalesView.heading('QUANTITY', text='QTY', anchor=CENTER)
        SalesView.heading('RATE', text='RATE', anchor=CENTER)
        SalesView.heading('AMOUNT', text='AMOUNT', anchor=CENTER)
        SalesView.heading('DATE', text='DATE', anchor=CENTER)


        TotalF = LabelFrame(window, width=260, height=40)
        TotalF.pack(expand='no', fill=Y)
        TotalF.place(x=500, y=360)

        Total = Label(TotalF, text='Total:', font=('roboto', 15, 'bold'), fg='green' )
        Total.place(x=10, y=4)

        TotalSum = Label(TotalF, textvariable=SumVar, font=('roboto', 15, 'bold'), fg='green' )
        TotalSum.place(x=90, y=4)

        # SrcDate = DateEntry(window, selectmode='day')
        # SrcDate.place(x=140, y=370)

        # SrcBtn = Button(window, text='Search', font=('roboto', 10, 'bold'), bg='green', fg='white', cursor='hand2', command=src)
        # SrcBtn.place(x=260, y=365)


        Sum()
        SalesData()


    def dashb(self):
        win = Toplevel()
        dashboard.Dashboard(win)
        self.window.withdraw()
        win.deiconify()

    def prod(self):
        win = Toplevel()
        products.Products(win)
        self.window.withdraw()
        win.deiconify()

    def cus(self):
        win = Toplevel()
        customers.Customers(win)
        self.window.withdraw()
        win.deiconify()


    def adds(self):
        win = Toplevel()
        addsales.AddSales(win)
        self.window.withdraw()
        win.deiconify()
    
    def searchsale(self):
        win = Toplevel()
        searchsales.SearchSales(win)
        self.window.withdraw()
        win.deiconify()
    
    def logout(self):
        win = Toplevel()
        signin.Signin(win)
        self.window.withdraw()
        win.deiconify()

def sales():
    window = Tk()
    Sales(window)
    window.mainloop()

if __name__ == '__main__':
    sales()