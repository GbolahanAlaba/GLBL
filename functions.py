from tkinter import *
import sqlite3
from tkinter import *
from datetime import *
import tkinter as tk
from time import strftime
from PIL import ImageTk, Image

import signin
import signup
import dashboard
import products
import sales
import customers
import addsales
import addproduct
import addcustomer


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

def salesor(self):
    win = Toplevel()
    addsales.SalesOrder(win)
    self.window.withdraw()
    win.deiconify()

def logout(self):
    win = Toplevel()
    signin.Signin(win)
    self.window.withdraw()
    win.deiconify()
