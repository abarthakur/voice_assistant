# File Module (Untested)
# Responsible for Managing File Browser nautilus
import os
import pyKeyboard
# import gui  ---Still to be made

def get_browser_path(): # Gets the path of the Nautilus file browser
	# The function is supossed to get the file address of the current nautilus file browser

def create_directory(): # Creates a New Directory in the current Nautilus file browser
	present_dir=get_browser_path() # Get Path of the current Directory in Nautilus 

	# Ask User for a name, to be implemented
	# name = gui.getInput('Please type a name for the new Directory')
	cmd="mkdir "+name
	os.system(cmd)

def open_file(file): # Open the file mentioned in the parameter
	present_dir=get_browser_path() # Get Path of the current Directory in Nautilus
	cmd="xdg-open "+file
	os.system(cmd)

def delete(inp): # Delete the file mentioned as parameter
	cmd="" 
	confirm=False
	present_dir=get_browser_path() # Get Path of the current Directory in Nautilus
	path=present_dir+"/"+inp
	if os.path.isdir(path):
		# gui.confirm(confirm,'Are you sure you want to delete '+input) --To be developed
		if confirm:
			cmd="rm -r "+path
			os.system(cmd)
	elif os.path.isfile(path):
		# gui.confirm(confirm,'Are you sure you want to delete '+input) --To be developed
		if confirm:
			cmd="rm "+path
			os.system(cmd)
	else:
		# gui.alert('Sorry, This is neither a path nor a folder') --To be developed


def search(string): # Search file or folder in current Nautilus window
	kboard = PyKeyboard()
	kboard.press_key(kboard.control_l_key)
	kboard.tap_key('f')
	kboard.release_key(kboard.control_l_key)
	time.sleep(.1)
	kboard.type_string(string)

def open_inner_directory(dirname): # Open a directory inside current open directory
	present_dir=get_browser_path() # Get Path of the current Directory in Nautilus
	path=present_dir+'/'+dirname
	if os.path.isdir(path):
		kboard = PyKeyboard()
		kboard.press_key(kboard.control_l_key)
		kboard.tap_key('f')
		kboard.release_key(kboard.control_l_key)
		time.sleep(.1)
		kboard.type_string(path)
		kboard.tap_key(kboard.enter_key)

def open_outer_directory(): # Navigate to the parent directory of the present directory
	present_dir=get_browser_path() # Get Path of the current Directory in Nautilus
	if present_dir.count('/')>=2:
		path=present_dir.split('-1')[:-1]
		kboard = PyKeyboard()
		kboard.press_key(kboard.control_l_key)
		kboard.tap_key('f')
		kboard.release_key(kboard.control_l_key)
		time.sleep(.1)
		kboard.type_string(path)
		kboard.tap_key(kboard.enter_key)

def move_item(item,destination): # Cut operation for file and folder
	present_dir=get_browser_path() # Get Path of the current Directory in Nautilus
	path=present_dir+'/'+item
	if os.path.isdir(path):
		cmd='mv '+path+' '+' '+destination
		os.system(cmd)
	elif os.path.isfile(path):
		cmd='mv '+path+' '+' '+destination
		os.system(cmd)
	else:
		# gui.alert('Sorry, This is neither a path nor a folder') --To be developed


def copy_item(item,destination): # Copy operation for folder and files
	present_dir=get_browser_path() # Get Path of the current Directory in Nautilus
	path=present_dir+'/'+item
	if os.path.isdir(path):
		cmd='cp '+path+' '+' '+destination
		os.system(cmd)
	elif os.path.isfile(path):
		cmd='cp '+path+' '+' '+destination
		os.system(cmd)
	else:
		# gui.alert('Sorry, This is neither a path nor a folder') --To be developed
