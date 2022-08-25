from tkinter import *

class Testing:
    def __init__(self, window):
        self.window = window
        self.window.geometry('500x300')
        self.window.title('Glory')




def test():
    window = Tk()
    Testing(window)
    mainloop()

if __name__ == '__main__':
    test()

