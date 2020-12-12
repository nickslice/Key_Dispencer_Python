from tkinter import *
from tkinter import messagebox as mb
import tkinter.ttk as ttk
import os
from datetime import datetime

root = Tk()
root.geometry('300x300')


options = ttk.Combobox(root, values=['batch_1', 'batch_2'])
get_key_but = Button(root, text='Get Key', width=13)
exit_but = Button(root, text='Cancel', width=13)
keys_ = Text(root, width=27, height=7)

options.current(0)


def get_key(event):
    with open(options.get() + '.txt', 'r') as out, open(options.get() + '_used_.txt', 'a') as used:
        content = out.read()
        if content.replace('\n', '') != '':
            lines = content.split('\n')
            key = lines[0] + '\n'
            keys_.insert(1.0, key)
            used.write(key + os.getlogin() + ' - ' + str(datetime.now()) + '\n\n')
        else:
            mb.showerror('Error', 'There are no keys in ' + options.get() + '.txt!')

    with open(options.get() + '.txt', 'w') as unused:
        if content.replace('\n', '') != '':
            del lines[0]
            for line in lines:
                unused.write(line + '\n')
        else:
            pass

get_key_but.bind('<Button-1>', get_key)


Label(text='Key batch: ').grid(column=0, row=0, padx=10, pady=10, sticky=W)
options.grid(column=0, row=0, padx=100, pady=10, sticky=W + E)
get_key_but.grid(column=0, row=1, padx=10, pady=0, sticky=W)
exit_but.grid(column=0, row=1, padx=100, pady=0, sticky=E)
keys_.grid(column=0, row=2, padx=10, pady=40, sticky=W, columnspan=2)

root.mainloop()
