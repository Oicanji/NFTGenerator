from ast import pattern
from unicodedata import name
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
    clear = lambda: os.system('cls')
    clear()
    print("-"*50)
    print('hello world, to '+'\033[92m'+'NFT'+'\033[0m'+' generator')
    print('this is developed by '+'\033[93m'+'@Oicaji'+'\033[0m')
    print('testing version, using WeirdoAnime from example')
    print("-"*50)
    menu()

def menu():
    print('options: [0] exit, [1] create example, [2] manual input images')
    option = input('respost: ')
    print("-"*50)
    if option == '1':
        createExample()
    elif option == '2':
        manualInputs()
    elif option == '0':
        exit()
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

def printAlredyAdded(pattern_added):
    print('patterns already added:')
    for i in pattern_added:
        print('\n -'+i['name'])
        print('\n')

def manualMenu(part, pattern_added):
        print('What image add into \033[1m'+part['name']+'\033[0m positon?')
        print('options: [.] view patterns available, [..] view patterns already added')
        option = input('file without extension: ')
        if option == '.':
            patterns_available(part['name'])
            manualMenu(part, pattern_added)
        elif option == '..':
            if(pattern_added.__len__() != 0):
                printAlredyAdded(pattern_added)
                manualMenu(part, pattern_added)
            else:
                print('\n\033[91mno patterns added yet\033[0m\n')
                manualMenu(part, pattern_added)
        else:
            option = option + '.png'
            if thisArchiveExists(option,part['name']):
                pattern_added.append({'file': option, 'directory': part['name']})
                to_black_list = {'file': option, 'directory': part['name']}
                print('\n'+'\033[92m'+'pattern added'+'\033[0m\n')
                return to_black_list
            else:
                print('\n'+'\033[91m'+'pattern not found'+'\033[0m\n')
                manualMenu(part, pattern_added)

def isRarity(part,pattern_added):
    if 'rarity' in part:
        print('You can add pattern to '+'\033[1m'+part['name']+'\033[0m'+' in you image?')
        print('options: [y] add pattern, [n] skip')
        option = input('respost: ')
        if option == 'y':
            return True
        elif option == 'n':
            return False
    else:
        return True

def isLinked(part,black_list):
    if 'linked' in part:
        if part['linked'] == 'instead':
            print('The '+'\033[1m'+part['name']+'\033[0m'+' is linked with \033[1m'+part['parent']+'\033[0m'+' you can this?')
            print('options: [y] continue to linked in \033[1m'+part['parent']+'\033[0m, [any] skip')
            option = input('respost: ')
            if option == 'y':
                black_list.append(part['parent'])
        elif part['closed'] == 'instead':
            black_list.append(part['parent'])
    return
def blackListExist(list, name):
    for i in list:
        print(i)
        if i['directory'] == name:
            return True
    return False
def thisFileReallyExist(part,black_list):
    directory_name = ''
    file_name = ''
    idx = -1
    for i in black_list:
        if i['directory'] == part['name']:
            directory_name = i['directory']
            file_name = i['file']
            idx = int(i)
    #remove de diretory name from file name
    #and add part['name'] to file name
    file_slice = file_name.split(directory_name)
    file_objetive = part[name]+file_slice
    print(file_objetive)
    if( not os.path.exists("resource/"+file_objetive) ):
        print('\033[91m'+'Error parent is not found')
        print('Please insert other file in place'+'\033[0m\n')
        #remove art['name'] from black_list
        black_list.pop(idx)
            
def manualInputs():
    pattern_added = []
    black_list = [{'directory': '-1'}]
    for part in patterns:
        if blackListExist(black_list,part['name']):
            thisFileReallyExist(part,black_list)
            continue
        if isRarity(part, pattern_added) and not blackListExist(black_list,part['name']):
            isLinked(part,black_list)
            respost_manualMenu = manualMenu(part, pattern_added)
            if respost_manualMenu != None:
                black_list.append(respost_manualMenu)

    createImage(pattern_added)
    menu()
    
def createImage(list_patterns):
    card = createBackground()
    for i in list_patterns:
        card = addImage(card,'resource/'+i['directory']+'/'+i['file'])
    card.save("result/new.png", format="png")

main()