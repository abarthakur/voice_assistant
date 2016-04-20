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
 #this will pop up wrning msgbox
def Warning_msg(msg_in_head,msg_in_body):
	root.withdraw()
	ans= tkMessageBox.showwarning(msg_in_head,msg_in_body)
	#this will return ok when ok is pressed
	return ans

#this will pop up info msgbox
def Info_msg(msg_in_head,msg_in_body):
	root.withdraw()
	ans= tkMessageBox.showinfo(msg_in_head,msg_in_body)
	#this will return ok when ok is pressed
	return ans

#this will pop us error msg box
def Error_msg(msg_in_head,msg_in_body):
	root.withdraw()
	ans= tkMessageBox.showerror(msg_in_head,msg_in_body)
	#this will return ok when ok is pressed
	return ans
def close_window():
	root.destroy()

def button_command():
	inpt=entry.get()
	print inpt
	close_window()
	return inpt
	# window.destroy()
	# return str(inpt)

def Take_input(msg_in_head,msg_in_body):
	root.wm_title(msg_in_head)
	entry.pack(side=LEFT)
	button = guiwindow.Button( text="Get", command=button_command)
	button.pack()
	guiwindow.mainloop()


#print Take_input("Window")