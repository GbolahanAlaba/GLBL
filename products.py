from itertools import count
from os import X_OK
from tkinter import *
from tkinter import ttk
from datetime import *
from time import strftime
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import sqlite3
# from functions import *
import signin
import dashboard
import products
import sales
import customers
import addproduct
import addcustomer
import addsales

class Products:
    def __init__(self, window):
        self.window = window
        width = 800
        height = 500
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        x = (sw/5)
        y = (sh/11)
        self.window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.window.title('TCP Management | Products page')
        self.window.configure(bg='#f7f3f2')
        self.window.wm_iconbitmap('FMCG.ico')
        self.window.resizable(0, 0)

        # Database
        def SalesData():
            db = sqlite3.connect('GLBL.db')
            cursor = db.cursor()
            cursor.execute('select * from products')
            records = cursor.fetchall()
            
            global count
            count = 0
            for record in records:
                SalesView.insert(parent='', index='end', iid=count, values=(record[0], 
                                    record[1], record[2], record[3])) 
                count = count + 1

            db.commit()
            db.close()



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

        Menu3 = Button(MenuFrame, text = 'Sales', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'), command=self.saless)
        Menu3.grid(row=0, column=4, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=5, pady=10)

        Menu4 = Button(MenuFrame, text = 'Customers', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'), command=self.cus)
        Menu4.grid(row=0, column=6, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=7, pady=10)

        Menu5 = Button(MenuFrame, text = 'Vendors', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
        Menu5.grid(row=0, column=8, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=9, pady=10)

        Menu6 = Button(MenuFrame, text = 'Inventory', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
        Menu6.grid(row=0, column=10, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=11, pady=10)

        Menu7 = Button(MenuFrame, text = 'Expenses', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
        Menu7.grid(row=0, column=12, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=13, pady=10)

        Menu9 = Button(MenuFrame, text = 'Log Out', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'), command=self.logout)
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



        # Center Frames & Labels
        Sales = LabelFrame(window, text="Our Products", height=275, width=648, font=('roboto', 9, 'bold'), fg='green')
        Sales.pack(fill=X, expand='no')
        Sales.place(x=130, y=75)

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
        SalesView['columns'] = ('PID', 'PRODUCT NAME', 'UNIT', 'DATE')

        SalesView.column('#0', width=0, stretch=NO)
        SalesView.column('PID', anchor=CENTER, width=70)
        SalesView.column('PRODUCT NAME', anchor=CENTER, width=140)
        SalesView.column('UNIT', anchor=CENTER, width=120)
        SalesView.column('DATE', anchor=CENTER, width=75)
        

        SalesView.heading('#0', text='', anchor=CENTER)
        SalesView.heading('PID', text='PID', anchor=CENTER)
        SalesView.heading('PRODUCT NAME', text='PRODUCT NAME', anchor=CENTER)
        SalesView.heading('UNIT', text='UNIT', anchor=CENTER)
        SalesView.heading('DATE', text='DATE', anchor=CENTER)

        LiveUp = Label(window, text='Products Live Updates', font=('roboto', 10, 'bold'), bg='#d11c03', fg='white')
        LiveUp.place(x=617, y=82)

        LiveUpF = LabelFrame(window, text='', width=190, height=226)
        LiveUpF.pack(fill=Y, expand='no', side=RIGHT)
        LiveUpF.place(x=600, y=115)

        PEX = Label(LiveUpF, text='Product: Quantity Produced', font=('roboto', 10, 'bold')).place(x=1, y=2)

        PP1 = Label(LiveUpF, text='Product 1:', font=('roboto', 10, 'bold'), fg='green').place(x=5, y=30)
        PP2 = Label(LiveUpF, text='Product 2:', font=('roboto', 10, 'bold'), fg='green').place(x=5, y=50)
        PP3 = Label(LiveUpF, text='Product 3:', font=('roboto', 10, 'bold'), fg='green').place(x=5, y=70)
        PP4 = Label(LiveUpF, text='Product 4:', font=('roboto', 10, 'bold'), fg='green').place(x=5, y=90)
        PP5 = Label(LiveUpF, text='Product 5:', font=('roboto', 10, 'bold'), fg='green').place(x=5, y=110)
        PP6 = Label(LiveUpF, text='Product 6:', font=('roboto', 10, 'bold'), fg='green').place(x=5, y=130)
        PPR1 = Label(LiveUpF, text='120000', font=('roboto', 10, 'bold')).place(x=80, y=30)
        PPR2 = Label(LiveUpF, text='130000', font=('roboto', 10, 'bold')).place(x=80, y=50)
        PPR3 = Label(LiveUpF, text='140000', font=('roboto', 10, 'bold')).place(x=80, y=70)
        PPR4 = Label(LiveUpF, text='150000', font=('roboto', 10, 'bold')).place(x=80, y=90)
        PPR5 = Label(LiveUpF, text='160000', font=('roboto', 10, 'bold')).place(x=80, y=110)
        PPR6 = Label(LiveUpF, text='170000', font=('roboto', 10, 'bold')).place(x=80, y=130)
        

        # SrcDate = DateEntry(window, selectmode='day')
        # SrcDate.place(x=140, y=370)

        # SrcBtn = Button(window, text='Search', font=('roboto', 10, 'bold'), bg='green', fg='white', cursor='hand2', command=src)
        # SrcBtn.place(x=260, y=365)


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

    def addc(self):
        win = Toplevel()
        addcustomer.AddCustomer(win)
        self.window.withdraw()
        win.deiconify()

    def adds(self):
        win = Toplevel()
        addsales.AddSales(win)
        self.window.withdraw()
        win.deiconify()
    
    def logout(self):
        win = Toplevel()
        signin.Signin(win)
        self.window.withdraw()
        win.deiconify()

def products():
    window = Tk()
    Products(window)
    window.mainloop()

if __name__ == '__main__':
    products()