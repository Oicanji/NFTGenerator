from PIL import Image
from background import *

def addImage(image, source):
    new = Image.open(source).convert("RGBA")
    image.paste(new, (0, 0, width, height), new)
    return image

def createExample():
    card = createBackground()
    card = addImage(card,"resource/hair-in-background/hair-in-background1_color1.png")
    card = addImage(card,"resource/face/face1_color1.png")
    card = addImage(card,"resource/bushes/bushes1_color1.png")
    card = addImage(card,"resource/skinmark/skinmark1_color1.png")
    card = addImage(card,"resource/noise/noise1_color1.png")
    card = addImage(card,"resource/mouth/mouth1_color1.png")
    card = addImage(card,"resource/eyebrow/eyebrow1_color1.png")
    card = addImage(card,"resource/eyes/eyes1_color1.png")
    card = addImage(card,"resource/hair-in-face/hair-in-face1_color1.png")
    card = addImage(card,"resource/upper-head/upper-head1_color1.png")

    card.save("result/example.png", format="png")
    card.show()
    
def createImage(list_patterns):
    card = createBackground()
    for i in list_patterns:
        card = addImage(card,'resource/'+i['directory']+'/'+i['file'])
    card.save("result/new.png", format="png")