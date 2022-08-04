from tkinter import *
from PIL import ImageTk, Image
import signin

class Signup:
    def __init__(self, window):
        self.window = window
        width = 650
        height = 320
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenwidth()
        x = (sw/4)
        y = (sh/7)
        self.window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.window.title('SOAR ACCT | Sign In Page')
        self.window.configure(bg='#f7f3f2')
        self.window.wm_iconbitmap('FMCG.ico')
        self.window.resizable(0, 0)


        # Frames
        TitleFrame = LabelFrame(window, bg='#bd2505')
        TitleFrame.pack(fill=X, expand='no', padx=10, pady=5)

        ImageFrame = LabelFrame(window, width=50, height=40, bg='#f7f3f2')
        ImageFrame.pack(fill=X, expand='no')
        ImageFrame.place(x=40, y=100)

        SignUpFrame = LabelFrame(window, text='Sign Up Details', font=('roboto', 10, 'bold'), bg='#f7f3f2', fg='#bd2505')
        SignUpFrame.pack(fill=Y, expand='no', pady=30, padx=20, anchor=E)


        # Labels
        self.img = PhotoImage(file='./signup.png')
        ImageLabel = Label(ImageFrame, image = self.img, bg='#f7f3f2')
        ImageLabel.pack()

        TitleLabel = Label(TitleFrame, text='New Employee?, Sign Up Here!', font=('roboto', 16, 'bold'), bg='#bd2505', fg='white')
        TitleLabel.pack(fill=X, expand='yes', padx=10, pady=10)

        Username = Label(SignUpFrame, text='Username', font=('roboto', 11, 'bold'), bg='#f7f3f2', fg='#bd2505')
        Username.grid(row=1, column=0, padx=15, pady=5)

        UsernameEntry = Entry(SignUpFrame, font=('roboto', 10, 'bold'), width=22, bd=2, relief='groove')
        UsernameEntry.grid(row=1, column=1, padx=10, pady=5)


        Password = Label(SignUpFrame, text='Password', font=('roboto', 11, 'bold'), bg='#f7f3f2', fg='#bd2505')
        Password.grid(row=2, column=0, padx=15, pady=5)

        PasswordEntry = Entry(SignUpFrame, font=('roboto', 10, 'bold'), show='*', width=22, bd=2, relief='groove')
        PasswordEntry.grid(row=2, column=1, padx=10, pady=5)

        RePassword = Label(SignUpFrame, text='Re-type Password', font=('roboto', 11, 'bold'), bg='#f7f3f2', fg='#bd2505')
        RePassword.grid(row=3, column=0, padx=15, pady=5)

        RePasswordEntry = Entry(SignUpFrame, show='*', width=26, bd=2, relief='groove')
        RePasswordEntry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons

        SigninLabelButton = Button(SignUpFrame, text='Have an account? Sign In', font=('roboto', 8, 'bold', 'underline'), bg='#f7f3f2', fg='#1a3783', bd=0, cursor='hand2', command=self.signIN)
        SigninLabelButton.grid(row=4, column=0, padx=10)

        SignUpButton = Button(SignUpFrame, text='Sign Up', font=('roboto', 10, 'bold'), bg='#bd2505', fg='white')
        SignUpButton.grid(row=4, column=1, padx=10, pady=5)

    def signIN(self):
        win = Toplevel()
        signin.Signin(win)
        self.window.withdraw()
        win.deiconify()




def signUP():
    window = Tk()
    Signup(window)
    window.mainloop()


if __name__ == '__main__':
    signUP()
