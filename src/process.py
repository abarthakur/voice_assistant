# Process Module (Untested)
# Responsible for Managing ongoing procecsses and Applications
import os 
import pyKeyboard

def maximize(window): # Maximise the window mentioned in the parameter window
	os.system('wmctrl -R "'+window+'" ')

def minimize(window): # Minimize the window mentioned in the parameter window
	os.system('wmctrl -R "'+window+'"')
	kboard = PyKeyboard()
	kboard.press_key(kboard.alt_key)
	kboard.tap_key(' ')
	kboard.release_key(kboard.alt_key)
	time.sleep(.1)
	kboard.tap_key(kboard.down_key)
	kboard.tap_key(kboard.enter_key)

def foreground(window): # Takes a window given as parameter to the front
	os.system('wmctrl -R "'+window+'"')

def close(window): # Close the window  given as parameter
	os.system('wmctrl -c "'+window+'"')