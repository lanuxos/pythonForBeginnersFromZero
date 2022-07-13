# ep4
# Basic input
# names = []
# for i in range(5):
#     data = input('Please type your name: ')
#     names.append(data)
# print(names)

# PyAutoGUI
from tkinter import *
from tkinter import ttk
import pyautogui as pg
import webbrowser

root = Tk()
root.geometry('500x300')
root.title('Calendar Auto Click')

def Calendar():
    pg.click(1541, 884)

def Google():
    webbrowser.open('https://www.google.com')

b1 = Button(root, text='Calendar', command=Calendar)
b1.pack(ipadx=5, ipady=5)

b2 = ttk.Button(root, text='Modern Calendar', command=Calendar)
b2.pack(ipadx=5, ipady=5)

b3 = ttk.Button(root, text='Google', command=Google)
b3.pack(ipadx=5, ipady=5)

root.mainloop()