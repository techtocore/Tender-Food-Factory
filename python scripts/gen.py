import pyqrcode
import png
from pyqrcode import QRCode
import csv
from datetime import date
from PIL import Image, ImageDraw, ImageFont

today = date.today()
curr_date = today.strftime("%Y-%m-%d")

with open('sku.csv', mode='r') as file:
    next(file)
    csvFile = csv.reader(file)
    for lines in csvFile:
        s = lines[0] + '_' + lines[1] + '_' + curr_date
        # print(s)
        url = pyqrcode.create(s)
        url.png(s + '.png', scale=4)

        im = Image.open(s + '.png')
        im = im.convert("RGBA")

        img = Image.new('RGB', (350, 200), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 18)
        d.text((30, 50), lines[2], fill=(0, 0, 0), font=font)
        d.text((30, 90), lines[3], fill=(0, 0, 0), font=font)
        d.text((30, 130), lines[4], fill=(0, 0, 0), font=font)

        img.paste(im, (180, 30, 328, 178))

        img.save(s + 'pil_text.png')
