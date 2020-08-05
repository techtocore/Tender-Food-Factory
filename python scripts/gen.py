import pyqrcode
import png
from pyqrcode import QRCode
import csv
from datetime import date
from PIL import Image, ImageDraw

today = date.today()
curr_date = today.strftime("%Y-%m-%d")

with open('sku.csv', mode='r') as file:
    next(file)
    csvFile = csv.reader(file)
    for lines in csvFile:
        s = lines[0] + '_' + lines[1] + '_' + curr_date
        # print(s)
        url = pyqrcode.create(s)
        url.png(s + '.png', scale=6)

        im = Image.open(s + '.png')
        im = im.convert("RGBA")

        img = Image.new('RGB', (800, 300), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        d.text((10, 10), "Hello World", fill=(0, 0, 0))

        img.paste(im, (500, 50, 722, 272))

        img.save(s + 'pil_text.png')
