from functools import cache
from pickle import TRUE
import string
import os
from decimal import Decimal

from config import *
from background import *
from image import *
from patterns import *
from cache import *

def menuMachine():
    print("-"*50)
    print('\033[95mWelcome to '+sufix_project+' generator!\033[95m')
    print('\033[96mthis is developed to new '+sufix_to_reference_obj+' born in world\033[0m\n')
    opMachine()

last_instance = []
def opMachine():
    print('options: [0] exit, [1] create new '+sufix_to_reference_obj+', [2] show my last '+sufix_to_reference_obj+'.')
    print(' '*9+'[3] create collection \033[93m [2] create for you '+'\033[0m')
    option = input('respost: ')
    print("-"*50)
    clear()
    if option == '0':
        return
    elif option == '1':
        result = randomObject()
        print('\n\033[96m Wild '+result[1].upper()+' the '+sufix_to_reference_obj+', appeared! \033[0m\n')
        saveImage(result[0], result[1])
        menuMachine()
    elif option == '2':
        if last_instance == []:
            print('\033[91m'+'no have '+sufix_to_reference_obj+' in cache :( '+'\033[0m')
        else:
            last_instance[last_instance.__len__()-1].show()
    elif option == '3':
        createColletion()
    elif option == '4':
        notImplemented()
    else:
        print('\n\033[91minvalid respost \033[0m\n')
    menuMachine()

def notImplemented():
    print('\n\033[91m not implemented \033[0m\n')
    print('\n\033[91m wait for update \033[0m\n')

def createColletion():
    print('\n\033[96m You You want to name your collection? \033[0m\n')
    respost = input('[y/n]: ')
    if respost == 'y':
        name_loop = True
        while name_loop:
            clear()
            print('\n\033[96m Please, type the name of your collection: \033[0m\n')
            name = input('name: ')
            if ~folderExist(name) and name != '':
                menuCollection(name)
                name_loop = False
            elif name == 'exit':
                name_loop = False            
    else:
        #create paste name with combinations numers and letters
        name_loop = True
        while name_loop:
            letters = string.ascii_uppercase
            name = ''.join(random.choice(letters) for i in range(10))
            if ~folderExist(name):
                menuCollection(name)
                name_loop = False

def menuCollection(name):
    clear()
    print('\n\033[96mWelcome to create collections options \033[0m\n')
    print('\033[96mYou collection called by "'+name+'" \033[0m\n')
    
    print("-"*50)
    print('options: [0] cancel, [1] create 30 items collection, [2] create other size')
    option = input('respost: ')
    clear()
    if option == '0':
        return
    elif option == '1':
        createCollection(name, 30)
    elif option == '2':
        clear()
        print('\n\033[96mWhich size do you want to put?\033[0m')
        #print red
        print('\033[91mCauntion: Oversize can crash your PC\033[0m')
        print('\033[91m'+' '*11+'and it might take a while -_-\033[0m\n')
        respost = input('size: ')
        #verify if respost is a number
        if respost.isdigit():
            createCollection(name, int(respost))
        else:
            print('\n\033[91mInvalid respost\033[0m\n')
            menuCollection(name)
    else:
        print('\n\033[91minvalid respost \033[0m\n')
        menuCollection(name)

def createCollection(name, range):
    #create folder
    path = "result/"+name+"/"
    os.mkdir(path)

    #habilitate cache
    instance_ant = globalContextGet()
    if ~globalContextGet():
        globalContextSet(True)

    i = 0
    while range >= i:

        clear()
        print ('\n\033[96m'+'Creating: '+str(i+1)+' of '+str(range)+'\033[0m\n')
        clear()

        #create file
        result = randomObject()
        saveImage(result[0], result[1], path)
        i += 1
    
    print('\n\033[96m Your collection called by '+name+' was created! \033[0m\n')

    #disable cache
    if ~instance_ant:
        globalContextSet(False)


#vefify if have a folder with name
def folderExist(folder):
    if os.path.exists("resource/"+folder):
        return True
    return False

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

instances = []
def randomObject():
    canvas = createBackground()
    for i in patterns:
        searchInPart(i, canvas)

    if(use_custom_names):
        print('\n\033[91m custom names not implement \033[0m\n')
        print('\n\033[91m please desable in config.py \033[0m\n')
        instances.clear()
    else:
        name = roboName()
    
        cacheCreate(name)

        for instance in instances:
            cacheAdd(name, instance)
        if has_resize:
            canvas = resizeImage(canvas)

        last_instance.append(canvas)
        instances.clear()

        return canvas, name

parent_cache = []
def patternParent(part):
    if 'linked' in part:
        if part['linked'] == 'instead':
            rand = random.randint(0,100)
            if instead_percentage >= rand:
                return
        parent_cache.append({'parent': part['parent'], 'family': part['name']})
    return

def verifyParent(part):
    for parent in parent_cache:
        if part == parent['parent']:
            return parent['family']
    return False

def verifyRarity(part):
    if 'rarity' in part:
        rand = random.randint(0,100)
        if rand <= part['rarity']:
            return itensInFolder(part['name'])
        return False
    else:
        return itensInFolder(part['name'])

def searchInPart(part_attributes, canvas):

    is_parent = verifyParent(part_attributes['name'])
    if is_parent:
        file_name = addParent(is_parent,part_attributes['name'])
        file_dict = fileToDict(file_name, part_attributes['name'])
        addInstances(file_dict)
        addCanvas(file_name, canvas, part_attributes['name'])
    else:
        patternParent(part_attributes)
        respost = verifyRarity(part_attributes)
        if respost != False:
            analysisFile(respost[0], part_attributes['name'])
        #if true, is draw
        if respost != False:
            if respost.__len__() > 1:
                #to models items to competition
                file_dict = competition(respost, part_attributes)
                addInstances(file_dict)
                addCanvasFileDict(file_dict, canvas, part_attributes['name'])
            else:
                file_dict = fileToDict(respost[0],part_attributes['name'])
                addInstances(file_dict)
                addCanvas(respost[0], canvas, part_attributes['name'])
                
                        
def fileToDict(file, family):
    file = analysisFile(file, family)
    for tag in file['tags']:
        #cheking if have a tag with contais 'color'
        if tag.__contains__('color'):
            color = tag.replace('color','')
            #create new data 'color' to save a int color
            file['color'] = color
            #remove this tag from file['tags']
            file['tags'].remove(tag)
            break
    file['family'] = family
    return file

def addInstances(file_dict):
    instances.append(file_dict)

def getInstances():
    return instances

def addParent(parent,family):
    parent_dict = returnParent(parent)
    file_name = family+parent_dict['model']
    file_name += '_color'+parent_dict['color']
    for tag in parent_dict['tags']:
        file_name += '_'+tag
    file_name += '.png'
    return file_name

def returnParent(parent):
    for instance in instances:
        if parent == instance['family']:
            return instance
    return False

def addCanvasFileDict(file_dict,canvas,family):
    name_file = family+file_dict['model']+'_color'+file_dict['color']
    for tag in file_dict['tags']:
        name_file += '_'+tag
    return addImage(canvas, 'resource/'+family+'/'+name_file+'.png')
    

def competition(list,part_attributes):
    items_available = []
    for file in list:
        result = analysisFile(file,part_attributes['name'])
        items_available.append(result)
    for file in items_available:
        for tag in file['tags']:
            #cheking if have a tag with contais 'color'
            if tag.__contains__('color'):
                color = tag.replace('color','')
                #create new data 'color' to save a int color
                file['color'] = color
                #remove this tag from file['tags']
                file['tags'].remove(tag)
                break
    tags = []
    losers = []
    model_winner = {}
    #gerated model competition
    competition_state = True
    while competition_state:
        rand = random.randint(0,items_available.__len__()-1)
        model_winner = items_available[rand]
        tags = model_winner['tags']
        in_cached = False
        if(cache_all_files.__len__() > 0):
            in_cached = existsInFamily(rand, part_attributes['name'])
        if ~verifyCached(in_cached):
            if tags.__len__() == 0:
                #no special tags
                competition_state = False
            else:
                #special tags
                rarity_tag = tags[0]
                if rarity_tag == "r" or rarity_tag == "v" or rarity_tag == "e" or rarity_tag == "l" or rarity_tag == "m":
                    rarity_calc = rarityCalc(rarity_tag)
                    if rarity_calc:
                        competition_state = False
        if competition_state == True:
            model_winner = {}
            losers.append(items_available[rand])
            items_available.pop(rand)
        if items_available.__len__() == 0:
            items_available = losers
            losers = []
    model_winner['family'] = part_attributes['name']
    return model_winner

def verifyCached(in_cached):
    if context_all:
        if in_cached:
            multiplier = getMulyiplier(in_cached)
            rand = random.randint(0,100)
            if(rand > multiplier):
                multiplierLess(in_cached)
                return False
            else:
                return True
    return False

def analysisFile(file_name, family):
    tags = splitFilename(file_name)
    model = 0
    for string in tags:
        if family in string:
            model = string.replace(family,'')
            tags.remove(string)
    return {'model':model, 'tags':tags}

def splitFilename(text):
    text = text.replace('.png','')
    result = text.split('_')
    return result

def rarityCalc(rarity):
    rand = random.randint(0,100)
    if rarity == 'r':
        if rand <= 50:
            return True
        return False
    elif rarity == 'v':
        if rand <= 35:
            return True
        return False
    elif rarity == 'e':
        if rand <= 15:
            return True
        return False
    elif rarity == 'l':
        if rand <= 7:
            return True
        return False
    elif rarity == 'm':
        if rand <= 2:
            return True
        return False
    else:
        print('\n\033[91m invalid rarity \033[0m\n')

def addCanvas(url, canvas, family):
    return addImage(canvas,'resource/'+family+'/'+url)

def automationWaifu():
    return

def automationName():
    return