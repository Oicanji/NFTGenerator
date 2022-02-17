from patterns import *
from decimal import Decimal
import os

def itensInFolder(folder):
    return os.listdir('resource/'+folder)
def getMaxCombinations():
    #with patterns route, get a list of items
    some = Decimal(0)
    list_ant = []
    for i in patterns:
        length = itensInFolder(i['name'])
        items = Decimal(len(length))
        if some != 0:
            if(list_ant.__len__() != 0):
                some += some ** items
            else:
                for quant in list_ant:
                    some += quant ** items
        else:
            some = items
        list_ant.append(items)

    return some

'''def genericPond():
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
    return'''
    
def automationWaifu():
    return

def automationName():
    return