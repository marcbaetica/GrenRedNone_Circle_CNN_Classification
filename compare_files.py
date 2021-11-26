import os
from pprintpp import pprint
from PIL import Image


imgs = os.listdir('raw_imgs')

# pprint(imgs)

for img in imgs:
    print(round(os.path.getsize('raw_imgs/' + img)/1000000, 3), img)
