from config import multiply_difficulty
from config import context_all

cache_all_files = []

def cacheCreate(name):
    cache_all_files.append({'cache': [], 'name': name, 'multiplier': multiply_difficulty})
def multiplierLess(name):
    for i in cache_all_files:
        if i['name'] == name:
            i['multiplier'] -= 10
def multiplierReset(name):
    for i in cache_all_files:
        if i['name'] == name:
            i['multiplier'] = multiply_difficulty

def getMulyiplier(name):
    for i in cache_all_files:
        if i['name'] == name:
            return i['multiplier']
    return 0
def listCache():
    for i in cache_all_files:
        print('\n'+'\033[92m'+i['name']+'\033[0m')
        for j in i['cache']:
            print(j)
def getCache(name):
    for i in cache_all_files:
        if i['name'] == name:
            return i['cache']
    return None
def cacheAdd(name,cache):
    for i in cache_all_files:
        if i['name'] == name:
            i['cache'].append(cache)
def cacheExists(name):
    for i in cache_all_files:
        if i['name'] == name:
            return True
    return False
def emptyCache():
    cache_all_files = []

def globalContextGet():
    return context_all

def globalContextSet(value):
    context_all = value

#return true if exist in cache, family with model equals a model_name
def existsInFamily(model_name, family):
    model_name = str(model_name)
    for cache in cache_all_files:
        for i in cache['cache']:
            if i['model'] == model_name and i['family'] == family:
                return cache['name']
    return False