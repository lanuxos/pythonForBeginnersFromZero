# Python for beginners from zero
# ep.5

# Github - 001200
# Install songline - 011250
# Line Notify - 011510
```
from songline import Sendline
token = ''
messenger = Senline(token)
messenger.sentext('Hello World')
```
# Expression/Operator - 014930
# Python GUI w/ try/except - 020930
```
from tkinter import *
from tkinter import ttk, messagebox
root = Tk()
root.geometry('500x300')
root.title('Calculator')

def Calc():
    try:
        q = float(quantity.get())
        c = q * 50
        messagebox.showinfo('Total', f'Total value is {c}')
        quantity.set('')
        e1.focus()
    except:
        messagebox.showwarning('Error', 'Only number accept')
        quantity.set('')

photo = PhotoImage(file='../../../komkarnngen.png').subsample(5)
bg = Label(root, image=photo)
bg.pack()

l = Label(root, text='Please input your value', font=('Times New Roman', 20))
l.pack(ipadx=5, ipady=5)

quantity = StringVar()
e1 = ttk.Entry(root, textvariable=quantity, font=('Times New Roman', 15))
e1.pack(ipadx=5, ipady=5)

b = ttk.Button(root, text='calc', command=Calc)
b.pack(ipadx=5, ipady=5)


root.mainloop()
```