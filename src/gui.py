import Tkinter as guiwindow
from Tkinter import *
import tkMessageBox


root=guiwindow.Tk()
entry = guiwindow.Entry()
#this function will psop up a window asking yes or no
def Ask_yes_or_no(msg_in_head,msg_in_body):
	#this will remove the back window
	root.withdraw()
	ans= tkMessageBox.askyesno(msg_in_head,msg_in_body)
	#this will return true if ans is yes
	return ans

#this will ask ok or cancel
def Ask_ok_or_Cancel(msg_in_head,msg_in_body):
	root.withdraw()
	ans=tkMessageBox.askokcancel(msg_in_head,msg_in_body)
	#this will return true if ans is yes
	return ans

#this will ask retry or cancel
def Ask_retry_or_cancel(msg_in_head,msg_in_body):
  	root.withdraw()
  	#this will return true if ans is yes
 	return ans