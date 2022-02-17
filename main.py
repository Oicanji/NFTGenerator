from PIL import Image
import os

from patterns import *
from algorithm import *
from image import *

def cleared():
    clear = lambda: os.system('cls')
    clear()

def main():
    cleared()
    print("-"*50)
    print('hello world, to '+'\033[92m'+'NFT'+'\033[0m'+' generator')
    print('this is developed by '+'\033[93m'+'@Oicaji'+'\033[0m')
    print('testing version, using WeirdoAnime from example')
    print("-"*50)
    menu()

def menu():
    print('options: [0] exit, [1] create example, [2] manual input images, [3] execute algorithm')
    option = input('respost: ')
    print("-"*50)
    if option == '1':
        createExample()
    elif option == '2':
        manualInputs()
    elif option == '0':
        exit()
    elif option == '3':
        cleared()
        algorithm()
    else:
        print('invalid respost')
        menu()

def algorithm():
    print("-"*50)
    print('Really want to execute algorithm?')
    print('now that the thing is serious... \n')

    algorithmMenu()

def algorithmMenu():
    print('options: [0] back, [1] possible combinations')
    option = input('respost: ')
    if option == '0':
        menu()
    elif option == '1':
        result = getMaxCombinations()
        print('\n'+'\033[92m'+'All possibles combinations is '+str(result)+' images\033[0m')
        print('you will continue with this...\n')
    algorithm()

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

def manualMenu(part, pattern_added):
        print('What image add into \033[1m'+part['name']+'\033[0m position?')
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
                menu()
        else:
            option = option + '.png'
            if thisArchiveExists(option,part['name']):
                pattern_added.append({'file': option, 'directory': part['name']})
                black_list.append({'file': option, 'directory': part['name']})
                print('\n'+'\033[92m'+'pattern added'+'\033[0m\n')
                return
            else:
                print('\n'+'\033[91m'+'pattern not found'+'\033[0m\n')
                manualMenu(part, pattern_added)

def isRarity(part):
    if 'rarity' in part:
        print('You can add pattern to '+'\033[1m'+part['name']+'\033[0m'+' in you image?')
        print('options: [y] add pattern, [n] skip')
        option = input('respost: ')
        if option == 'y':
            return True
        elif option == 'n':
            return False
        print('\n')
    else:
        return False

def isLinked(part):
    if 'linked' in part:
        if part['linked'] == 'instead':
            print('The '+'\033[1m'+part['name']+'\033[0m'+' is linked with \033[1m'+part['parent']+'\033[0m'+' you can this?')
            print('options: [y] continue to linked in \033[1m'+part['parent']+'\033[0m, [any] skip')
            option = input('respost: ')
            if option != 'y':
                #remove end of list
                black_list.pop()
            print('\n')
    return
def blackListExist(name):
    for i in black_list:
        if i['directory'] == name:
            return True
    return False
def thisFileReallyExist(part):
    directory_name = ''
    file_name = ''
    idx = 0
    for i in black_list:
        if i[1] == part:
            directory_name = i['directory']
            file_name = i['file']
            idx = black_list.index(i)

    file_slice = file_name.split(directory_name)
    file_objetive = part+file_slice
    print(file_objetive)
    if( not os.path.exists("resource/"+file_objetive) ):
        print('\033[91m'+'Error parent is not found')
        print('Please insert other file in place'+'\033[0m\n')
        #remove art['name'] from black_list
        black_list.pop(idx)
        return False
    return True
        
black_list = []      
def manualInputs():
    pattern_added = []
    print(patterns)
    for part in patterns:
        print(isRarity(part))
        print(blackListExist(part['name']))
        if isRarity(part):
            continue
        else:
            if(blackListExist(part['name'])):
                manualMenu(part, pattern_added)
                isLinked(part)

    createImage(pattern_added)
    main()

main()