# Firefox Module (Untested)
# This module is responsible for controlling your Browser Completely
# Please note that the following applications need to be installed first before using this module
# 1. pykeyboard python library: For acessing your Keyboard
# 2. wmctrl ubuntu package : For switching between windows
import os 
from pykeyboard import PyKeyboard
import time

def start_window(): # Start Firefox
	os.system('firefox')

def search(term): # Search a particular term on Default Search Engine
	os.system('firefox -search '+term)

def close_window(): # Close the Firefox Window
	os.system('wmctrl -c "Mozilla Firefox"')

def maximize(): # Maximise the Firefox Window
	os.system('wmctrl -R "Mozilla Firefox" ')

def minimize(): # Minimise the Firefox Window
	os.system('wmctrl -R "Mozilla Firefox"')
	kboard = PyKeyboard()
	kboard.press_key(kboard.alt_key)
	kboard.tap_key(' ')
	kboard.release_key(kboard.alt_key)
	time.sleep(.1)
	kboard.tap_key(kboard.down_key)
	kboard.tap_key(kboard.enter_key)

def new_tab(): # Open a New Tab
	os.system('wmctrl -R "Mozilla Firefox"')
	kboard = PyKeyboard()
	kboard.press_key(kboard.control_l_key)
	kboard.tap_key('t')
	kboard.release_key(kboard.control_l_key)
 
def close_tab(): # Close the current Tab
	os.system('wmctrl -R "Mozilla Firefox"')
	kboard = PyKeyboard()
	kboard.press_key(kboard.control_l_key)
	kboard.tap_key(kboard.function_keys[4])
	kboard.release_key(kboard.control_l_key)

def next_tab(): # Navigate to tab on the right
	os.system('wmctrl -R "Mozilla Firefox"')
	kboard = PyKeyboard()
	kboard.press_key(kboard.control_l_key)
	kboard.tap_key(kboard.tab_key)
	kboard.release_key(kboard.control_l_key)

def previous_tab(): # Navigate to tab on left
	os.system('wmctrl -R "Mozilla Firefox"')
	kboard = PyKeyboard()
	kboard.press_key(kboard.control_l_key)
	kboard.press_key(kboard.shift_key)
	kboard.tap_key(kboard.tab_key)
	kboard.release_key(kboard.shift_key)
	kboard.release_key(kboard.control_l_key)
