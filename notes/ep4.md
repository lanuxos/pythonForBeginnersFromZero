# Python for beginners from zero
# ep.4

# list - 001645
```
list = []
list.append()
list.insert(INDEX, VALUE)
list.pop()
list.pop(INDEX)
list.remove(VALUE)
list.sort()
list.sort(reverse=True)
sorted(list) # temporary sort w/o changing the list order
sorted(list, reverse=True)
list.reverse()
list.copy()
list.extend()
list[INDEX]=VALUE
```
# tuple - 004545
```
tuple = ()
tuple.count(VALUE)
tuple.index()
```
# dictionary - 010505
```
dict = {}
dict[KEY] = VALUE
dict[KEY]
dict.get(KEY)
```
# Install PyAutoGUI - 022145
`pip install pyautogui`
# Basic GUI - 022620
```
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
```