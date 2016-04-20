import speech_recognition as gsr
import os
from ctypes import *
import threading

class Listener(threading.Thread):

	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.ALSA_err_handler=self.suppress_ALSA_warnings()
		self.recognizer=gsr.Recognizer()
		self.mic = gsr.Microphone()

#need to reset error handler at time of exiting thread			
	def run(self):
		print "Starting " + self.name
		self.test()
		print "Exiting " + self.name

#http://stackoverflow.com/questions/7088672/pyaudio-working-but-spits-out-error-messages-each-time

	def suppress_ALSA_warnings(self):
		ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
		c_error_handler = ERROR_HANDLER_FUNC(self.py_error_handler)
		asound = cdll.LoadLibrary('libasound.so')
		asound.snd_lib_error_set_handler(c_error_handler)
		#asound.snd_lib_error_set_handler(None)
		return c_error_handler
	
	def py_error_handler(self,filename, line, function, err, fmt):
		pass


	def speech2text(self):
		try: 
			print "Say Something ..."
			with self.mic as source: 
				audio = self.recognizer.listen(source=source,timeout=2)
			
			value = self.recognizer.recognize_google(audio_data=audio,language="en-IN")
			return format(value).encode("utf-8")
		
		except gsr.UnknownValueError:
			print("Oops! Didn't catch that")
		except gsr.RequestError as e:
			print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))


	def test(self):
		# handler=self.suppress_ALSA_warnings()
		# r = gsr.Recognizer()
		# m = gsr.Microphone()
		print "Silence for 5 seconds"
		with self.mic as source: self.recognizer.adjust_for_ambient_noise(source=source,duration=5)
		print "Ok, good to go!"
		i=0
		while(i<5):
			try:
				print self.speech2text()
				i+=1
			except gsr.WaitTimeoutError:
				pass

# Create new threads
# thread1 = Listener(1, "Thread-1")
# # Start new Threads
# thread1.start()
# print "Exiting Main Thread"
