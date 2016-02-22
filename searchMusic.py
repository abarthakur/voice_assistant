# The aim of this file is to search a music file by name and play it randomly
import os
import subprocess
import re

sample_input=raw_input("Enter the command : ")
sample_input=sample_input.lower()
gutter=["play ","music ","song ","listen ","hear "];
for gt in gutter:
	sample_input=sample_input.replace(gt,'');

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

print filekeys

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