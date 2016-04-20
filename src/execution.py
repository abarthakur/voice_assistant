import firefox
# import music
import terminal
import process
import text2speech
import os
import subprocess
import gui



commands={}
commands["process"]=["maximize","minimize","foreground","close"]
commands["firefox"]=["start_window","search","close_window","minimize","maximize",
					"new_tab","close_tab","previous_tab","next_tab",
					"scroll_down","scroll_up","zoom_in","zoom_out","search_page",
					"forward","back","refresh","reload",
					"bookmark","open_bookmark","history","delete_history","print_page","save_page"
					]
commands["music"]=["play","pause","next","previous","restart","vol_up","vol_down","quit","hide"]
commands["terminal"]=["update","upgrade","shutdown","restart","lock","logout","open"]

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


running={}
running['firefox'] = active("Mozilla Firefox")
running['rhythmbox'] = active("Rhythmbox")
running['totem'] = active("Totem") 
 	 	


task={"module":"terminal","func":"update","param":[]}



def sanity_check_firefox(func,param,msg):
	if func not in commands["firefox"]:
		return False
	if func=='start_window':
	 	if running["firefox"]:
			msg="Firefox is already running"
			return False
		else:
			return True
	else:
		if not running["firefox"]:
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




msg=''
allow=False
module=task["module"]
function=task["func"]
parameter=task["param"]


sanity_function="sanity_check_"+module
sanity_check=globals()[sanity_function]
allow=sanity_check(function,parameter,msg)





if not allow:
	if msg:
		print msg
else:
	execute=getattr(__import__(task["module"]),task["func"])
	execute(*parameter)
 		
 		

