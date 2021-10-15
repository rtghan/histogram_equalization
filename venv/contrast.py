from PIL import Image, ImageEnhance
import os

src = 'C:/Users/chane/Downloads/EE images/1000_g'
destination = 'C:/Users/chane/Downloads/EE images/1000_0.2'

for img in os.listdir(src):
    image = Image.open(f'{src}/{img}')

    enhancer = ImageEnhance.Contrast(image)

    factor = 0.15
    img_enhanced = enhancer.enhance(factor)
    img_enhanced.save(f'{destination}/{img}')

