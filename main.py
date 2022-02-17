from ast import pattern
from PIL import Image
import random
import os

from background import *
from patterns import *

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

def main():
    print("-"*50)
    print('hello world, to '+'\033[92m'+'NFT'+'\033[0m'+' generator')
    print('this is developed by '+'\033[93m'+'@Oicaji'+'\033[0m')
    print('testing version, using WeirdoAnime from example')
    print("-"*50)
    menu()

def menu():
    print('options: [1] create example, [2] manual input images')
    option = input('respost: ')
    print("-"*50)
    if option == '1':
        createExample()
    elif option == '2':
        manualInputs()
    else:
        print('invalid respost')
        menu()

def getFiles(path):
    files = []
    path = 'resource/'+path
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)
    return files

def patterns_available(name):
    print('\npatterns available:')
    list_files = getFiles(name)
    for i in list_files:
        print('> '+i[:-4])
    print('\n')

def thisArchiveExists(name,pattern_name):
    if ( os.path.exists("resource/"+pattern_name+"/"+name) ):
        return True
    return False

def printAlredyAdded(part, pattern_added):
    print('patterns already added:')
    for i in pattern_added:
        print('\n -'+i['name'])
        print('\n')
    manualMenu(part, pattern_added)

def manualMenu(part, pattern_added):
        print('What image add into \033[1m'+part['name']+'\033[0m positon?')
        print('options: [.] view patterns available, [..] view patterns already added')
        option = input('file without extension: ')
        if option == '.':
            patterns_available(part['name'])
            manualMenu(part, pattern_added)
        elif option == '..':
            if(pattern_added.__len__() != 0):
                printAlredyAdded(part, pattern_added)
                manualMenu(part, pattern_added)
            else:
                print('\n\033[91mno patterns added yet\033[0m\n')
                manualMenu(part, pattern_added)
        else:
            option = option + '.png'
            if thisArchiveExists(option,part['name']):
                pattern_added.append({'file': option, 'directory': part['name']})
                print('\n'+'\033[92m'+'pattern added'+'\033[0m\n')
                return
            else:
                print('\n'+'\033[91m'+'pattern not found'+'\033[0m\n')
                manualMenu(part, pattern_added)


def manualInputs():
    pattern_added = []
    for part in patterns:
        if 'rarity' in part:
            print('You can add pattern to '+'\033[1m'+part['name']+'\033[0m'+' in you image?')
            print('options: [y] add pattern, [n] skip')
            option = input('respost: ')
            print('\n')
            if option == 'y':
                manualMenu(part, pattern_added)
            elif option == 'n':
                continue
        else:
            manualMenu(part, pattern_added)

    createImage(pattern_added)
    
def createImage(list_patterns):
    card = createBackground()
    for i in list_patterns:
        card = addImage(card,'resource/'+i['directory']+'/'+i['file'])
    card.save("result/new.png", format="png")
    card.show()

    menu()

main()