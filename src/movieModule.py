from os import system
import pyttsx

#Setting up the speaker
def onStart(name):
   print ""
def onWord(name, location, length):
   print ""
def onEnd(name, completed):
   print "" 
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd) 
#Speaker terminated

#variables needed
music_dir="~/media/hritik/New\ Volume1/dc++/movies"
input_cmd=raw_input("Enter the command : ")

#setting up the commands
cmd={'pause':"totem --pause"}
cmd['next']="totem --play \n totem --next"
cmd['previous']="totem --play \n totem --previous"
cmd['play']="totem --play"
cmd['vol-up']="totem --volume-up"
cmd['vol-down']="totem --volume-down"
cmd['err_message']="print 'Sorry unknown command'"
cmd['quit']="totem --quit"
cmd['forward']="totem --seek-fwd"
cmd['backward']="totem --seek-bwd"
cmd['fullscreen']="totem --fullscreen"
cmd['mute']="totem --mute"

#Controller begins
priority_key={}
priority_key['next']=['next']
priority_key['previous']=['previous']
priority_key['pause']=['pause','stop']
priority_key['quit']=['quit','close']
priority_key['fullscreen']=['full','fullscreen','maximize','maximise']
priority_key['mute']=['mute','nil','zero','lowest']
priority_key['forward']=['ahead','forward']
priority_key['backward']=['back','backward']
priority_key['vol-up']=['increase','up','raise','high']
priority_key['vol-down']=['decrease','down','lower','low','reduce']
priority_key['play']=['play','start','video','movie','watch','player','current']

def search(word,command,priority_key):
    if word in priority_key[command]:
        return 1
    return 0

str_split=input_cmd.split()
selected="err_message"

for command in priority_key:
	for word in str_split:
		if(search(word,command,priority_key)):
			selected=command
			break;

print selected
system(cmd[selected])