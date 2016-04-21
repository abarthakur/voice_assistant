import speech2text
import threading
import time

class Control(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print "Starting " + self.name
        # Get lock to synchronize threads
        
        # Free lock to release next thread
        print "Exiting " + self.name

