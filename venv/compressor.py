from PIL import Image
import os

counter = 0
source_dir = 'C:/Users/chane/Downloads/EE images/100'
output_dir = 'C:/Users/chane/Downloads/EE images/100_supercompressed'
for img in os.listdir('C:/Users/chane/Downloads/EE images/100'):
    image = Image.open(f'{source_dir}/{img}')
    image.save(f'{output_dir}/{img}', "JPEG", quality=8)
    print(img)
    counter += 1
print(counter)
# im1 = Image.open('C:/Users/chane/Downloads/EE images/100/2.jpg')
#
# im1.save("C:/Users/chane/Downloads/EE images/100 compressed 10/2.jpg", "JPEG", quality=15);
