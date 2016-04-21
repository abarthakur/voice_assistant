# Process Module (Untested)
# Responsible for Managing ongoing procecsses and Applications
import os 

def maximize(window): # Maximise the window mentioned in the parameter window
	os.system('xdotool search --name "'+window+'" windowactivate')
	cmd="xdotool key ctrl+super+Up"
	os.system(cmd)

def minimize(window): # Minimize the window mentioned in the parameter window
	os.system('xdotool search --name "'+window+'" windowminimize')

def foreground(window): # Takes a window given as parameter to the front
	os.system('xdotool search --name "'+window+'" windowactivate')

def close(window): # Close the window  given as parameter
	os.system('xdotool search --name "'+window+'" windowkill')