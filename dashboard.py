import sqlite3
from tkinter import *
from datetime import *
import tkinter as tk
from time import strftime
from PIL import ImageTk, Image
import addproduct


class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.geometry('800x500')
        self.window.title('SOAR ACCT (VERSION 1.28)')
        self.window.configure(bg='#f7f3f2')
        self.window.wm_iconbitmap('FMCG.ico')
        self.window.resizable(0, 0)
        

# Inflow Functions
        def InflowD():
            a = "N1,000,000"
            InfVar.set(a)


        def InflowW():
            a = "N7,000,000"
            InfVar.set(a)


        def InflowM():
            a = "N30,000,000"
            InfVar.set(a)

        # Outflow Functions
        def OutflowD():
            a = "N96,500"
            OutfVar.set(a)


        def OutflowW():
            a = "N680,000"
            OutfVar.set(a)


        def OutflowM():
            a = "N2,850,500"
            OutfVar.set(a)

        # Expense Functions
        def ExpD():
            a = "N22,000"
            ExpVar.set(a)


        def ExpW():
            a = "N129,000"
            ExpVar.set(a)


        def ExpM():
            a = "N550,000"
            ExpVar.set(a)


        # Balance Functions
        def BalD():
            a = "N882,000"
            BalVar.set(a)


        def BalW():
            a = "N6,191,000"
            BalVar.set(a)


        def BalM():
            a = "N26,599,500"
            BalVar.set(a)

        def SWSum():
            db = sqlite3.connect('GLBL.db')
            cursor = db.cursor()
            cursor.execute("select sum(quantity) from salesorder where product = 'Sachet Water'")
            records = cursor.fetchall()

            count = 0
            for record in records:
                value = record[0]
                count = count + 1
            
            SWSumVar.set(value)

            db.commit()
            db.close()


        def BWSum():
            db = sqlite3.connect('GLBL.db')
            cursor = db.cursor()
            cursor.execute("select sum(quantity) from salesorder where product = 'Bottled Water'")
            records = cursor.fetchall()

            count = 0
            for record in records:
                value = record[0]
                count = count + 1
            
            BWSumVar.set(value)

            db.commit()
            db.close()


        def DSSum():
            db = sqlite3.connect('GLBL.db')
            cursor = db.cursor()
            cursor.execute("select sum(quantity) from salesorder where product = 'Dee Speed'")
            records = cursor.fetchall()

            count = 0
            for record in records:
                value = record[0]
                count = count + 1
            
            DSSumVar.set(value)

            db.commit()
            db.close()
            

        # Variables
        InfVar = IntVar()
        OutfVar = IntVar()
        ExpVar = IntVar()
        BalVar = IntVar()
        SWSumVar = IntVar()
        BWSumVar = IntVar()
        DSSumVar = IntVar()


        # Top Menu Functions
        def Sales():
            window.destroy()
            import sales

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
            

        # First Frame & Menus
        MenuFrame = Frame(self.window)
        MenuFrame.pack(fill=X, expand='no')

        Menu = Button(MenuFrame, text = 'Overview', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
        Menu.grid(row=0, column=0, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=1, pady=10)

        Menu2 = Button(MenuFrame, text = 'Products', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'))
        Menu2.grid(row=0, column=2, padx=5, pady=10)
        DivLine = Frame(MenuFrame, height=15, width=1, bg='red')
        DivLine.grid(row=0,column=3, pady=10)

        Menu3 = Button(MenuFrame, text = 'Sales', bd=0, cursor='hand2', activebackground='green', activeforeground='white', font=('roboto', 9, 'bold'), command=Sales)
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


        # Second Frames

        Frame1 = LabelFrame(window, height=120, width=800)
        Frame1.pack(fill=X, expand='no', padx=10, pady=10)

        Inflow = LabelFrame(Frame1, text='Inflow', height=150, width=150, font=('roboto', 9, 'bold'), fg='green')
        Inflow.pack  (fill=Y, expand='no')
        Inflow.place(x=25, y=5)

        InfV = Label(Inflow, textvariable=InfVar, font=('roboto', 11, 'bold'))
        InfV.grid(row=0, column=0, padx=10, pady=10)
        DivLine = Frame(Inflow, height=2, width=150, bg='green')
        DivLine.grid(row=1,column=0, pady=1)

        InfVD = Button(Frame1, text='TDI', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='green', activeforeground='white', command=InflowD)
        InfVD.place(x=32, y=70)
        DivLine = Frame(Frame1, height=15, width=1, bg='red')
        DivLine.place(x=70, y=75)
        InfVW = Button(Frame1, text='TWI', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='green', activeforeground='white', command=InflowW)
        InfVW.place(x=80, y=70)
        DivLine = Frame(Frame1, height=15, width=1, bg='red')
        DivLine.place(x=124, y=75)
        InfVM = Button(Frame1, text='TMI', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='green', activeforeground='white', command=InflowM)
        InfVM.place(x=133, y=70)

        # Seperator Line 1
        DivLine = Frame(Frame1, height=100, width=4, bg='green')
        DivLine.place(x=190, y=5)

        # Ouflow block
        Outflow = LabelFrame(Frame1, text='Outflow', height=150, width=150, font=('roboto', 9, 'bold'), fg='black')
        Outflow.pack  (fill=Y, expand='no')
        Outflow.place(x=205, y=5)

        OutfV = Label(Outflow, textvariable=OutfVar, font=('roboto', 11, 'bold'))
        OutfV.grid(row=0, column=0, padx=10, pady=10)
        DivLine = Frame(Outflow, height=2, width=150, bg='black')
        DivLine.grid(row=1,column=0, pady=1)

        OutfVD = Button(Frame1, text='TDO', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='black', activeforeground='white', command=OutflowD)
        OutfVD.place(x=212, y=70)
        DivLine = Frame(Frame1, height=15, width=1, bg='red')
        DivLine.place(x=253, y=75)
        OutfVW = Button(Frame1, text='TWO', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='black', activeforeground='white', command=OutflowW)
        OutfVW.place(x=260, y=70)
        DivLine = Frame(Frame1, height=15, width=1, bg='red')
        DivLine.place(x=305, y=75)
        OutfVM = Button(Frame1, text='TMO', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='black', activeforeground='white', command=OutflowM)
        OutfVM.place(x=313, y=70)


        # Seperator Line 2
        DivLine = Frame(Frame1, height=100, width=4, bg='green')
        DivLine.place(x=370, y=5)

        # Expense Block
        Expense = LabelFrame(Frame1, text='Expense', height=150, width=150, font=('roboto', 9, 'bold'), fg='#d11c03')
        Expense.pack  (fill=Y, expand='no')
        Expense.place(x=385, y=5)

        ExpV = Label(Expense, textvariable=ExpVar, font=('roboto', 11, 'bold'))
        ExpV.grid(row=0, column=0, padx=10, pady=10)
        DivLine = Frame(Expense, height=2, width=150, bg='#d11c03')
        DivLine.grid(row=1,column=0, pady=1)

        ExpVD = Button(Frame1, text='TDE', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=ExpD)
        ExpVD.place(x=393, y=70)
        DivLine = Frame(Frame1, height=15, width=1, bg='red')
        DivLine.place(x=433, y=75)
        ExpVW = Button(Frame1, text='TWE', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=ExpW)
        ExpVW.place(x=443, y=70)
        DivLine = Frame(Frame1, height=15, width=1, bg='red')
        DivLine.place(x=488, y=75)
        ExpVM = Button(Frame1, text='TME', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=ExpM)
        ExpVM.place(x=493, y=70)

        # Seperator Line 3
        DivLine = Frame(Frame1, height=100, width=4, bg='green')
        DivLine.place(x=550, y=5)

        # Balance Block
        Balance = LabelFrame(Frame1, text='Balance', height=150, width=150, font=('roboto', 9, 'bold'), fg='green')
        Balance.pack  (fill=Y, expand='yes')
        Balance.place(x=585, y=5)

        BalV = Label(Balance, textvariable=BalVar, font=('roboto', 13, 'bold'), fg='green')
        BalV.grid(row=0, column=0, padx=10, pady=10)
        DivLine = Frame(Balance, height=2, width=150, bg='green')
        DivLine.grid(row=1,column=0, pady=1)

        BalVD = Button(Frame1, text='TDB', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='green', activeforeground='white', command=BalD)
        BalVD.place(x=592, y=70)
        DivLine = Frame(Frame1, height=15, width=1, bg='red')
        DivLine.place(x=632, y=75)
        BalVW = Button(Frame1, text='TWB', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='green', activeforeground='white', command=BalW)
        BalVW.place(x=639, y=70)
        DivLine = Frame(Frame1, height=15, width=1, bg='red')
        DivLine.place(x=684, y=75)
        BalVM = Button(Frame1, text='TMB', font=('roboto', 10, 'bold'), bd=0, cursor='hand2', activebackground='green', activeforeground='white', command=BalM)
        BalVM.place(x=689, y=70)

        # Third Frame
        SideFrame = LabelFrame(window, height=300, width=150)
        SideFrame.pack(fill=Y, expand='no', anchor=W, padx=10)


        SideMenu = Button(SideFrame, text='Add Product', font=('roboto', 9, 'bold'), bg='#d11c03', fg='white', bd=0, cursor='hand2', activebackground='#d11c03', activeforeground='white', command=self.addp)
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
        Prod = LabelFrame(window, text="Today's Prod History", height=65, width=648, font=('roboto', 9, 'bold'), fg='green')
        Prod.pack(fill=Y, expand='no')
        Prod.place(x=140, y=176)

        SWP = Label(Prod, text="Sachet Water:", font=('roboto', 10, 'bold'))
        SWP.place(x=10, y=10)
        SWPV = Label(Prod, text='(1,700)', font=('roboto', 10, 'bold'), fg='#d11c03')
        SWPV.place(x=110, y=10)

        BWP = Label(Prod, text="Bottle Water:", font=('roboto', 10, 'bold'))
        BWP.place(x=216, y=10)
        BWPV = Label(Prod, text='(4,700)', font=('roboto', 10, 'bold'), fg='#d11c03')
        BWPV.place(x=316, y=10)

        DSP = Label(Prod, text="Dee Speed:", font=('roboto', 10, 'bold'))
        DSP.place(x=432, y=10)
        DSPV = Label(Prod, text='(2,700)', font=('roboto', 10, 'bold'), fg='#d11c03')
        DSPV.place(x=532, y=10)

        Sales = LabelFrame(window, text="Today's Sales History", height=65, width=648, font=('roboto', 9, 'bold'), fg='green')
        Sales.pack(fill=Y, expand='no')
        Sales.place(x=140, y=251)

        SWS = Label(Sales, text="Sachet Water:", font=('roboto', 10, 'bold'))
        SWS.place(x=10, y=10)
        SWSV = Label(Sales, textvariable=SWSumVar, font=('roboto', 10, 'bold'), fg='green')
        SWSV.place(x=110, y=10)

        BWS = Label(Sales, text="Bottle Water:", font=('roboto', 10, 'bold'))
        BWS.place(x=216, y=10)
        BWSV = Label(Sales, textvariable=BWSumVar, font=('roboto', 10, 'bold'), fg='green')
        BWSV.place(x=316, y=10)

        DSS = Label(Sales, text="Dee Speed:", font=('roboto', 10, 'bold'))
        DSS.place(x=432, y=10)
        DSSV = Label(Sales, textvariable=DSSumVar, font=('roboto', 10, 'bold'), fg='green')
        DSSV.place(x=532, y=10)

        # Footer Frames
        Footer1 = LabelFrame(window, text='', height=120, width=152, font=('roboto', 9, 'bold'), fg='#d11c03')
        Footer1.pack(fill=Y, expand='yes')
        Footer1.place(x=140, y=326)
        img1 = ImageTk.PhotoImage(Image.open("SachetWater.jpg"))
        ImageLabel = Label(Footer1, image = img1)
        ImageLabel.pack()


        Footer2 = LabelFrame(window, text='', height=120, width=152, font=('roboto', 9, 'bold'), fg='#d11c03')
        Footer2.pack(fill=Y, expand='yes')
        Footer2.place(x=302, y=326)
        img2 = ImageTk.PhotoImage(Image.open("SachetWater.jpg"))
        ImageLabel = Label(Footer2, image = img2)
        ImageLabel.pack()


        Footer3 = LabelFrame(window, text='', height=120, width=152, font=('roboto', 9, 'bold'), fg='#d11c03')
        Footer3.pack(fill=Y, expand='yes')
        Footer3.place(x=464, y=326)
        img3 = ImageTk.PhotoImage(Image.open("SachetWater.jpg"))
        ImageLabel = Label(Footer3, image = img3)
        ImageLabel.pack()


        Footer4 = LabelFrame(window, text='', height=120, width=152, font=('roboto', 9, 'bold'), fg='#d11c03')
        Footer4.pack(fill=Y, expand='yes')
        Footer4.place(x=625, y=326)
        img4 = ImageTk.PhotoImage(Image.open("SachetWater.jpg"))
        ImageLabel = Label(Footer4, image = img4)
        ImageLabel.pack()




        InflowD()
        OutflowD()
        ExpD()
        BalD()
        SWSum()
        BWSum()
        DSSum()


    def addp(self):
        win = Toplevel()
        addproduct.AddProduct(win)
        self.window.withdraw()
        win.deiconify()


def dash():
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__ == '__main__':
    dash()
# mainloop()