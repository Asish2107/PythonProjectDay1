
import os
import time
import tkinter.filedialog
import pyautogui
from tkinter import filedialog
from datetime import datetime

#Function to print star program
def star(a):
    k = a - 1
    #Loop To print spaces
    for i in range(0, a):
        for j in range(0, k):
            print(end=" ")
        k = k - 1

        #Loop To print *
        for j in range(0, i + 1):
            print("* ", end="")
        time.sleep(2)#time.sleep(n) is used to have n seconds gap between the execution of one loop to another
        a=pyautogui.screenshot()#pyautogui will be helpful to take screenshots automatically
        b=tkinter.filedialog.askdirectory() #tkinter.filedialog.askdirectory() is used to create a dialog to ask the user the location path where we want to save the screenshots
        #root = tkinter.Tk()
        #root.withdraw()
        current_time = datetime.now().replace(microsecond=0)
        #print(type(current_time))
        format = "%y_%b_%d_%H_%M_%S"
        new_time = datetime.strftime(current_time, format)
        z="a"+new_time+".png"
        c = os.path.join(b,z)
        a.save(c)
        print("\r")
star(5)




