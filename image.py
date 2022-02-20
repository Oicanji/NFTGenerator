from PIL import Image
from background import *
from config import *
from patterns import *
import random
import os

def addImage(image, source):
    new = Image.open(source).convert("RGBA")
    image.paste(new, (0, 0, width, height), new)
    return image

def createExample():
    card = createBackground()
    for i in patterns:
        files = os.listdir('resource/'+i['name'])
        file = random.choice(files)
        card = addImage(card,'resource/'+i['name']+'/'+file)

    card.save("result/example.png", format="png")
    card.show()
    
def createImage(list_patterns):
    card = createBackground()
    for i in list_patterns:
        card = addImage(card,'resource/'+i['directory']+'/'+i['file'])
    if has_resize:
        card = resizeImage(card)
    card.save("result/new.png", format="png")

def resizeImage(image):
    image = image.resize((int(width*resize_width), int(height*resize_height),), Image.NEAREST)
    return image

def saveImage(canva, name, local = "result/"):
    canva.save(local+name+"-"+sufix_to_reference_obj+".png", format="png")