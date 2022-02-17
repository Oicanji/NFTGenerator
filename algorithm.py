import string
import os
from decimal import Decimal

from config import *
from background import *
from image import *
from patterns import *

def menuMachine():
    clear = lambda: os.system('cls')
    clear()
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
        if 'rarity' in i:
            rand = random.randint(0,100)
            if rand <= i['rarity']:
                item = random.choice(itensInFolder(i['name']))
                canvas = addImage(canvas,'resource/'+i['name']+'/'+item)

        else:
            item = random.choice(itensInFolder(i['name']))
            canvas = addImage(canvas,'resource/'+i['name']+'/'+item)

    if(use_custom_names):
        print('\n\033[91m not implement\033[0m\n')
    else:
        name = roboName()
        print('\n\033[96m Wild '+name.upper()+' the waifu, appeared! \033[0m\n')
        canvas.save("result/"+name+"-virtual-waifu.png", format="png")
        waifu_in_cache.append(canvas)
    
parent_cache = []
def patternParent(part):
    if 'linked' in part:
        parent_cache.append(part['parent'])
    return

def verifyParent(part):
    if part['name'] in parent_cache:
        return True
    return False

def verifyRarity(part):
    if 'rarity' in part:
        rand = random.randint(0,100)
        if rand <= part['rarity']:
            return itensInFolder(part['name'])
            canvas = addImage(canvas,'resource/'+part['name']+'/'+item)
        return False
    else:
        return itensInFolder(part['name'])
        canvas = addImage(canvas,'resource/'+part['name']+'/'+item)

def searchInPart(Part, canvas):
    if verifyParent(Part):
        #aqui e quando o objeto e parente de alguem
        return
    else:
        patternParent()
        respost = verifyRarity(Part)
        #if true, is draw
        if respost != False:
            #based in length of respost, get a random item or get other
            return
    
def addCanvas(url, canvas):
    return addImage(canvas,'resource/'+url)

def automationWaifu():
    return

def automationName():
    return