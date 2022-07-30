from cProfile import label
from tkinter import *
import sqlite3

window = Tk()
window.geometry('400x400')

def sam():
    db = sqlite3.connect('GLBL.db')
    cursor = db.cursor()
    # cursor.execute('create table SalesOrder (SID int, CID int, Product varchar(200), Quantity int, Rate int, Amount decimal, Date date)')
    cursor.execute("select * from salesorder where date = 7/6/22")
    records = cursor.fetchall()

    var.set(records)


    db.commit()
    db.close()

var = StringVar()
a = Label(window, textvariable=var)
a.pack()

sam()
mainloop()

