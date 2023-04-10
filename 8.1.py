from PIL import Image
image = Image.open('209476.jpg')
box = (100, 100, 300, 300)
cropped_image = image.crop(box)
cropped_image.save('new_image.jpg')