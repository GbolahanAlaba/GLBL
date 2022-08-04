from cProfile import label
from tkinter import *

window = Tk()
window.geometry('1336x768')

scrwidth = window.winfo_screenwidth()
scrheight = window.winfo_screenheight()

lab = Label(window, text=scrwidth, font=('roboto', 20,'bold'))
lab.grid(row=0, column=0, padx=20, pady=50)
lab2 = Label(window, text=scrheight, font=('roboto', 20,'bold'))
lab2.grid(row=1, column=0, padx=20, pady=60)

mainloop()

# class profile:

#     def __init__(self, name, age, country):
#         self.name = 'Gbolahan'
#         self.age = 28
#         self.country = 'Nigeria'
    
#     def update(self):
#         self.name = 'Shola'
#         self.age = 30
#         self.country = 'Ghana'
  
# p = profile()
# p.update()

# print(p.country)


