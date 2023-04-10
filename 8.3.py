from PIL import Image, ImageDraw, ImageFont
image = Image.open('209476.jpg')
box = (100, 100, 300, 300)
cropped_img = image.crop(box)
cropped_img.save('new_image.jpg')

name = input('Введите имя того, кого вы хотите поздравить: ')

draw = ImageDraw.Draw(cropped_img)
text = name + ', поздравляю!'
font = ImageFont.truetype('arial.ttf', size=30)
textwidth, textheight = draw.textsize(text, font)
x = (cropped_img.width - textwidth) / 2
y = cropped_img.height - textheight - 10
draw.text((x, y), text, font=font, fill=(255, 0, 0, 255))

cropped_img.save('new_card.png', 'PNG')