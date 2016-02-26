# The aim of this file is to search a music file by name and play it randomly
import os
import subprocess
import re
from os import system


sample_input=raw_input("Enter the command : ")
sample_input=sample_input.lower()
gutter=["play ","music ","song ","listen ","hear "];
for gt in gutter:
	sample_input=sample_input.replace(gt,'');
in_splits=sample_input.split(); # Splits input string

music_dir="~/Music/English\ Music"

#Storing the list of songs extracted from music folder in an array
cmd="ls "+music_dir
music_files = subprocess.Popen(cmd,  shell=True, stdout=subprocess.PIPE) #runnning the subprocess
temp = music_files.stdout.read() #string of filenames

fileraw=temp.split("\n")
filenames=[]
for name in fileraw:
	filenames.append(name.lower())


filekeys=[]
count=0
for name in filenames:
	a=re.split('[,\+!.\-@\(\)\{\}\~\"\[\]_# ]*',name)
	filekeys.append(a)
	count=count+1

pointer=-1;
select_ptr=-1;
top_words=0
temp_words=0
top_score=0
temp_score=0


for file in filekeys:
	pointer+=1
	for inp in in_splits:
		if inp in file:
			temp_score=temp_score+len(inp)
			temp_words+=1
	if temp_score >= top_score:
		selected=file
		top_score=temp_score
		top_words=temp_words
		select_ptr=pointer

	temp_score=0
	temp_words=0
out_len=len(selected);
print selected

in_len=0
for inp in in_splits:
	in_len+=len(inp)

w1=0.8
w2=0.5
score1=w1*float(top_score)/float(in_len)
score2=w2*float(top_words)/float(out_len)
print "input_string: ",score1," output_string: ",score2
score =score1+score2
print  score
print filenames[select_ptr]
add=fileraw[select_ptr]
add=add.replace(" ","\ ");
cmd="xdg-open "+music_dir+"/"+add
if score>0.6:
	print cmd
	os.system(cmd)
else:
	#setting up the commands
	cmnd={'pause':"rhythmbox-client --pause"}
	cmnd['next']="rhythmbox-client --play \n rhythmbox-client --next"
	cmnd['previous']="rhythmbox-client --play \n rhythmbox-client --previous"
	cmnd['play']="rhythmbox-client --play"
	cmnd['vol-up']="rhythmbox-client --volume-up"
	cmnd['vol-down']="rhythmbox-client --volume-down"
	cmnd['hide']="rhythmbox-client --quit"
	cmnd['err_message']="print 'Sorry unknown command'"
	cmnd['quit']="rhythmbox-client --quit"

	#Controller begins
	priority_key={}
	priority_key['next']=['next']
	priority_key['previous']=['previous']
	priority_key['pause']=['pause','stop']
	priority_key['hide']=['hide']
	priority_key['quit']=['quit','close']
	priority_key['vol-up']=['increase','up','raise','high']
	priority_key['vol-down']=['decrease','down','lower','low','reduce']
	priority_key['play']=['play','start','music','song','listen','rhythmbox','current']

	def search(word,command,priority_key):
	    if word in priority_key[command]:
	        return 1
	    return 0

	str_split=sample_input.split()
	selected="err_message"

	for command in priority_key:
		for word in str_split:
			if(search(word,command,priority_key)):
				selected=command
				break;	

	print selected
	system(cmnd[selected])
