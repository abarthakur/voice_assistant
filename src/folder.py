import os
cmd=raw_input("Enter the command: ")

folder="Desktop"
home= os.path.expanduser("~")

#Commands to be programmed:
#Move, copy, delete, paste, zip, open a file, search a file, open a folder, list file


#http://stackoverflow.com/questions/18860679/searching-a-directory-for-folders-and-files-using-python\
for root,dirs,files in os.walk(home):
	for name in dirs:
		if '.' not in os.path.join(root,name) and (name.lower()).endswith(folder.lower()):
			print os.path.join(root,name)


