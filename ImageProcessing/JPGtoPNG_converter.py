import sys
import os

from PIL import Image

img_folder = sys.argv[1]
op_folder = sys.argv[2]

print(img_folder)
print(op_folder)


if not os.path.exists(op_folder):
    os.makedirs(op_folder)


for file_name in os.listdir(img_folder):
    img = Image.open(f'{img_folder}\{file_name}')
    clean_name = os.path.splitext(file_name)[0]
    print(clean_name)
    img.save(f'{op_folder}\{clean_name}.png', 'png')

    print('All done!')