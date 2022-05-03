from tkinter import *

# Create the root window
# with specified size and title
root = Tk()
root.title("Quick Access")
root.geometry("450x300")
# def main_page():
#     global button
#     global label1
#     label1 = Label(root, text="Click on the button to open")
#     button = Button(root, text="DB OPERATION", command=open_Toplevel1)
#
#     label1.pack()
#
#     # position the button
#     button.place(x=175, y=125)
#     root.mainloop()


# define a function for 2nd toplevel
# window which is not associated with
# any parent window
# Create button to open toplevel1
label1 = Label(root, text="Click on the button to open")

label1.pack()

# position the button

def DB_ARCHITECURE():
    pqrst = Label(root,
                  text="A Database Architecture is a representation of DBMS design.\n It helps to design, develop, implement, and maintain the database management system.\n A DBMS architecture allows dividing the database system into individual components that can be\n independently modified, changed, replaced, and altered. It also helps to understand the components of a database.")
    pqrst.pack(side="top", fill="both", expand=True, padx=20, pady=20)

def ACID_PROPERTIES():
    pqrst = Label(root,
                  text="The ACID properties, in totality, provide a mechanism to ensure the correctness and consistency of a database\n in a way such that each transaction is a group of operations that acts as a single unit, produces consistent results, acts in isolation from other operations,\n and updates that it makes are durably stored. ")
    pqrst.pack(side="top", fill="both", expand=True, padx=20, pady=20)
def open_Create():
    pqrst = Label(root,
                  text="CREATE TABLE TABLE_NAME(COLUMN_NAME1,) ")
    pqrst.pack(side="top", fill="both", expand=True, padx=20, pady=20)
    #button = Button(root, text="OK", command=lambda: root.destroy())
    # button.pack(side="bottom", fill="none", expand=True)
def open_Alter():
    global label
    label = Label(root,
                  text="Alter Table Table_Name Modify/Add/Drop Column Column_Name")
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
    #button = Button(root, text="OK", command=lambda: root.destroy())
    # button.pack(side="bottom", fill="none", expand=True)
def open_Drop():
    global label
    label = Label(root,
                  text="Alter Table Table_Name Modify/Add/Drop Column Column_Name")
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
    #button = Button(root, text="OK", command=lambda: root.destroy())
    # button.pack(side="bottom", fill="none", expand=True)
def open_INSERT():
    # global label
    label = Label(root,
                  text="Insert Table_Name(Column1,Column2,Column3......ColumnN) values(value1,value2,value3,value4..........valueN)")
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
    #button = Button(root, text="OK", command=lambda: root.destroy())
    # button.pack(side="bottom", fill="none", expand=True)
def open_UPDATE():
    #global abcde
    # label.destroy()

    abcde = Label(root,
                  text="UPDATE TABLE_NAME SET VALUE=REQUIRED VALUE WHERE CONDITION")
    abcde.pack(side="top", fill="both", expand=True, padx=20, pady=20)
def open_DELETE():
    # global xyzw
    # abcde.destroy()

    xyzw = Label(root,
                  text="DELETE TABLE_NAME WHERE CONDITION")
    xyzw.pack(side="top", fill="both", expand=True, padx=20, pady=20)


def des():
    button.destroy()
    label1.destroy()

# define a function for 1st toplevel
# which is associated with root window.

# def t():
#
#     lb = Label(root, text="Hiii")
#     lb.place(x=50, y=60)
def open_DDL():
    label.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button1.destroy()

    button6 = Button(root, text="Create",command=open_Create)
    button7 = Button(root, text="Alter",command=open_Alter)
    button8 = Button(root, text="Drop",command=open_Drop)


    # Create exit button.
    button9 = Button(root, text="Exit",
                    command=root.destroy)
    button6.pack()
    button7.pack()
    button8.pack()
    button9.pack()
    button6.config(height=5, width=25)
    button7.config(height=5, width=25)
    button8.config(height=5, width=25)
    button9.config(height=5, width=25)

def open_Toplevel1():
    global label
    global button1
    global button2
    global button3
    global button4
    global button5
    global u

    des()

    # Create label
    label =Label(root,
                  text="Click Any Button From the Following")

    # Create Exit button
    button1 = Button(root, text="Exit",
                     command=root.destroy)

    # create button to open toplevel2
    button2 = Button(root, text="DML",command=open_DML)
    button3 = Button(root, text="DDL",command=open_DDL)
    button4 = Button(root, text="DB Architecture",command=DB_ARCHITECURE)
    button5 = Button(root, text="ACID PROPERTIES",command=ACID_PROPERTIES)
    u= Button(root,text="Back",command=main_page)


    label.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button1.pack()
    u.pack()
    button1.config(height=5, width=25)
    button2.config(height=5, width=25)
    button3.config(height=5, width=25)
    button4.config(height=5, width=25)
    button5.config(height=5, width=25)
    u.config(height=5, width=25)

    # Display until closed manually
def open_Toplevel2():
    # p.destroy()
    # q.destroy()

    # Create label
    label =Label(root,
                  text="Click Any Button From the Following")

    # Create Exit button
    button1 = Button(root, text="Exit",
                     command=root.destroy)

    # create button to open toplevel2
    button2 = Button(root, text="DML",command=open_DML)
    button3 = Button(root, text="DDL",command=open_DDL)
    button4 = Button(root, text="DB Architecture",command=DB_ARCHITECURE)
    button5 = Button(root, text="ACID PROPERTIES",command=ACID_PROPERTIES)
    u= Button(root,text="Back",command=main_page)


    label.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button1.pack()
    u.pack()
    button1.config(height=5, width=25)
    button2.config(height=5, width=25)
    button3.config(height=5, width=25)
    button4.config(height=5, width=25)
    button5.config(height=5, width=25)
    u.config(height=5, width=25)
def open_DML():
    global button6
    global button7
    global button8
    global button9
    label.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button1.destroy()
    u.destroy()

    button6 = Button(root, text="Insert",command=open_INSERT)
    button7 = Button(root, text="Update",command=open_UPDATE)
    button8 = Button(root, text="Delete",command=open_DELETE)
    # l = Button(root, text="Back", command=lambda:[button6.destroy(),button7.destroy(),button8.destroy(),open_Toplevel1])

    # Create exit button.
    button9 = Button(root, text="Exit",
                    command=root.destroy)
    l = Button(root, text="Back",
               command=lambda: [button6.destroy(), button7.destroy(), button8.destroy(), open_Toplevel2])
    button6.pack()
    button7.pack()
    button8.pack()
    button9.pack()
    l.pack()
    button6.config(height=5, width=25)
    button7.config(height=5, width=25)
    button8.config(height=5, width=25)
    button9.config(height=5, width=25)
    l.config(height=5, width=25)
button = Button(root, text="DB OPERATION", command=open_Toplevel1)
button.place(x=175, y=125)
def main_page():
    global p
    global q
    label.destroy()
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()

    u.destroy()
    p = Label(root, text="Click on the button to open")

    p.pack()
    q = Button(root, text="DB OPERATION", command=lambda:[p.destroy(),q.destroy(),open_Toplevel2])
    # position the button
    q.place(x=175, y=125)


root.mainloop()
# main_page()

