import os
from os import system

def play():
	os.system('rhythmbox-client --play')
def pause():
	os.system('rhythmbox-client --pause')
def vol_up():
	os.system('rhythmbox-client --volume-up')
def vol_down():
	os.system('rhythmbox-client --volume-down')
def next():
	os.system('rhythmbox-client --play \n rhythmbox-client --next')
def previous():
	os.system('rhythmbox-client --play \n rhythmbox-client --previous')
def restart():
	os.system('rhytethmbox-client --play \n rhythmbox-client --previous')
def hide():
	os.system('rhythmbox-client --quit')
def error_message():
	os.system('print Sorry unknown command')
def quit():
	os.system('rhythmbox-client --quit')
