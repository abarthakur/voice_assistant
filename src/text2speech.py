#pyttsx Copyright (c) 2009, 2013 Peter Parente
#Code snippet came along as sample code with the library
import pyttsx

def speak(txt):
	engine = pyttsx.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-50)
	engine.say(txt)
	engine.runAndWait()