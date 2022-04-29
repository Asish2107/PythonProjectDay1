import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os

# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('300x150')

l=[]
def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )
    l.extend(filenames)



# open button
open_button = ttk.Button(
    root,
    text='Open Files',
    command=select_files
)
open_button.pack(expand=True)
root.mainloop()
import copy
# a=[1,2,3,4,5,6]
# b=a.copy().s
# b[3]="abs"
# print(b)
# print(a)

# a="india is great"
# print(a.partition("i"))
# reading files
f1 = open(r"{}".format(l[0]), "r")
f2 = open(r"{}".format(l[1]), "r")
#
f= open("new.txt","w")
#
# #i=0
l=f1.readlines()
s=f2.readlines()
p=[]
q=[]
for i in l:
    c=i.replace("\n","")
    p.append(c)
for j in s:
    d=j.replace("\n","")
    q.append(d)
i=0
for line1 in range(0,len(p)):
    i=i+1
    for line2 in range(0,len(q)):
        if p[line1]!=q[line2] and line1==line2:
            f.write("{}\n".format(p[line1]))
            f.write("{}\n".format(q[line2]))
            # data = [["ABC","DEF"],[p[line1],q[line2]]]
            # print(tabulate(data, headers='firstrow', showindex='always',tablefmt='fancy_grid'))

# closing files
f1.close()
f2.close()
f.close()
os.system(r"C:\Users\Dell\Desktop\pythonProject1\new.txt")
# # A simple Python program to demonstrate
# # getpass.getpass() to read security question
# # User's password without echoing
# # import maskpass # to hide the password
# #
# # # masking the password
# # pwd = maskpass.askpass(mask="")
# # print(pwd)


