# Firefox Module (Untested)
# This module is responsible for controlling your Browser Completely

import os 
import time

def start_window(): # Start Firefox
	os.system('nohup firefox </dev/null &>/dev/null &')

def search(term): # Search a particular term on Default Search Engine
	os.system('nohup firefox --search '+term+' </dev/null &>/dev/null &')

def close_window(): # Close the Firefox Window
	os.system('xdotool search --name "Mozilla Firefox" windowkill')

def maximize(): # Maximise the Firefox Window
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	cmd="xdotool key ctrl+super+Up"
	os.system(cmd)

def minimize(): # Minimise the Firefox Window
	os.system('xdotool search --name "Mozilla Firefox" windowminimize')
	

def new_tab(): # Open a New Tab
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key "ctrl+t"')
 
def close_tab(): # Close the current Tab
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key "ctrl+F4"')

def next_tab(): # Navigate to tab on the right
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key "ctrl+Tab"')
	

def previous_tab(): # Navigate to tab on left
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key "ctrl+shift+Tab"')
	
def scroll_down(): # Scroll Down
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key Down')
	

def scroll_up(): # Scroll Up
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key Up')
	
def search_page(string): # Search for a particular term in the page
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key Ctrl+f')
	time.sleep(0.1)
	os.system('xdotool type '+ string)

def zoom_in(): # Zoom in the current tab
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key Ctrl+plus')	

def zoom_out(): # Zoom out the current tab
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key Ctrl+minus')
	
def forward():
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key alt+Right')
	
def back():
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key alt+Left')
	
def refresh():
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key F5')
	
def reload():
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key ctrl+F5')
	

def bookmark(): # Adds a bookmark
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key ctrl+d')

def open_bookmark(): # Open the bookmark Window
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key ctrl+shift+o')
	
def history(): # Display the History window
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key ctrl+h')
	

def delete_history(): # Delete the History
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key ctrl+shift+Delete')
	

def print_page(): # Prompt the user to Print Window
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key ctrl+p')
	

def save_page(): # Prompt the user to save window
	os.system('xdotool search --name "Mozilla Firefox" windowactivate')
	os.system('xdotool key ctrl+s')
