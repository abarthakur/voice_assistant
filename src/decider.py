import os
from os import system


def generate(features):
	f_verb=features['verb']
	f_obj=features['object']
	with open("function_map") as fmap:
		task={}
		for line in fmap:
			line=line[:-1]
			terms=line.split()
			if f_verb==terms[0] and f_obj==terms[1]:
				task['module']=terms[2]
				task['func']=terms[3]
				if len(terms)>4:
					task['param']=terms[4:]
				else:
					task['param']=[]
	return task
print generate({'verb':'listen','object':'song'})



	