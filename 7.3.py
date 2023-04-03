from PIL import Image, ImageEnhance
import os

if not os.path.exists("processed_images"):
    os.mkdir("processed_images")

for i in range(0, 5):
    # Открываем изображение
    img = Image.open(f"{i}.jpg")
    contrast_img = ImageEnhance.Contrast(img).enhance(1.5)
    contrast_img.save(f"processed_images/{i}_processed.jpg")