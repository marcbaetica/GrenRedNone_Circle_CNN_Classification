#all images exactly 1024x576
#https://www.google.com/search?tbs=imgo:1,isz:ex,iszw:1024,iszh:576&tbm=isch&q=flash+comics&chips=q:flash+comics,g_1:new+52:Ym44EcWEMEM%3D&usg=AI4_-kSeaptIdmhnlHnWSvIcVslIT4ooBg&sa=X&ved=0ahUKEwj924yJzufgAhVBnq0KHcG_CtQQ4lYILigD&biw=1536&bih=754&dpr=1.25
#https://www.google.com/search?biw=1536&bih=754&tbs=imgo%3A1%2Cisz%3Aex%2Ciszw%3A1024%2Ciszh%3A576&tbm=isch&sa=1&ei=NoN8XIDKJYKQsAXnlKEY&q=batman+cartoon&oq=batman+cartoon&gs_l=img.3..0i67j0l3j0i67j0l5.5515.7478..8201...0.0..0.119.686.3j4......1....1..gws-wiz-img.......0i7i30j0i10.FUNMk1XEX8g#imgrc=4fYkc1oy72px3M:


#Need: labeled test data //TODO: generate it -> figure out how

#classification:
#- no ball
#- red ball
#- green ball
#Image aspect ration: 16:9
#image type = PNG
#resolution: x (width) (edited) 
#labeled data
#name: r_x_m_index.png (edited) 
#name example: r_1024_m_007.png (edited) 
#Deadline to create images: Tuesday night. (edited)


import os, shutil
import random

#noball, redball, greenball
options = ['n', 'r', 'g']	

#dir sturcture
working_folder = 'labeled_dataset'
working_dir = os.getcwd() + '/' + working_folder + '/'


#function to give random ball selection from py list
def choose_random(options):
	choice=random.randint(0, 2)
	return options[choice]

def zeros(number):
	if number<10: return '00'+str(number)
	if number<100: return '0'+str(number)
	if number<1000: return str(number)

#TODO remove this
n=0
r=0
g=0

index=0
for file in os.listdir(working_folder):
	choice=choose_random(options)
	shutil.move(working_dir+file, working_dir+choice+'_1024_m_'+zeros(index)+'.png') # r_1024_m_007.png
	index=index+1

	#TODO remove this
	if choice=='n': n=n+1
	if choice=='r': r=r+1
	if choice=='g': g=g+1

print('Ratio (n,r,g): ' + str(n) + ' ' + str(r) + ' ' + str(g))
print(str(index) + ' images converted.')