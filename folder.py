import os
cmd=raw_input("Enter the command: ")
folder="Desktop"
for root,dirs,files in os.walk("/home/hritik"):
	for name in dirs:
		if '.' not in os.path.join(root,name) and (name.lower()).endswith(folder.lower()):
			print os.path.join(root,name)
