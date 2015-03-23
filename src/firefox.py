# Firefox Module (Untested)
# This module is responsible for controlling your Browser Completely

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