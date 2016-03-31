# Terminal Module (Untested)
# Open Applications, manage sessions, and basic operations that are possible through terminal
import os

def update(): # Update system
	os.system('sudo apt-get update')

def upgrade(): # Upgrade system
	os.system('sudo apt-get upgrade')

def shutdown(): # Shuts down the PC
	os.system('sudo poweroff')

def restart(): # Restart the system
	os.system('sudo reboot')

def lock(): # Lock the Screen
	os.system('gnome-screensaver-command -l')

def logout(): # Log out the current session
	os.system('gnome-session-quit')
 
def open(app): # Run the application mentioned as app
	app_dict={} # Stores the command to launch app
	app_dict['LibreWriter']='libreoffice --writer'
	app_dict['LibreSpread']='libreoffice --calc'
	app_dict['LibreDraw']='libreoffice --draw'
	app_dict['LibrePresentation']='libreoffice --impress'
	app_dict['calculator']='gnome-calculator'
	app_dict['sublime']='subl'

	os.system(app_dict[app])