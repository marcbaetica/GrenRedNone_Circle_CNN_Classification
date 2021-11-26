import os
from bokeh.plotting import figure, show
from PIL import Image


images = os.listdir('raw_imgs')

single = 0
triple = 0
quadruple = 0

for image in images:
    im = Image.open('raw_imgs/' + image)
    print(im.format, im.size, im.mode)
    bands = im.mode
    single = single+1 if bands == 'P' else single
    triple = triple+1 if bands == 'RGB' else triple
    quadruple = quadruple+1 if bands == 'RGBA' else quadruple

x = [1, 2, 3]
y = [single, triple, quadruple]


p = figure()
p.vbar(x=x, top=y, width=0.5)
show(p)
