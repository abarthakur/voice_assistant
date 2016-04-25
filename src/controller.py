import speech2text
import parse
import threading
import time
import Queue
import execution

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
		self.create_listener()
		self.parser= parse.Parser()

	def run(self):
		print "Starting " + self.name
		#start listener
		self.listenerThread.start()
		out_file = open("out.txt","a")
		while (self.listenerThread.isAlive() and not self.kill_listener.isSet()):
			text=self.workQueue.get(True)
			if text :
				out_file.write(text+"\n")
				parse_res=self.parser.parse_sent(text)
				out_file.write(str(parse_res)+"\n")
				#execution.exec_cmd(task)	
		out_file.close()		
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


start_threads()