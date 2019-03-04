#shutil.move ('C:\\file.txt', 'C:\\eggs\\file2.txt')  same with move
#absolute path: begins with root folder
#relative path: relative to your current working directory
#also . and .. exist linke in shell
#os.listdir('C:\\eggs') -> returns an array of file names containing their extension

import os
import shutil

#list the files in 'dataset' folder
files = os.listdir('dataset') #returns py list
print("Files found: " + str(files))

#move files to new folder '.\\labeled' with number + ''.png
label=0
for name in files:

	baseurl=os.getcwd()
	print('CWD:' + baseurl)

	src=baseurl+'/dataset/'+name
	dest=baseurl+'/labeled_dataset/'+str(label)+'.png'

	print(src + ' ' + dest)
	print("First file exists:" + str(os.path.isfile(src)))

	print(name + " " + str(label))
	shutil.copy(src, dest)
	
	label=label+1