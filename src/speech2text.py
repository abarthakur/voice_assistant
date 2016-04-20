import speech_recognition as gsr
import os
from ctypes import *


ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
  pass
  #print filename,line,function,err,fmt

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
# Set error handler
asound.snd_lib_error_set_handler(c_error_handler)

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