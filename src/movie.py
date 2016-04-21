import os
from os import system

def play():
	os.system('totem --play')
def pause():
	os.system('totem --pause')
def next():
	os.system('totem --play \n totem --next')
def previous():
	os.system('totem --play \n totem --previous')
def vol_up():
	os.system('totem --volume-up')
def vol_down():
	os.system('totem --volume-down')
def forward():
	os.system('totem --seek-fwd')
def backward():
	os.system('totem --seek-bwd')
def fullscreen():
	os.system('totem --fullscreen')
def mute():
	os.system('totem --mute')
def quit():
	os.system('totem --quit')
def error_message():
	os.system("print 'Sorry unknown command'")
