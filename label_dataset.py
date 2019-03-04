#shutil.move ('C:\\file.txt', 'C:\\eggs\\file2.txt')  same with move
#absolute path: begins with root folder
#relative path: relative to your current working directory
#also . and .. exist linke in shell
#os.listdir('C:\\eggs') -> returns an array of file names containing their extension

import os
import shutil

#list the files in '.\\dataset'

files = os.listdir('dataset')

print(files)

#move files to new folder '.\\labeled' with number + ''.png