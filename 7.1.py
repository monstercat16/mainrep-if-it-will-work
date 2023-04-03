from PIL import Image

img = Image.open("209476.jpg")
print("209476.jpg", img.size)
print("Формат:", img.format)
print("Цветовая модель:", img.mode)

img.show()