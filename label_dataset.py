import os
import shutil

# list the files in 'raw_imgs' folder
files = os.listdir('raw_imgs') #returns py list
print("Files found: " + str(files))

#move files to new folder '.\\labeled' with number + ''.png
label=0
for name in files:

	baseurl=os.getcwd()
	print('CWD:' + baseurl)

	src=baseurl+'/raw_imgs/'+name
	dest=baseurl+'/labeled_dataset/'+str(label)+'.png'

	print(src + ' ' + dest)
	print("First file exists:" + str(os.path.isfile(src)))

	print(name + " " + str(label))
	shutil.copy(src, dest)
	
	label=label+1