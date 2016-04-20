import firefox
import terminal
import process
import text2speech
import os
import subprocess
import gui
import music
import movie
import inspect
import process

commands={}

def import_function(name):
	fns=[fn[0] for fn in inspect.getmembers(__import__(name),inspect.isfunction)]
	return fns


def foreground(window):
	pid=subprocess.Popen(['xdotool','getactivewindow','getwindowname'],stdout=subprocess.PIPE).stdout.read()
	if window in pid:
		return True
	else:
		return False

def active(window):
	pid=subprocess.Popen(['xdotool','search','--name',window,"getwindowname"],stdout=subprocess.PIPE).stdout.read()
	if pid:
		return True
	else:
		return False



def validate(module,func):
	if func in commands[module]:
		return True
	else:
		return False

def sanity_check_firefox(func,param,msg):
	if func=='start_window':
	 	if active("firefox"):
			msg="Firefox is already running"
			return False
		else:
			return True
	else:
		if not active("firefox"):
			return False
		else:
			if func=="search_page" and not param:
				return False
			else:
				return True



def sanity_check_process(func,param,msg):
	if not param:
		return False
	window=param[0]
	if not active(window):
		msg=param[0]+" is not running"
		return False

	if func=="foreground" and foreground(window):
		msg=window+" is already in front"
		return False
	return True


def sanity_check_terminal(func,param,msg):
	if func=="open":
		if not param:
			return False
		else:
			return True
	else:
		confirm=gui.Ask_yes_or_no("Request for confirmation","Are you sure you want to "+func+" your system ?")
		if not confirm:
			return False
		# password=gui.Take_input("Authentication Needed","Please enter your password")
		# print str(password)+"hello"
		return True

def sanity_check_music(func,param,msg):
	if not active("Rhythmbox"):
		if func != "play":
			msg="Rhythmbox is not running. start rhythmbox first"
			return False
	return True

def sanity_check_movie(func,param,msg):
	if not active("Videos"):
		return False
	return True


def exec_cmd(task):
	# task={"module":"movie","func":"pause","param":[]}
	modules=["firefox","process","music","movie","terminal"]
	for module in modules:
		commands[module]=import_function(module)

	msg=''
	allow=False
	module=task["module"]
	function=task["func"]
	parameter=task["param"]


	valid=validate(module,function)
	if valid:
		sanity_function="sanity_check_"+module
		sanity_check=globals()[sanity_function]
		allow=sanity_check(function,parameter,msg)
	else:
		print "Utility not available"

	if not allow or not valid:
		if msg:
			print msg
	else:
		execute=getattr(__import__(task["module"]),task["func"])
		execute(*parameter)
 			

