import speech_recognition as gsr
import os
from ctypes import *
import threading
import Queue
import time

class Listener(threading.Thread):

	#Should all other fns besides recalibrate be private? perhaps we can even set recalibrate to be private by using
	#threading.Event
	def __init__(self, threadID, name, queueLock,workQueue,stopThread,doListen,doRecalibrate):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.ALSA_err_handler=self.suppress_ALSA_warnings()
		self.recognizer=gsr.Recognizer()
		self.mic = gsr.Microphone()
		self.queueLock=queueLock
		self.workQueue=workQueue
		self.stopThread=stopThread
		self.doListen=doListen
		self.doRecalibrate=doRecalibrate

#need to reset error handler at time of exiting thread
#doListen is an threading.Event object that manages a flag that determines whether Listener listens		
#doRecalibrate is an threading.Event object that manages a flag that determines whether Listener listens
#stopThread	is also a threading.Event object. If set true, the thread exits.
#doListen must be set when stopThread is set. Later we can add a timeout arg		
	def run(self):
		print "Starting " + self.name
		start=1
		# self.test()
		while (not self.stopThread.isSet()):
			if (self.doListen.isSet()):
				#initially recalibrate once, or if asked to by another thread
				if(start==1 or self.doRecalibrate.isSet()):
					self.recalibrate()
					start=0
					self.doRecalibrate.clear()
				try:
					text_output= self.speech2text()
					self.push_to_queue(text_output)
					# i+=1
				except gsr.WaitTimeoutError:
					pass
			else:
				self.doListen.wait()
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

	def recalibrate(self):
		print "Silence for 5 seconds"
		with self.mic as source: self.recognizer.adjust_for_ambient_noise(source=source,duration=5)
		print "Ok, good to go!"

	def push_to_queue(self,item):
		self.queueLock.acquire()
		self.workQueue.put(item=item,block=False)
		self.queueLock.release()

	def test(self):
		# handler=self.suppress_ALSA_warnings()
		# r = gsr.Recognizer()
		# m = gsr.Microphone()
		self.recalibrate()
		i=0
		while(i<5):
			try:
				text_output= self.speech2text()
				self.push_to_queue(text_output)
				i+=1
			except gsr.WaitTimeoutError:
				pass

# queueLock = threading.Lock()
# workQueue = Queue.Queue(10)
# # Create new threads
# kill=threading.Event()
# kill.clear()
# listen=threading.Event()
# listen.set()
# cal=threading.Event()
# cal.clear()
# thread1 = Listener(1, "Thread-1",queueLock,workQueue,kill,listen,cal)
# # Start new Threads
# thread1.start()
# out_file = open("out.txt","a")
# # while(thread1.is_alive()):
# # 	try:
# # 		text = workQueue.get(True)
# # 		out_file.write(text+"\n")
# # 		print "From main thread:"+text
# # 	except Queue.Empty:
# # 		continue
# x=time.time()
# y=time.time()	
# flag=1
# flag2=1
# flag3=1
# while(y-x<=120 and thread1.is_alive()):#thread1.is_alive()):
# 	y=time.time()	
# 	#print y,x
	
# 	if(y-x>30 and y-x<60 and flag==1):
# 		print "From main thread: 1 min up! stop listening!"
# 		listen.clear()
# 		flag=0
# 	if (y-x>60 and y-x<90 and flag2==1):
# 		print "From main thread: listen again"
# 		listen.set()
# 		flag2=0
# 	if(y-x>90 and flag3==1):
# 		print "From main thread: die permanently"
# 		kill.set()
# 		flag3=0
# 	try:
# 		text = workQueue.get(True,3)
# 		if text:
# 			out_file.write(text+"\n")
# 			print "\n\nFrom main thread:"+text+"\n\n"
# 	except :#Queue.Empty:
# 		continue
# print "Exiting Main Thread"