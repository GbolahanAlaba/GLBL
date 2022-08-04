from tkinter import *
from PIL import ImageTk, Image

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



        def clear():
            UsernameEntry.delete(0, END)
            PasswordEntry.delete(0, END)

        TitleFrame = LabelFrame(window, bg='#bd2505')
        TitleFrame.pack(fill=X, expand='no', padx=10, pady=5)

        ImageFrame = Frame(window, width=50, height=50, bg='#f7f3f2')
        ImageFrame.pack(fill=X, expand='no')
        ImageFrame.place(x=40, y=100)

        SigninFrame = LabelFrame(window,
                                text='Sign In Details',
                                font=('roboto', 10, 'bold'),
                                bg='#f7f3f2',
                                fg='#bd2505')
        SigninFrame.pack(fill=Y, expand='yes', pady=30, padx=20, anchor=E)

        # Labels
        img = ImageTk.PhotoImage(Image.open("signin.png"))
        ImageLabel = Label(ImageFrame, image = img, bg='#f7f3f2')
        ImageLabel.pack()

        TitleLabel = Label(TitleFrame,
                        text='Welcome, Sign into your account',
                        font=('roboto', 16, 'bold'),
                        bg='#bd2505',
                        fg='white')
        TitleLabel.pack(fill=X, expand='yes', padx=10, pady=10)

        # Login Label & Entries
        Username = Label(SigninFrame,
                        text='Username',
                        font=('roboto', 11, 'bold'),
                        bg='#f7f3f2',
                        fg='#bd2505')
        Username.grid(row=0, column=0, padx=20, pady=10)

        UsernameEntry = Entry(SigninFrame,
                        font=('roboto', 10, 'bold'),
                        width=22,
                        bd=2,
                        relief='groove')
        UsernameEntry.grid(row=0, column=1, padx=10, pady=10)
        # UserEntry.insert(1, 'Enter Your Username')


        Password = Label(SigninFrame,
                        text='Password',
                        font=('roboto', 11, 'bold'),
                        bg='#f7f3f2',
                        fg='#bd2505')
        Password.grid(row=1, column=0, padx=20, pady=10)


        PasswordEntry = Entry(SigninFrame,
                        font=('roboto', 10, 'bold'),
                        show='*',
                        width=22,
                        bd=2,
                        relief='groove')
        PasswordEntry.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        ChkButton = Checkbutton(SigninFrame,
                                text='Remember Me',
                                bg='#f7f3f2',
                                cursor='hand2')
        ChkButton.grid(row=2, column=0, pady=5)


        SigninButton = Button(SigninFrame,
                            text='Sign in',
                            font=('roboto', 10, 'bold'),
                            bg='#bd2505',
                            fg='white',
                            command=signin)
        SigninButton.place(x=150, y=93)


        ClearButton = Button(SigninFrame,
                            text='Clear',
                            font=('roboto', 10, 'bold'),
                            bg='#bd2505', fg='white',
                            command=clear)
        ClearButton.place(x=230, y=93)


        ForgetPwLabel = Button(SigninFrame,
                        text='Forget Password?',
                        font=('roboto', 8, 'bold', 'underline'),
                        bg='#f7f3f2',
                        fg='#1a3783',
                        bd=0, cursor='hand2')
        ForgetPwLabel.place(x=10, y=130)


        SignupLabel = Button(SigninFrame,
                            text='Create Account',
                            font=('roboto', 8, 'bold', 'underline'),
                            bg='#f7f3f2',
                            fg='#1a3783',
                            bd=0, cursor='hand2')
        SignupLabel.place(x=130, y=130)



def signin():
    window = Tk()
    Signin(window)
    window.mainloop()

if __name__ == '__main__':
    signin()

        