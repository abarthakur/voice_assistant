import speech_recognition as gsr
import os


r = gsr.Recognizer()
m = gsr.Microphone()

def speech2text():
	try: 
		print "Say Something ..."
		with m as source: r.adjust_for_ambient_noise(source)
		with m as source: audio = r.listen(source)
		value = r.recognize_google(audio)
		return format(value).encode("utf-8")
	except gsr.UnknownValueError:
		print("Oops! Didn't catch that")
	except gsr.RequestError as e:
		print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))