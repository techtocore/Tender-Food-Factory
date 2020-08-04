import pyqrcode 
import png 
from pyqrcode import QRCode
import csv
from datetime import date

today = date.today()
curr_date = today.strftime("%Y-%m-%d")

with open('sku.csv', mode ='r') as file: 
    next(file)
    csvFile = csv.reader(file)
    for lines in csvFile:
        s = lines[0] + '_' + lines[1] + '_' + curr_date
        # print(s)
        url = pyqrcode.create(s)
        url.png(s + '.png', scale = 6)
