from PIL import Image, ImageDraw, ImageFont
import pandas


def optionone(s, r, j):
    font = ImageFont.truetype( , 90)   # First parameter is the font (address)
    option1 = Image.open( )   # Address of the template
    draw = ImageDraw.Draw(option1)
    draw.text((800, 1180), r, (0, 0, 0), font=font)   # These define the position of the text (varies based on template)
    draw.text((880, 1300), s, (0, 0, 0), font=font)
    option1.save(f'{j}.png')


def optiontwo(s, r, j):
    font = ImageFont.truetype( , 55)
    option2 = Image.open( )
    draw = ImageDraw.Draw(option2)
    draw.text((1450, 871), r, (0, 0, 0), font=font)
    draw.text((1470, 1070), s, (0, 0, 0), font=font)
    option2.save(f'{j}.png')


def optionthree(s, r, j):
    font = ImageFont.truetype( , 80)
    option3 = Image.open( )
    draw = ImageDraw.Draw(option3)
    draw.text((1060, 30), r, (0, 0, 0), font=font)
    draw.text((1135, 140), s, (0, 0, 0), font=font)
    option3.save(f'{j}.png')


def optionfour(s, r, j):
    font = ImageFont.truetype( , 80)
    option4 = Image.open( )
    draw = ImageDraw.Draw(option4)
    draw.text((270, 1067), r, (255, 255, 255), font=font)
    draw.text((383, 1228), s, (255, 255, 255), font=font)
    option4.save(f'{j}.png')

data = pandas.read_csv( )   # Address of the form data
sName = # Title of the sender list
rName = # Title of the recipient list
koption = # Title of the template choice list

sNames = []
rNames = []
options = []

for i in range(len(data[sName])):   
    sNames.append(data[sName][i])
    rNames.append(data[rName][i])
    options.append(int(data[koption][i][-1]))

for i in range(len(sNames)):
    if options[i] == 1:
        optionone(sNames[i], rNames[i], i)

    if options[i] == 2:
        optiontwo(sNames[i], rNames[i], i)

    if options[i] == 3:
        optionthree(sNames[i], rNames[i], i)

    if options[i] == 4:
        optionfour(sNames[i], rNames[i], i)
