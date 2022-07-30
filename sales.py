from itertools import count
from sre_parse import expand_template
from tkinter import *
from tkinter import ttk
from datetime import *
from time import strftime
from turtle import right
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import sqlite3


window = Tk()
window.geometry('800x500')
window.title('SOAR ACCT (VERSION 1.28)')
window.configure(bg='#f7f3f2')
window.wm_iconbitmap('FMCG.ico')
window.resizable(height=FALSE, width=FALSE)

# Database
def SalesData():
    db = sqlite3.connect('GLBL.db')
    cursor = db.cursor()
    cursor.execute('select salesorder.sid, customers.name, salesorder.product, salesorder.quantity, salesorder.rate, salesorder.amount, salesorder.date from salesorder inner join customers on salesorder.CID = customers.CID')
    records = cursor.fetchall()
    
    global count
    count = 0
    for record in records:
        SalesView.insert(parent='', index='end', iid=count, values=(record[0], 
                            record[1], record[2], record[3], record[4], record[5], record[6])) 
        count = count + 1

    db.commit()
    db.close()


# def src():
#     db = sqlite3.connect('GLBL.db')
#     cursor = db.cursor()
#     val = SrcDate.get()
#     cursor.execute('select * from salesorder where date = ?', [val])
#     records = cursor.fetchall()
#     global count
#     count = 0
#     for record in records:
#         SalesView.insert(parent='', index='end', iid='count', values=(record[0], record[1],
#                             record[2], record[3], record[4], record[5], record[6]))
#         count = count + 1

    
    # db.commit()
    # db.close()


def Sum():
    db = sqlite3.connect('GLBL.db')
    cursor = db.cursor()
    cursor.execute('select sum(amount) from salesorder')
    records = cursor.fetchall()

    count = 0
    for record in records:
        value = record[0]
        count = count + 1
    currency = "₦{:,.2f}".format(value)
    SumVar.set(currency)

    db.commit()
    db.close()


# Top Menu Functions
def Overview():
    window.destroy()
    import dashboard

# Side Menu Functions
def AddProduct():
    window.destroy()
    import addproduct

def AddCustomer():
    window.destroy()
    import addcustomer

def SalesOrder():
    window.destroy()
    import salesorder



SumVar = IntVar()

# First Frame & Menu
MenuFrame = Frame(window)
MenuFrame.pack(fill=X, expand='no')

Menu = Button(MenuFrame, text = 'Overview', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'), command=Overview)
Menu.grid(row=0, column=0, padx=5, pady=10)
DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
DivLine.grid(row=0,column=1, pady=10)

Menu2 = Button(MenuFrame, text = 'Products', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
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

Menu6 = Button(MenuFrame, text = 'Customers', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
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


SideMenu = Button(SideFrame, text='Add Product', font=('roboto', 9, 'bold'), bg='#d11c03', fg='white', bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=AddProduct)
SideMenu.grid(row=0, column=0, padx=10, pady=7)
DivLine = Frame(SideFrame, height=2, width=100, bg='red')
DivLine.grid(row=1, column=0, padx=10)

SideMenu = Button(SideFrame, text='Add Customer', font=('roboto', 9, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=AddCustomer)
SideMenu.grid(row=2, column=0, padx=10, pady=7)
DivLine = Frame(SideFrame, height=2, width=100, bg='red')
DivLine.grid(row=3, column=0, padx=10)

SideMenu = Button(SideFrame, text='Sales Order', font=('roboto', 9, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=SalesOrder)
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
Sales = LabelFrame(window, text="New Sales Order", height=275, width=648, font=('roboto', 9, 'bold'), fg='green')
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
mainloop()
