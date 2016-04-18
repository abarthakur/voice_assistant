from nltk.parse import stanford

p= stanford.StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz", 
							path_to_jar="/home/aneesh/git_projects/team12cs243/stanford-parser.jar",
							path_to_models_jar="/home/aneesh/git_projects/team12cs243/stanford-parser-3.5.2-models.jar"
							)
sents = ['My name is Khan','Print this page','Play Boulevard of Broken Dreams']
for sent in sents:
	x=p.raw_parse(sent)
	y=x.next()
	y.pretty_print()