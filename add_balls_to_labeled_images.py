#uses OpenCV to generate random balls based on labeling

import os

#do this in a more efficient way lol
def find_first_char(file_name):
	for char in file_name:
		if char=='n':
			print('none')
			break
		if char=='r':
			print('red')
			break
		if char=='g':
			print('green')
			break
		#else

for file in os.listdir(os.getcwd() + '/labeled_dataset/'):
	label = find_first_char(file);
	#if label is something => take action with OpenCV