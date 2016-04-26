import os
from os import system
import re

def generate(features):
	f_verb=features['verb']
	f_obj=features['object']
	task={}
	with open("function_map") as fmap:
		for line in fmap:
			line=line.strip()
			terms=line.split()
			if f_verb==terms[0] and f_obj==terms[1]:
				task['module']=terms[2]
				task['func']=terms[3]
				if len(terms)>4:
					task['param']=terms[4:]
				else:
					task['param']=[]
	return task


def resolve(features):
	task = {}
	templates = []
	with open("regex.txt") as regex:
		for line in regex:
			line=line.strip()
			template=line
			templates.append(template)
	string=features['input'].lower()
	for t in templates:
		t=t.split("###")
		template=t[0]
		try:
			if (re.match(template, string)):
				m=re.match(template, string)
				task['module']=t[1]
				task['func']=t[2]
				if len(t)>3:
					num=int(t[3])
					print m.groups()
					substr=m.groups()[num]
					print substr
					task['param']=substr
				else:
					task['param']=[]
				return  task
		except:
			print "Sorry Didn't get you"
	return task

print resolve({"input":"search this page for bitch and his"})