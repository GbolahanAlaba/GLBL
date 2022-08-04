from tkinter import *
import sqlite3

window = Tk()
window.geometry('400x400')


db = sqlite3.connect('GLBL.db')
cursor = db.cursor()
cursor.execute('Create table "Signup" (Username varchar(100), Password varchar(100), Repassword varchar(100)')

db.commit()
db.close()

mainloop()

