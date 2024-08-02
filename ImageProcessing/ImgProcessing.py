from PIL import Image
img = Image.open('./pokidex/astro.jpg')

img.thumbnail((400, 400))
img.save('astro.jpg', 'png')
print(img.size)
img.show()


