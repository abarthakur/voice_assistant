import Tkinter as guiwindow
from Tkinter import *
import tkMessageBox
import Queue
import threading

class Gui(threading.Thread):
	#initializer
	def __init__(self, threadID, name,guiQueue):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.myQueue=guiQueue
		(self.mainwindow,self.youSaid,self.systemMsg)=self.create_mainwindow()

	def run(self):
		self.mainwindow.after(100,check)
		self.mainwindow.mainloop()


	def create_mainwindow(self):
		root=Tk()
		topframe=Frame(root)
		botframe=Frame(root)
		topframe.pack(side=TOP)
		botframe.pack(side=BOTTOM)
		ys=StringVar()
		ys.set("You said :")
		sm=StringVar()
		sm.set("System Messages :")
		var=StringVar()
		var.set(".....")
		var2=StringVar()
		var2.set(".....")

		lab=Label(topframe,textvariable=ys,justify=LEFT,padx=1)
		lab2=Label(topframe,textvariable=var,justify=LEFT,padx=2,relief=SUNKEN)
		lab3=Label(botframe,textvariable=sm,justify=LEFT,padx=1)
		lab4=Label(botframe,textvariable=var2,justify=LEFT,padx=2,relief=SUNKEN)
		lab.pack(side=TOP)
		lab2.pack(side=BOTTOM)
		lab3.pack(side=TOP)
		lab4.pack(side=BOTTOM)
		return root,var,var2

	def check(self):
		msgs=self.myQueue.get(True)
		if msgs.has_key("yousaid"):
			self.youSaid=msgs["yousaid"]
		if msgs.has_key("systemMsg"):
			self.systemMsg=msgs["systemMsg"]

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


