from nltk.parse import stanford


def extract_obj(vp_subtree) :
	obj="noobj"
	par = vp_subtree.parent
	#print par
	for child in par :
		if(child.label()=="NP" or child.label()=="PP") :
			for x in child :
				#print x[0]		
				if (x.label()[0:2]=="NN"):
					# print x.label()
					obj = x[0]
					break
		elif (child.label()=="ADJP"):
			for x in child :
				if (x.label()[0:1]=="JJ"):
					obj = x[0]

	return obj


def extract_pred(vp_subtree):
	#the deepest verb is the predicate
	#do BFS
	verb="none"
	queue= [vp_subtree]
	for subtree in queue:

		if (subtree.height()>2 ) :#not a leaf
			for child in subtree: #note that all the children's height is at least 2
				child.parent= subtree
				queue.append(child)

		elif (subtree.height()==2) :
			if (subtree.label()[0] =='V'):
				verb_tree=subtree
	verb = verb_tree[0]
	return (verb,verb_tree)

def verify_coms():
	p= stanford.StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz", 
								path_to_jar="/home/aneesh/git_projects/team12cs243/stanford-parser.jar",
								path_to_models_jar="/home/aneesh/git_projects/team12cs243/stanford-parser-3.5.2-models.jar"
								)

	#sent = "A rare black squirrel has become a regular visitor in our suburban garden"
	# sent = "I want to listen to about time"
	com_file = open("all_commands.txt","r")
	verb_file = open("verbs.txt","w")
	sents = com_file.readlines()
	for sent in sents :
		iterator=p.raw_parse(sent)
		root=iterator.next(	)
		#print y.leaves()
		# tree_file.write(sent +"\n" +root.pretty_print() +"\n\n\n")
		root.pretty_print()
		s=root[0]
		# s.pretty_print()
		
		verb=""
		obj=""
		for child in s:
			if (child.label()=="VP"):
				(verb,tree)=extract_pred(child)
				obj= extract_obj(tree)
		verb_file.write(verb +"  " +obj +"\n"+ sent+"\n")


#verify_coms()

p= stanford.StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz", 
								path_to_jar="/home/aneesh/git_projects/team12cs243/stanford-parser.jar",
								path_to_models_jar="/home/aneesh/git_projects/team12cs243/stanford-parser-3.5.2-models.jar"
								)
sent = "open libre writer application"
iterator=p.raw_parse(sent)
root=iterator.next(	)
#print y.leaves()
# tree_file.write(sent +"\n" +root.pretty_print() +"\n\n\n")
root.pretty_print()
s=root[0]
# s.pretty_print()
for child in s:
	if (child.label()=="VP"):
		 (verb,tree) = extract_pred(child)
		 obj=extract_obj(tree)
		 print verb
		 print obj