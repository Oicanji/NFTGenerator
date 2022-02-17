from PIL import Image
import random

use_background_colors = True

width = 86
height = 86

golden = {'r': 255, 'g': 188, 'b': 0, 'rarity': 15, 'name': 'golden'}
silver = {'r': 178, 'g': 189, 'b': 191, 'rarity': 40, 'name': 'silver'}
red =    {'r': 236, 'g': 16, 'b': 56, 'rarity': 5, 'name': 'red'}
blue =   {'r': 42, 'g': 110, 'b': 227, 'rarity': 30, 'name': 'blue'}

list_background_colors = [golden, silver, red, blue]

def createBackground():
    rand = random.randint(1, 10)
    if rand > 8:
        background = pond(list_background_colors)
        return Image.new("RGBA", (width, height), (background['r'], background['g'], background['b']))
    return Image.new("RGBA", (width, height), (0, 0, 0, 0))
    
def pond(list):
    total = 0
    for i in list:
        total += i['rarity']
    pond = []
    for i in list:
        pond.append((i['rarity']*100) / total)
    rand = random.randint(1, 100)
    for i in pond:
        print('tem chance real de '+str(i)+'%')
    return list[pond.index(min(pond, key=lambda x:abs(x-rand)))]