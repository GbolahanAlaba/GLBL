from email import message
from tkinter import *
from tkinter import ttk
from datetime import *
from time import strftime
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import messagebox
import sqlite3
import dashboard
import sales
import customers
import addcustomer
import salesorder



class AddProduct:
    def __init__(self, window):
        self.window = window
        width = 800
        height = 500
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenwidth()
        x = (sw/5)
        y = (sh/11)
        self.window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.window.title('TCP Management | Add Product Page')
        self.window.configure(bg='#f7f3f2')
        self.window.wm_iconbitmap('FMCG.ico')
        self.window.resizable(0, 0)


        # Database
        def AddProductDB():
            if not PNameEntry.get() or not Combo.get() or not DateEnt.get():
                messagebox.showerror('Invalid!', 'Field(s) cannot\nbe empty')

            else:
                db = sqlite3.connect('GLBL.db')
                cursor = db.cursor()
                Val = [(PNameEntry.get()), (Combo.get()), (DateEnt.get())]
                cursor.executemany('Insert into products (ProductName, Unit, Date) values(?, ?, ?)', [Val])

                db.commit()
                db.close()

                PNameEntry.delete(0, END)

                messagebox.showinfo('Great!', 'Product added')
            


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


        SideMenu = Button(SideFrame, text='Add Product', font=('roboto', 9, 'bold'), bg='#d11c03', fg='white', bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white')
        SideMenu.grid(row=0, column=0, padx=10, pady=7)
        DivLine = Frame(SideFrame, height=2, width=100, bg='red')
        DivLine.grid(row=1, column=0, padx=10)

        SideMenu = Button(SideFrame, text='Add Customer', font=('roboto', 9, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=self.addc)
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
        AddProd = LabelFrame(window, text="Add New Product", height=275, width=648, font=('roboto', 9, 'bold'), fg='green')
        AddProd.pack(fill=Y, expand='no')
        AddProd.place(x=140, y=75)

        PName = Label(AddProd, text='Product Name', font=('roboto', 10, 'bold'))
        PName.place(x=20, y=20)
        PNameEntry = Entry(AddProd, bd=2, relief='groove', width=28, font=('roboto', 10, 'bold'))
        PNameEntry.place(x=20, y=45)


        List = [
            'Distilled Water',
            'Wine Spirit'
        ]


        Unit = Label(AddProd, text='Unit', font=('roboto', 10, 'bold'))
        Unit.place(x=250, y=20)
        Combo = ttk.Combobox(AddProd, value=List)
        Combo.current(0)
        Combo.bind('<<<ComboboxSelected>>>')
        Combo.place(x=250, y=45)

        Date = Label(AddProd, text='Date', font=('roboto', 10, 'bold'))
        Date.place(x=20, y=90)
        DateEnt = DateEntry(AddProd, selectmode='day')
        DateEnt.place(x=20, y=115)

        Btn = Button(AddProd, text='Add Product', font=('roboto', 9, 'bold'), bg='green', fg='white', cursor='hand2', command=AddProductDB)
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

    def addc(self):
        win = Toplevel()
        addcustomer.AddCustomer(win)
        self.window.withdraw()
        win.deiconify()

    def salesor(self):
        win = Toplevel()
        salesorder.SalesOrder(win)
        self.window.withdraw()
        win.deiconify()


def addpro():
    window = Tk()
    AddProduct(window)
    window.mainloop()

if __name__ == '__main__':
    addpro()

# mainloop()
