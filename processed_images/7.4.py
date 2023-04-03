from PIL import Image
img = Image.open("2_processed.jpg")
watermark = Image.open("1_processed.jpg")
(w, h) = img.size
watermark = watermark.resize((w, h))

result = Image.new('RGBA', (w, h), (0, 0, 0, 0))
result.paste(img, (0, 0))
result = Image.alpha_composite(result, watermark)

result.save("result.png")