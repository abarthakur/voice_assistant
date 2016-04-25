import Tkinter as guiwindow
from Tkinter import *
import tkMessageBox

class Gui:
	#initializer
	def __init__(self):
		pass
	#this function will psop up a window asking yes or no
	def Ask_yes_or_no(self, msg_in_head, msg_in_body):
		#this will remove the back window
		root=guiwindow.Tk()
		root.withdraw()
		ans= tkMessageBox.askyesno(msg_in_head,msg_in_body)
		root.destroy()
		#this will return true if ans is yes
		return ans

	#this will ask ok or cancel
	def Ask_ok_or_Cancel(self, msg_in_head, msg_in_body):
		root=guiwindow.Tk()
		root.withdraw()
		ans=tkMessageBox.askokcancel(msg_in_head,msg_in_body)
		root.destroy()
		#this will return true if ans is ok
		return ans
	
	#this will ask retry or cancel
	def Ask_retry_or_cancel(self, msg_in_head, msg_in_body):
		root=guiwindow.Tk()
	  	root.withdraw()
	  	#this will return true if ans is yes
	  	ans=tkMessageBox.askretrycancel(msg_in_head,msg_in_body)
	  	root.destroy()
	 	return ans
	 #this will pop up wrning msgbox
	def Warning_msg(self, msg_in_head, msg_in_body):
		root=guiwindow.Tk()
		root.withdraw()
		ans= tkMessageBox.showwarning(msg_in_head,msg_in_body)
		root.destroy()
		#this will return ok when ok is pressed
		return ans

	#this will pop up info msgbox
	def Info_msg(self, msg_in_head, msg_in_body):
		root=guiwindow.Tk()
		root.withdraw()
		ans= tkMessageBox.showinfo(msg_in_head,msg_in_body)
		root.destroy()
		#this will return ok when ok is pressed
		return ans

	#this will pop us error msg box
	def Error_msg(self, msg_in_head, msg_in_body):
		root=guiwindow.Tk()
		root.withdraw()
		ans= tkMessageBox.showerror(msg_in_head,msg_in_body)
		root.destroy()
		#this will return ok when ok is pressed
		return ans
	def button_command(self):
		inpt=self.z.get()
		self.x=inpt
		self.y.destroy()	
		
		#print inpt

	def Take_input(self, msg_in_head, msg_in_body):
		root=guiwindow.Tk()
		self.y=root
		#root.withdraw()
		entry = guiwindow.Entry(font = "Helvetica 16",bd =0, width= 50)
		self.z=entry
		root.wm_title(msg_in_head)
		entry.pack(side=LEFT)
		button = guiwindow.Button( text="Get", command=self.button_command)
		button.pack()
		guiwindow.mainloop()
		return self.x
	def Take_password(self,msg_in_head,msg_in_body):
		root=guiwindow.Tk()
		self.y=root
		l = Label( text="Enter Password :")
		l.pack( side = LEFT)
		entry = guiwindow.Entry(show="*", font ="Helvetica 16",bd =0, width= 50)
		self.z=entry
		root.wm_title(msg_in_head)
		entry.pack(side=LEFT)
		button = guiwindow.Button( text="Get", command=self.button_command)
		button.pack()
		guiwindow.mainloop()
		return self.x
