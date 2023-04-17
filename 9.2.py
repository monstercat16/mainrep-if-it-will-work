from PIL import Image
import os

sdir = (r'C:\Users\Ivan\PycharmProjects\pythonProject\githubbo\processedimages')
odir = (r'C:\Users\Ivan\PycharmProjects\pythonProject\githubbo\output')

if not os.path.exists(odir):
    os.makedirs(odir)

allowed_extensions = ['.jpg', '.png']

for filename in os.listdir(sdir):
    if any(filename.endswith(ext) for ext in allowed_extensions):
        with Image.open(os.path.join(sdir, filename)) as im:
            resz = im.resize((200, 200))
            resz.save(os.path.join(odir, filename))