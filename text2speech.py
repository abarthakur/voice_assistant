#pyttsx Copyright (c) 2009, 2013 Peter Parente
#Code snippet came along as sample code with the library
import pyttsx

txt=raw_input("Enter Something you want me to speak: ")

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-90)
engine.say(txt)
engine.runAndWait()