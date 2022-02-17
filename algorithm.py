import string
import os
from decimal import Decimal

from config import *
from background import *
from image import *
from patterns import *

def menuMachine():
    #clear = lambda: os.system('cls')
    #clear()
    print("-"*50)
    print(' Welcome to Waifu Machine ')
    print('this is developed to new waifu born in world\n')
    opMachine()

waifu_in_cache = []
def opMachine():
    print('options: [0] exit, [1] create new waifu, [2] show my last waifu')
    option = input('respost: ')
    print("-"*50)
    if option == '0':
        return
    elif option == '1':
        randomWaifu()
        menuMachine()
    elif option == '2':
        if waifu_in_cache == []:
            print('\033[91m'+'no have waifu in cache :( '+'\033[0m')
            menuMachine()
        else:
            waifu_in_cache[waifu_in_cache.__len__()-1].show()
            menuMachine()
    else:
        print('\n\033[91minvalid respost \033[0m\n')
        menuMachine()

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
def thisNameExist(name):
    if os.path.exists("result/"+name):
        return True
    return False

def roboName():
    length_of_string = 4
    name = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    while thisNameExist(name):
        name = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    return name

def randomWaifu():
    canvas = createBackground()

    for i in patterns:
        #get a random item
        item = random.choice(itensInFolder(i['name']))
        #add the item to canvas
        canvas = addImage(canvas,'resource/'+i['name']+'/'+item)

    if(use_custom_names):
        print('\n\033[91m not implement\033[0m\n')
    else:
        name = roboName()
        print('\n\033[96m Wild '+name.upper()+' the waifu, appeared! \033[0m\n')
        canvas.save("result/"+name+"-virtual-waifu.png", format="png")
        waifu_in_cache.append(canvas)
    
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