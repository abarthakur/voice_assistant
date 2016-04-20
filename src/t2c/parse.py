from nltk.parse import stanford

class Parser(object):
	
	#Later pass these as arguments, when the main loads configuration file
	MODEL_PATH="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz"
	PATH_TO_JAR="/home/aneesh/git_projects/team12cs243/stanford-parser.jar"
	PATH_TO_MODELS_JAR="/home/aneesh/git_projects/team12cs243/stanford-parser-3.5.2-models.jar"

	def __init__(self):
		super(Parser, self).__init__()
		self.stanpar=p= stanford.StanfordParser(model_path=self.MODEL_PATH, 
								path_to_jar=self.PATH_TO_JAR,
								path_to_models_jar=self.PATH_TO_MODELS_JAR
								)

	def parse_sent(self,sent):
		iterator=self.stanpar.raw_parse(sent)
		root=iterator.next()
		#print y.leaves()
		# tree_file.write(sent +"\n" +root.pretty_print() +"\n\n\n")
		#root.pretty_print()
		s=root[0]
		s.pretty_print()
		##multiple VPs
		for child in s:
			if (child.label()=="VP"):
				child.parent=s
				(verb,vtree) = self.extract_pred(child)
				(obj,otree)=self.extract_obj(vtree)

		results = {}
		results['input']=sent
		results['verb']=verb
		results['object']=obj
		return results
		# print verb
		# print extract_attr(tree)
		# print obj
		# print extract_attr(otree)


	def extract_pred(self,vp_subtree):
		#the deepest verb is the predicate
		#do BFS
		verb="none"
		verb_tree=None
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


	def extract_obj(self,verb_subtree) :
		obj="noobj"
		objtree=None
		if (verb_subtree==None):
			return (obj,objtree)

		par = verb_subtree.parent
		#print par
		for child in par :
			if(child.label()=="NP" or child.label()=="PP") :
				for x in child :
					x.parent=child
					#print x[0]		
					if (x.label()[0:2]=="NN"):
						# print x.label()
						obj = x[0]
						objtree=x
						break
			elif (child.label()=="ADJP"):
				for x in child :
					x.parent=child
					if (x.label()[0:1]=="JJ"):
						obj = x[0]
						objtree=x
		return (obj,objtree)


	def extract_attr(self,word_subtree):
		if word_subtree==None :
			return []
		par=word_subtree.parent
		attrs=[]
		if word_subtree.label()[0:2]=="JJ" :
			for child in par:
				if(child.label()=="RB"):
					attrs.append(("RB"," ".join(child.leaves())))
		elif word_subtree.label()[0:2]=="NN":
			for child in par :
				if child.label() in ["DT","PRP$","POS","JJ","CD","ADJP","QP","NP"] :
					attrs.append((child.label()," ".join(child.leaves())))
		elif word_subtree.label()[0:2]=="VB":
			for child in par:
				if(child.label()=="ADVP"):
					attrs.append(("ADVP"," ".join(child.leaves())))

		grandpar=par.parent
		if word_subtree.label()[0:2] in ["NN","JJ"]:
			for uncle in grandpar:
				if uncle.label() == "PP":
					attrs.append(("PP"," ".join(uncle.leaves())))
		elif word_subtree.label()[0:2] =="VB" :
			for uncle in grandpar:
				if uncle.label()[0:2]=="VB":
					attrs.append(("VB"," ".join(child.leaves())))
		return attrs


	def verify_coms(self):
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
			v_attr=[]
			o_attr=[]
			for child in s:
				if (child.label()=="VP"):
					child.parent=s
					(verb,tree)=extract_pred(child)
					v_attr= extract_attr(tree)
					(obj,objtree)= extract_obj(tree)
					o_attr=extract_attr(objtree)
			verb_file.write("verb="+verb+",v_attr="+str(v_attr)+",obj="+obj+",o_attr"+str(o_attr)+"\n"+ sent+"\n")


par=Parser()
print par.parse_sent("Play a song")

# verify_coms()

# p= stanford.StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz", 
# 								path_to_jar="/home/aneesh/git_projects/team12cs243/stanford-parser.jar",
# 								path_to_models_jar="/home/aneesh/git_projects/team12cs243/stanford-parser-3.5.2-models.jar"
# 								)
# sent = "play a song"
# res=parse_sent(sent,p)
# print res['input']
# print res['verb']
# print res['object']

# iterator=p.raw_parse(sent)
# root=iterator.next(	)
# #print y.leaves()
# # tree_file.write(sent +"\n" +root.pretty_print() +"\n\n\n")
# root.pretty_print()
# s=root[0]
# # s.pretty_print()
# for child in s:
# 	if (child.label()=="VP"):
# 		child.parent=s
# 		(verb,tree) = extract_pred(child)
# 		(obj,otree)=extract_obj(tree)
# 		print verb
# 		print extract_attr(tree)
# 		print obj
# 		print extract_attr(otree)