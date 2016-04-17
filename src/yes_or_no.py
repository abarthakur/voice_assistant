import Tkinter as guiwindow
from Tkinter import *
import tkMessageBox

#if you want to show yes or no
root=guiwindow.Tk()
root.withdraw()
ans= tkMessageBox.askyesno("Message you want to write at the top","Message you want to write at window")
#True for Yes button and vice versa
print ans