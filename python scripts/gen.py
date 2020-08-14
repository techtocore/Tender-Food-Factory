import pyqrcode
import png
from pyqrcode import QRCode
import csv
import os
from datetime import date
from PIL import Image, ImageDraw, ImageFont

today = date.today()
curr_date = today.strftime("%Y-%m-%d")
try:
    os.mkdir('qr')
except:
    pass

with open('sku.csv', mode='r') as file:
    next(file)
    csvFile = csv.reader(file)
    for lines in csvFile:
        s = lines[0] + '_' + lines[1] + '_' + curr_date
        # print(s)
        url = pyqrcode.create(s)
        url.png(s + '_temp.png', scale=3)

        im = Image.open(s + '_temp.png')
        im = im.convert("RGBA")
        os.remove(s + '_temp.png')

        img = Image.new('RGB', (267, 132), color=(255, 255, 255)) # 6cm x 3.5cm
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 17)
        d.text((15, 30), lines[2], fill=(0, 0, 0), font=font)
        d.text((15, 60), lines[3], fill=(0, 0, 0), font=font)
        d.text((15, 90), lines[4], fill=(0, 0, 0), font=font)

        img.paste(im, (150, 15, 261, 126))

        img.save('qr/' + s + '.png')
