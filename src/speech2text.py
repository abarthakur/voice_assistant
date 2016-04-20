import speech_recognition as gsr
import os


r = gsr.Recognizer()
m = gsr.Microphone()
print "Silence for 5 seconds"
with m as source: r.adjust_for_ambient_noise(source=source,duration=5)
print "Ok, good to go!"

def speech2text():
	try: 
		print "Say Something ..."
		with m as source: audio = r.listen(source=source,timeout=2)
		value = r.recognize_google(audio_data=audio,language="en-IN")
		return format(value).encode("utf-8")
	except gsr.UnknownValueError:
		print("Oops! Didn't catch that")
	except gsr.RequestError as e:
		print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

while(True):
	try:
		print speech2text()
	except gsr.WaitTimeoutError:
		pass