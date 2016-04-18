from nltk.parse import stanford

def extract_pred(vp_subtree):
	#the deepest verb is the predicate
	#do BFS
	queue= [vp_subtree]
	verb = "none"
	for subtree in queue:

		if (subtree.height()>2) :#not a leaf
			for child in subtree: #note that all the children's height is at least 2
				queue.append(child)

		elif (subtree.height()==2) :
			if (subtree.label()[0] =='V'):
				verb=subtree[0]

	return verb


p= stanford.StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz", 
							path_to_jar="/home/aneesh/git_projects/team12cs243/stanford-parser.jar",
							path_to_models_jar="/home/aneesh/git_projects/team12cs243/stanford-parser-3.5.2-models.jar"
							)
# sents = ['My name is Khan','Print this page','Play Boulevard of Broken Dreams']
# for sent in sents:
# 	x=p.raw_parse(sent)
# 	y=x.next()
# 	y.pretty_print()
sent = "A rare black squirrel has become a regular visitor in our suburban garden"
iterator=p.raw_parse(sent)
root=iterator.next()
#print y.leaves()
# root.pretty_print()
s=root[0]
# s.pretty_print()
for child in s:
	if (child.label()=="VP"):
		print extract_pred(child)