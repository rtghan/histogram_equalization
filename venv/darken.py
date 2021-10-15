from PIL import Image
import os

def darken(p):
    return p*0.5

counter = 0
source_dir = 'C:/Users/chane/Downloads/EE images/100'
output_dir = 'C:/Users/chane/Downloads/EE images/100_darken'
for img in os.listdir('C:/Users/chane/Downloads/EE images/100'):
    image = Image.open(f'{source_dir}/{img}')
    image_darken = image.point(darken)
    image_darken.save(f'{output_dir}/{img}')
    print(img)
    counter += 1
print(counter)
#
# im1 = Image.open('C:/Users/chane/Downloads/EE images/100/2.jpg')
#
# im2 = im1.point(darken)
# im2.save("C:/Users/chane/Downloads/EE images/100_darken/2.jpg");