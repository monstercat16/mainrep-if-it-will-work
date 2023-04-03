from PIL import Image

img = Image.open("209476.jpg")
(w, h) = img.size
new_size = (w//3, h//3)
resized_img = img.resize(new_size)
resized_img.save("resized_image.png")
horizontal_mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_mirror.save("horizontal_mirror.png")
vertical_mirror = img.transpose(Image.FLIP_TOP_BOTTOM)
vertical_mirror.save("vertical_mirror.png")