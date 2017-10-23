import speech2text
import parse
import threading
import time
import Queue
import execution
import decider
import re
import gui

def start_threads():
	controlThread=Control(1,"control")
	controlThread.start()
	# print time.time()
	# time.sleep(20)
	# print time.time()
	print "Exiting main thread"


class Control(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.parser= parse.Parser()
		self.guiQ=Queue.Queue(10)
		self.killall=threading.Event()
		self.killall.clear()
		self.stop_listen=threading.Event()
		self.stop_listen.clear()
		self.gui=gui.Gui(2,"gui",self.guiQ,self.killall,self.stop_listen)

		# with open("SAVED_DIRS.txt","r") as f:
		# 	saved_dirs={}
		# 	for line in f.readlines():
		# 		mo=re.match(r'(.*)####(.*)',line)
		# 		saved_dirs[mo.group(1)]=mo.group(2)
		# 	self.SAVED_DIRS=saved_dirs
		# 	print self.SAVED_DIRS


	def run(self):
		print "Starting " + self.name
		#start listener
		self.create_listener()
		self.listenerThread.start()
		self.gui.start()
		out_file = open("out.txt","a")
		do_listen=True	
		guiItem={}
		while (self.listenerThread.isAlive() and not self.kill_listener.isSet() and not self.killall.isSet()):
			print "abc"
			#print self.killall.isSet()
			# if self.stop_listen.isSet():
			# 	do_listen=True
			# else:202.141.80.22
			# 	do_listen=False
			text=self.workQueue.get(True)
			if do_listen:
				guiItem["yousaid"]=text	
			else:
				guiItem["yousaid"]="nothing!"
			self.guiQ.put(item=guiItem,block=True)
			if text :
				text=text.lower().strip()
				# out_file.write(text+"\n")
				parse_res=self.parser.parse_sent(text)
				print parse_res
				out_file.write(str(parse_res)+"\n")
				task=decider.generate(parse_res)
				print task
				if not task :
					task=decider.resolve(parse_res)
				print task
				try :
					if task['module']=="control":
						if task['func']=="startListening":
							do_listen=True
						else :
							self.stop_listen.clear()
							do_listen=False
					else:
						if do_listen:
							try:
								execution.exec_cmd(task)	
							except:
								print "ops"
				except KeyError:
					print "Oops! Can you repeat that?"
					
		# out_file.close()
		self.kill_listener.set()		
		print "Exiting " + self.name

	def create_listener(self):
		queueLock = threading.Lock()
		workQueue = Queue.Queue(10)
		kill_listener=threading.Event()
		kill_listener.clear()
		listen=threading.Event()
		listen.set()
		calibrate=threading.Event()
		calibrate.clear()

		self.queueLock=queueLock
		self.workQueue=workQueue
		self.kill_listener=kill_listener
		self.listen=listen
		self.calibrate=calibrate

		self.listenerThread = speech2text.Listener(1, "listener",queueLock,workQueue,kill_listener,listen,calibrate)
		# Start new Threads
		# self.listenerThread.start()

	def killListener(self):
		self.kill_listener.set()
		self.listenerThread=None
	def stopListening(self):
		self.listen.clear()	
	def startListening(self):
		self.listen.set()

	def test (self,text):
		text=text.lower().strip()
		parse_res=self.parser.parse_sent(text)
		print parse_res
		task=decider.generate(parse_res)
		print task
		if not task :
			task=decider.resolve(parse_res)
		print task
		if task['module']=="control":
			if task['func']=="startListening":
				self.startListening()
			else :
				self.stopListening()
		execution.exec_cmd(task)

start_threads()
# x= Control(1,"abcd")
# while (True):
# 	t=raw_input("Input:")
# 	x.test(t)