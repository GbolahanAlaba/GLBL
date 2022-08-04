from tkinter import *

class Signin:
    def __init__(self, window):
        self.window = window
        width = 550
        height = 310
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenwidth()
        x = (sw/3)
        y = (sh/7)
        self.window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.window.title('SOAR ACCT | Sign In Page')
        self.window.configure(bg='#f7f3f2')
        self.window.wm_iconbitmap('FMCG.ico')
        self.window.resizable(0, 0)



def signin():
    window = Tk()
    Signin(window)
    window.mainloop()

if __name__ == '__main__':
    signin()

        