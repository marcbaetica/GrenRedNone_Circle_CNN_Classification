#uses OpenCV to generate random balls based on labeling

import os, cv2, random

folder_name = 'labeled_dataset'
working_dir = os.getcwd() + '/' + folder_name + '/'

#do this in a more efficient way lol
def find_first_char(file_name):
	for char in file_name:
		if char=='n':
			return 'none'
			break
		if char=='r':
			return 'red'
			break
		if char=='g':
			return 'green'
			break
		else:
			return 'weird'
			print('Found a weird file with filename starting with: ' + char)
			break

def get_random_circle_parameters():
	h = random.randrange(63, 513)
	w = random.randrange(62, 962)
	if h<281: h_distance = abs(13-h)
	if h>=281: h_distance = abs(563-h)
	if w<506: w_distance = abs(12-w)
	if w>=506: w_distance = abs(1012-w)
	minimum_potential_radius = min(h_distance, w_distance)
	if minimum_potential_radius<51 : minimum_potential_radius=51
	print(h, w, minimum_potential_radius)
	r = random.randrange(50, minimum_potential_radius)
	print(r)
	return h, w, r


def draw(filename, color):
	print('DRAWING')

	h, w, r = get_random_circle_parameters()

	img = cv2.imread(working_dir + filename)
	print(working_dir + filename)
	#cv2.imshow('image', img)
	cv2.circle(img, (w, h), r, color, -1) #width left to right height top to bottom
	
	cv2.imwrite(working_dir+filename, img) #save on drive


def draw_ball(file, color):
	if color == 'red':
		print('Drawing red ball!')
		draw(file, (0,0,255))
	if color == 'green':
		print('Drawing green ball!')
		draw(file, (0,128,0))


for file in os.listdir(working_dir):
	label = find_first_char(file)
	if label == 'none':
		print('Skipping file ' + file + ' as it was labeled to be without a ball.')
	if label == 'red':
		print('Drawing a red ball in image: ' + file)
		draw_ball(file, label)
	if label == 'green':
		print('Drawing a green ball in image: ' + file)
		draw_ball(file, label)

