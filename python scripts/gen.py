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

try:
    with open('sku.csv', mode='r') as file:
        next(file)
        csvFile = csv.reader(file)
        for lines in csvFile:
            date_data = curr_date
            if len(lines[5]) > 0:
                date_data = lines[5]
            s = lines[0] + '_' + lines[1] + '_' + date_data
            # print(s)
            url = pyqrcode.create(s)
            url.png(s + '_temp.png', scale=3)

            im = Image.open(s + '_temp.png')
            im = im.convert("RGBA")
            os.remove(s + '_temp.png')

            img = Image.new('RGB', (267, 132), color=(
                255, 255, 255))  # 6cm x 3.5cm
            d = ImageDraw.Draw(img)
            font = ImageFont.truetype("arial.ttf", 17)
            d.text((15, 30), lines[2], fill=(0, 0, 0), font=font)
            d.text((15, 60), lines[3], fill=(0, 0, 0), font=font)
            d.text((15, 90), lines[4], fill=(0, 0, 0), font=font)

            img.paste(im, (150, 15, 261, 126))

            ct = 1
            if len(lines[6]) > 0:
                ct = int(lines[6])
            for i in range(ct):
                img.save('qr/' + s + '_' + str(i+1) + '.png')
except:
    print("Either the CSV file seems incorrect, or, a few libraries might be missing ")
